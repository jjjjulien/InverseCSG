import os
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
    cd = (np.mean(dist1) + np.mean(dist2)) / 2  # 修改为直接计算平均距离

    bbox = mesh1.get_axis_aligned_bounding_box()
    diag = np.linalg.norm(bbox.get_max_bound() - bbox.get_min_bound())
    return cd / diag if diag > 0 else cd


# Normal Consistency
def compute_normal_consistency(mesh1, mesh2, num_samples=10000):
    pcd1 = mesh1.sample_points_uniformly(number_of_points=num_samples)
    pcd2 = mesh2.sample_points_uniformly(number_of_points=num_samples)
    pcd1.estimate_normals()
    pcd2.estimate_normals()
    normals1 = np.asarray(pcd1.normals)
    normals2 = np.asarray(pcd2.normals)

    # 使用最近邻搜索找到对应点
    pts1 = np.asarray(pcd1.points)
    pts2 = np.asarray(pcd2.points)
    tree = cKDTree(pts2)
    _, indices = tree.query(pts1)

    # 计算对应点的法线余弦相似度
    normals2_matched = normals2[indices]
    cos_sim = np.einsum('ij,ij->i', normals1, normals2_matched)
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
    ecd = (np.mean(dist1) + np.mean(dist2)) / 2  # 修改为直接计算平均距离

    bbox = mesh1.get_axis_aligned_bounding_box()
    diag = np.linalg.norm(bbox.get_max_bound() - bbox.get_min_bound())
    return ecd / diag if diag > 0 else ecd


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
        ctr.rotate(angle, 0)  # 修改为直接使用浮点数角度
        vis.poll_events()
        vis.update_renderer()
        img = vis.capture_screen_float_buffer(do_render=True)
        img = (np.asarray(img) * 255).astype(np.uint8)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
        images.append(binary)
    vis.destroy_window()
    return images

def compute_lfd(mesh1, mesh2, num_views=10):
    imgs1 = render_mesh_views(mesh1, num_views)
    imgs2 = render_mesh_views(mesh2, num_views)
    ssim_scores = []
    for im1, im2 in zip(imgs1, imgs2):
        score = ssim(im1, im2)
        ssim_scores.append(score)
    lfd = 1 - np.mean(ssim_scores)

    return lfd

# Relative Volume Difference
def compute_relative_volume_difference(mesh1, mesh2):
    vol1 = mesh1.get_volume()
    vol2 = mesh2.get_volume()
    if vol1 + vol2 == 0:
        return 0.0
    return abs(vol1 - vol2) / ((vol1 + vol2) / 2)


# 原始与结果模型文件夹路径
gt_dir = r"C:\Users\Julien-CAD\Desktop\siggraph_stl"
# gen_dir = r"C:\Users\Julien-CAD\Desktop\inversecsg_result"
# gen_dir = r"C:\Users\Julien-CAD\Desktop\new_result"
gen_dir = r"C:\Users\Julien-CAD\Desktop\old_result"
# gen_dir = r"C:\Users\Julien-CAD\Desktop\d2csg_result"

indices = [32, 68, 77, 180, 265, 266, 375, 447, 9000, 9013, 9044, 9072, 9078, 9099, 9113, 9120, 9124, 9808, 9829, 9875, 9892, 9896, 9924, 9934, 9954]
# 结果列表
results = []

for i in indices:
    gt_path = os.path.join(gt_dir, f"ABC_{i}.STL")
    # gen_path = os.path.join(gen_dir, f"solution_{i}.stl")
    # gen_path = os.path.join(gen_dir, f"new_{i}.stl")
    gen_path = os.path.join(gen_dir, f"old_{i}.stl")
    # gen_path = os.path.join(gen_dir, f"{i}.stl")

    if not os.path.exists(gt_path) or not os.path.exists(gen_path):
        print(f"跳过第 {i} 对：文件不存在。")
        results.append({
            "Index": i,
            "Chamfer Distance": None,
            "Normal Consistency": None,
            "Edge Chamfer Distance": None,
            "Light Field Distance": None,
            # "Relative Volume Difference": None
        })
        continue

    mesh1 = o3d.io.read_triangle_mesh(gt_path)
    mesh2 = o3d.io.read_triangle_mesh(gen_path)

    chamfer = compute_chamfer_distance(mesh1, mesh2)
    normal_consistency = compute_normal_consistency(mesh1, mesh2)
    edge_chamfer = compute_edge_chamfer_distance(mesh1, mesh2)
    lfd = compute_lfd(mesh1, mesh2)
    # vol_diff = compute_relative_volume_difference(mesh1, mesh2)

    results.append({
        "Index": i,
        "Chamfer Distance": chamfer,
        "Normal Consistency": normal_consistency,
        "Edge Chamfer Distance": edge_chamfer,
        "Light Field Distance": lfd,
        # "Relative Volume Difference": vol_diff
    })
    print(f"完成第 {i} 对")

# 保存为 Excel
df = pd.DataFrame(results)
df.to_excel("batch_mesh_comparison_results.xlsx", index=False)
print("批量结果保存到 batch_mesh_comparison_results.xlsx")
