import trimesh

# 定义文件路径
file_path = r"E:\Projects\zjx\inversecsg\InverseCSG\decomposable\cube_cube_cylinder\cube_cube_cylinder.off"
# 定义修复后的文件保存路径
repaired_file_path = r"E:\Projects\zjx\inversecsg\InverseCSG\decomposable\cube_cube_cylinder\cube_cube_cylinder_repaired.off"

# 加载OFF文件
mesh = trimesh.load(file_path, process=False)  # 设置process=False以避免自动合并顶点

# 检查网格是否水密
if mesh.is_watertight:
    print("网格已经是水密的")
else:
    print("网格非水密，需要修复")
    # 修复网格中的孔洞
    watertight = trimesh.repair.fill_holes(mesh)
    if watertight:
        print("网格已修复为水密")
        # 保存修复后的网格
        mesh.export(repaired_file_path)
        print(f"修复后的网格已保存到：{repaired_file_path}")
    else:
        print("网格修复失败，未能修复为水密")