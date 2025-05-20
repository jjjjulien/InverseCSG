import open3d as o3d
import numpy as np
from scipy.spatial import cKDTree

def compute_chamfer_distance(mesh1, mesh2, num_samples=10000):
    """
    使用点云采样计算两个网格之间的 Chamfer Distance
    """
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

def compute_normal_consistency(mesh1, mesh2, num_samples=10000):
    """
    计算两个网格之间的 Normal Consistency（余弦相似度的绝对值平均）
    """
    pcd1 = mesh1.sample_points_uniformly(number_of_points=num_samples)
    pcd2 = mesh2.sample_points_uniformly(number_of_points=num_samples)
    pcd1.estimate_normals()
    pcd2.estimate_normals()

    normals1 = np.asarray(pcd1.normals)
    normals2 = np.asarray(pcd2.normals)

    # 点数必须一致才能一一比较
    min_len = min(len(normals1), len(normals2))
    normals1 = normals1[:min_len]
    normals2 = normals2[:min_len]

    # 单位化
    normals1 /= np.linalg.norm(normals1, axis=1, keepdims=True)
    normals2 /= np.linalg.norm(normals2, axis=1, keepdims=True)

    cos_sim = np.einsum('ij,ij->i', normals1, normals2)
    nc = np.mean(np.abs(cos_sim))  # 取绝对值避免方向相反导致负值
    return nc

def extract_boundary_points(mesh):
    """
    提取网格的边界点（即边界边的端点）
    """
    # 获取所有三角形的边
    triangles = np.asarray(mesh.triangles)
    edges = np.vstack([
        triangles[:, [0, 1]],
        triangles[:, [1, 2]],
        triangles[:, [2, 0]],
    ])

    # 将每条边按照端点顺序排序，确保无向边唯一性
    edges = np.sort(edges, axis=1)

    # 找出边界边（只出现一次的边）
    edges_tuple = [tuple(e) for e in edges]
    from collections import Counter
    edge_counts = Counter(edges_tuple)
    boundary_edges = [e for e, count in edge_counts.items() if count == 1]

    # 提取边界边的所有顶点索引
    boundary_vertex_indices = np.unique(np.array(boundary_edges).flatten())

    # 提取对应顶点坐标
    boundary_points = np.asarray(mesh.vertices)[boundary_vertex_indices]
    return boundary_points


def compute_edge_chamfer_distance(mesh1, mesh2):
    """
    计算两个网格边界点之间的 Chamfer Distance
    """
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

mesh1_path = r"E:\Projects\zjx\inversecsg\InverseCSG\decomposable\ABC_77\ABC_77.STL"
mesh2_path = r"E:\Projects\zjx\inversecsg\InverseCSG\decomposable\ABC_77\csg\solution_4.stl"
# 加载两个网格文件
mesh1 = o3d.io.read_triangle_mesh(mesh1_path)
mesh2 = o3d.io.read_triangle_mesh(mesh2_path)

# 计算Chamfer Distance
cd = compute_chamfer_distance(mesh1, mesh2)
print("Chamfer Distance:", cd)

# 计算Normal Consistency
nc = compute_normal_consistency(mesh1, mesh2)
print("Normal Consistency:", nc)

# 计算Edge Chamfer Distance
ecd = compute_edge_chamfer_distance(mesh1, mesh2)
print("Edge Chamfer Distance:", ecd)