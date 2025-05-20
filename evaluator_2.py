import open3d as o3d
import numpy as np
from scipy.spatial import cKDTree
import cv2
from skimage.metrics import structural_similarity as ssim
from collections import Counter
import pandas as pd

# Chamfer Distance
def compute_chamfer_distance(mesh1, mesh2, num_samples=10000):
    pcd1 = mesh1.sample_points_uniformly(number_of_points=num_samples)
    pcd2 = mesh2.sample_points_uniformly(number_of_points=num_samples)
    pts1 = np.asarray(pcd1.points)
    pts2 = np.asarray(pcd2.points)
    tree1 = cKDTree(pts1)
    tree2 = cKDTree(pts2)
    dist1, _ = tree1.query(pts2)
    dist2, _ = tree2.query(pts1)
    cd = (np.mean(dist1**2) + np.mean(dist2**2)) / 2
    return cd

# Normal Consistency
def compute_normal_consistency(mesh1, mesh2, num_samples=10000):
    pcd1 = mesh1.sample_points_uniformly(number_of_points=num_samples)
    pcd2 = mesh2.sample_points_uniformly(number_of_points=num_samples)
    pcd1.estimate_normals()
    pcd2.estimate_normals()
    normals1 = np.asarray(pcd1.normals)
    normals2 = np.asarray(pcd2.normals)
    min_len = min(len(normals1), len(normals2))
    normals1 = normals1[:min_len]
    normals2 = normals2[:min_len]
    normals1 /= np.linalg.norm(normals1, axis=1, keepdims=True)
    normals2 /= np.linalg.norm(normals2, axis=1, keepdims=True)
    cos_sim = np.einsum('ij,ij->i', normals1, normals2)
    nc = np.mean(np.abs(cos_sim))
    return nc

# Boundary Point Extraction
def extract_boundary_points(mesh):
    triangles = np.asarray(mesh.triangles)
    edges = np.vstack([
        triangles[:, [0, 1]],
        triangles[:, [1, 2]],
        triangles[:, [2, 0]],
    ])
    edges = np.sort(edges, axis=1)
    edges_tuple = [tuple(e) for e in edges]
    edge_counts = Counter(edges_tuple)
    boundary_edges = [e for e, count in edge_counts.items() if count == 1]
    boundary_vertex_indices = np.unique(np.array(boundary_edges).flatten()).astype(np.int64)
    boundary_points = np.asarray(mesh.vertices)[boundary_vertex_indices]
    return boundary_points

# Edge Chamfer Distance
def compute_edge_chamfer_distance(mesh1, mesh2):
    edge_pts1 = extract_boundary_points(mesh1)
    edge_pts2 = extract_boundary_points(mesh2)
    if len(edge_pts1) == 0 or len(edge_pts2) == 0:
        print("Warning: One of the meshes has no boundary points.")
        return np.inf
    tree1 = cKDTree(edge_pts1)
    tree2 = cKDTree(edge_pts2)
    dist1, _ = tree1.query(edge_pts2)
    dist2, _ = tree2.query(edge_pts1)
    ecd = (np.mean(dist1**2) + np.mean(dist2**2)) / 2
    return ecd

# Light Field Distance (LFD)
def render_mesh_views(mesh, num_views=20, image_size=256):
    vis = o3d.visualization.Visualizer()
    vis.create_window(visible=False, width=image_size, height=image_size)
    mesh.compute_vertex_normals()
    vis.add_geometry(mesh)

    ctr = vis.get_view_control()
    ctr.set_zoom(0.7)  # 缩放，确保mesh在画面中
    vis.get_render_option().background_color = np.asarray([1.0, 1.0, 1.0])  # 白底
    vis.get_render_option().mesh_show_back_face = True

    images = []
    angles = np.linspace(0, 360, num_views, endpoint=False)
    for angle in angles:
        ctr.rotate(int(angle), 0)
        vis.poll_events()
        vis.update_renderer()
        img = vis.capture_screen_float_buffer(do_render=True)
        img = (np.asarray(img) * 255).astype(np.uint8)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
        images.append(binary)
    vis.destroy_window()
    return images

def compute_lfd(mesh1, mesh2, num_views=20):
    imgs1 = render_mesh_views(mesh1, num_views)
    imgs2 = render_mesh_views(mesh2, num_views)
    ssim_scores = []
    for im1, im2 in zip(imgs1, imgs2):
        score = ssim(im1, im2)
        ssim_scores.append(score)
    return 1 - np.mean(ssim_scores)

# Relative Volume Difference
def compute_relative_volume_difference(mesh1, mesh2):
    vol1 = mesh1.get_volume()
    vol2 = mesh2.get_volume()
    if vol1 + vol2 == 0:
        return 0.0
    return abs(vol1 - vol2) / ((vol1 + vol2) / 2)

# Example usage:
if __name__ == "__main__":
    mesh1_path = r"E:\Projects\zjx\inversecsg\InverseCSG\decomposable\ABC_9954\csg\solution_0.stl"
    mesh2_path = r"C:\Users\Julien-CAD\Desktop\siggraph_stl\ABC_9954.STL"
    # 加载两个网格文件
    mesh1 = o3d.io.read_triangle_mesh(mesh1_path)
    mesh2 = o3d.io.read_triangle_mesh(mesh2_path)

    chamfer = compute_chamfer_distance(mesh1, mesh2)
    normal_consistency = compute_normal_consistency(mesh1, mesh2)
    edge_chamfer = compute_edge_chamfer_distance(mesh1, mesh2)
    lfd = compute_lfd(mesh1, mesh2)
    # relative_vol_diff = compute_relative_volume_difference(mesh1, mesh2)

    print("Chamfer Distance:", chamfer)
    print("Normal Consistency:", normal_consistency)
    print("Edge Chamfer Distance:", edge_chamfer)
    print("Light Field Distance:", lfd)
    # print("Relative Volume Difference:", relative_vol_diff)

    # 保存到 Excel
    results = {
    "CD": [chamfer],
    "NC": [normal_consistency],
    "ECD": [edge_chamfer],
    "LFD": [lfd],
    # "Relative Volume Difference": [relative_vol_diff],
}
    df = pd.DataFrame(results)
    df.to_excel("mesh_comparison_results.xlsx", index=False)
    print("Results saved to mesh_comparison_results.xlsx")
