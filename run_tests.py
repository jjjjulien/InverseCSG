import os
import sys

# Usage: python3 run_tests.py <build_dir> <test_name>
# Example:
# python3 run_tests.py ../build one_cube
# python3 run_tests.py ../build one_sphere
# python3 run_tests.py ../build 001
# python3 run_tests.py ../build 011

if len(sys.argv) < 3:
  print('Error: please specify the test case name.')
  sys.exit(-1)

build_dir = sys.argv[1]
test_name = sys.argv[2]

if test_name == 'ABC_14':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_14 --mesh decomposable/ABC_14/ABC_14.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_180':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_180 --mesh decomposable/ABC_180/ABC_180.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_239':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_239 --mesh decomposable/ABC_239/ABC_239.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_240':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_240 --mesh decomposable/ABC_240/ABC_240.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_265':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_265 --mesh decomposable/ABC_265/ABC_265.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_266':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_266 --mesh decomposable/ABC_266/ABC_266.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_268':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_268 --mesh decomposable/ABC_268/ABC_268.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_296':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_296 --mesh decomposable/ABC_296/ABC_296.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_32':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_32 --mesh decomposable/ABC_32/ABC_32.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_370':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_370 --mesh decomposable/ABC_370/ABC_370.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_372':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_372 --mesh decomposable/ABC_372/ABC_372.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_375':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_375 --mesh decomposable/ABC_375/ABC_375.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_38':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_38 --mesh decomposable/ABC_38/ABC_38.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_389':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_389 --mesh decomposable/ABC_389/ABC_389.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_42':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_42 --mesh decomposable/ABC_42/ABC_42.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_447':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_447 --mesh decomposable/ABC_447/ABC_447.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_49':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_49 --mesh decomposable/ABC_49/ABC_49.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_50':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_50 --mesh decomposable/ABC_50/ABC_50.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_65':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_65 --mesh decomposable/ABC_65/ABC_65.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_68':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_68 --mesh decomposable/ABC_68/ABC_68.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_69':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_69 --mesh decomposable/ABC_69/ABC_69.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_7':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_7 --mesh decomposable/ABC_7/ABC_7.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_77':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_77 --mesh decomposable/ABC_77/ABC_77.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_8':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_8 --mesh decomposable/ABC_8/ABC_8.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9 --mesh decomposable/ABC_9/ABC_9.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9000':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9000 --mesh decomposable/ABC_9000/ABC_9000.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9005':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9005 --mesh decomposable/ABC_9005/ABC_9005.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9013':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9013 --mesh decomposable/ABC_9013/ABC_9013.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9016':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9016 --mesh decomposable/ABC_9016/ABC_9016.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9017':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9017 --mesh decomposable/ABC_9017/ABC_9017.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9030':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9030 --mesh decomposable/ABC_9030/ABC_9030.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9031':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9031 --mesh decomposable/ABC_9031/ABC_9031.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9035':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9035 --mesh decomposable/ABC_9035/ABC_9035.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9039':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9039 --mesh decomposable/ABC_9039/ABC_9039.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9041':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9041 --mesh decomposable/ABC_9041/ABC_9041.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9043':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9043 --mesh decomposable/ABC_9043/ABC_9043.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9044':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9044 --mesh decomposable/ABC_9044/ABC_9044.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9045':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9045 --mesh decomposable/ABC_9045/ABC_9045.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9051':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9051 --mesh decomposable/ABC_9051/ABC_9051.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9052':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9052 --mesh decomposable/ABC_9052/ABC_9052.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9066':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9066 --mesh decomposable/ABC_9066/ABC_9066.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9072':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9072 --mesh decomposable/ABC_9072/ABC_9072.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9074':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9074 --mesh decomposable/ABC_9074/ABC_9074.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9077':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9077 --mesh decomposable/ABC_9077/ABC_9077.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9078':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9078 --mesh decomposable/ABC_9078/ABC_9078.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9090':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9090 --mesh decomposable/ABC_9090/ABC_9090.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9099':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9099 --mesh decomposable/ABC_9099/ABC_9099.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9103':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9103 --mesh decomposable/ABC_9103/ABC_9103.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9105':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9105 --mesh decomposable/ABC_9105/ABC_9105.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9108':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9108 --mesh decomposable/ABC_9108/ABC_9108.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9113':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9113 --mesh decomposable/ABC_9113/ABC_9113.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9120':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9120 --mesh decomposable/ABC_9120/ABC_9120.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9124':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9124 --mesh decomposable/ABC_9124/ABC_9124.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9808':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9808 --mesh decomposable/ABC_9808/ABC_9808.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9819':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9819 --mesh decomposable/ABC_9819/ABC_9819.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9829':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9829 --mesh decomposable/ABC_9829/ABC_9829.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9835':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9835 --mesh decomposable/ABC_9835/ABC_9835.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9865':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9865 --mesh decomposable/ABC_9865/ABC_9865.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9875':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9875 --mesh decomposable/ABC_9875/ABC_9875.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9887':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9887 --mesh decomposable/ABC_9887/ABC_9887.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9892':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9892 --mesh decomposable/ABC_9892/ABC_9892.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9893':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9893 --mesh decomposable/ABC_9893/ABC_9893.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9896':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9896 --mesh decomposable/ABC_9896/ABC_9896.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9924':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9924 --mesh decomposable/ABC_9924/ABC_9924.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9927':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9927 --mesh decomposable/ABC_9927/ABC_9927.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9931':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9931 --mesh decomposable/ABC_9931/ABC_9931.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9934':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9934 --mesh decomposable/ABC_9934/ABC_9934.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9947':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9947 --mesh decomposable/ABC_9947/ABC_9947.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9951':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9951 --mesh decomposable/ABC_9951/ABC_9951.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9954':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9954 --mesh decomposable/ABC_9954/ABC_9954.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'ABC_9959':
    os.system('python3 main.py --builddir %s --outdir decomposable/ABC_9959 --mesh decomposable/ABC_9959/ABC_9959.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'cube_cube_cylinder':
    os.system('python3 main.py --builddir %s --outdir decomposable/cube_cube_cylinder --mesh decomposable/cube_cube_cylinder/cube_cube_cylinder.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'cube_cube':
    os.system('python3 main.py --builddir %s --outdir decomposable/cube_cube --mesh decomposable/cube_cube/cube_cube.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'cylinder_cylinder':
    os.system('python3 main.py --builddir %s --outdir decomposable/cylinder_cylinder --mesh decomposable/cylinder_cylinder/cylinder_cylinder.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'cylinder_ring':
    os.system('python3 main.py --builddir %s --outdir decomposable/cylinder_ring --mesh decomposable/cylinder_ring/cylinder_ring.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'Model_101':
    os.system('python3 main.py --builddir %s --outdir decomposable/Model_101 --mesh decomposable/Model_101/Model_101.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'Model_14':
    os.system('python3 main.py --builddir %s --outdir decomposable/Model_14 --mesh decomposable/Model_14/Model_14.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'Model_28':
    os.system('python3 main.py --builddir %s --outdir decomposable/Model_28 --mesh decomposable/Model_28/Model_28.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'Model_32':
    os.system('python3 main.py --builddir %s --outdir decomposable/Model_32 --mesh decomposable/Model_32/Model_32.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'Model_87':
    os.system('python3 main.py --builddir %s --outdir decomposable/Model_87 --mesh decomposable/Model_87/Model_87.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'Model_89':
    os.system('python3 main.py --builddir %s --outdir decomposable/Model_89 --mesh decomposable/Model_89/Model_89.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'Model_9':
    os.system('python3 main.py --builddir %s --outdir decomposable/Model_9 --mesh decomposable/Model_9/Model_9.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'No000256_ASSY_part0':
    os.system('python3 main.py --builddir %s --outdir decomposable/No000256_ASSY_part0 --mesh decomposable/No000256_ASSY_part0/No000256_ASSY_part0.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'No000256_ASSY_part10':
    os.system('python3 main.py --builddir %s --outdir decomposable/No000256_ASSY_part10 --mesh decomposable/No000256_ASSY_part10/No000256_ASSY_part10.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'No000256_ASSY_part14':
    os.system('python3 main.py --builddir %s --outdir decomposable/No000256_ASSY_part14 --mesh decomposable/No000256_ASSY_part14/No000256_ASSY_part14.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'No000256_ASSY_part6':
    os.system('python3 main.py --builddir %s --outdir decomposable/No000256_ASSY_part6 --mesh decomposable/No000256_ASSY_part6/No000256_ASSY_part6.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'sphere_sphere':
    os.system('python3 main.py --builddir %s --outdir decomposable/sphere_sphere --mesh decomposable/sphere_sphere/sphere_sphere.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'temp_7':
    os.system('python3 main.py --builddir %s --outdir decomposable/temp_7 --mesh decomposable/temp_7/temp_7.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'temp_8':
    os.system('python3 main.py --builddir %s --outdir decomposable/temp_8 --mesh decomposable/temp_8/temp_8.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'UpSmokeBox':
    os.system('python3 main.py --builddir %s --outdir decomposable/UpSmokeBox --mesh decomposable/UpSmokeBox/UpSmokeBox.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'one_cube':
  os.system('python3 main.py --builddir %s --outdir ../one_cube --mesh example/one_cube/csg_low_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'rotated_cuboid':
  os.system('python3 main.py --builddir %s --outdir ../rotated_cuboid --mesh example/rotated_cuboid/csg_low_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'two_cuboids':
  os.system('python3 main.py --builddir %s --outdir ../two_cuboids --mesh example/two_cuboids/csg_low_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'one_sphere':
  os.system('python3 main.py --builddir %s --outdir ../one_sphere --mesh example/one_sphere/csg_high_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'one_cylinder':
  os.system('python3 main.py --builddir %s --outdir ../one_cylinder --mesh example/one_cylinder/csg_high_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'rotated_cylinder':
  os.system('python3 main.py --builddir %s --outdir ../rotated_cylinder --mesh example/rotated_cylinder/csg_high_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'three_cuboids_one_cylinder':
  os.system('python3 main.py --builddir %s --outdir ../three_cuboids_one_cylinder --mesh example/three_cuboids_one_cylinder/csg_high_res.off --eps 0.1 --surfacedensity 100 --volumedensity 10' % build_dir)
elif test_name == 'torus':
  os.system('python3 main.py --builddir %s --outdir ../torus --mesh example/torus/csg_high_res.off --eps 0.1 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'torus_cube':
  os.system('python3 main.py --builddir %s --outdir ../torus_cube --mesh example/torus_cube/csg_high_res.off --eps 0.1 --surfacedensity 400 --volumedensity 100' % build_dir)
elif test_name == 'single_torus':
  os.system('python3 main.py --builddir %s --outdir ../single_torus --mesh example/single_torus/csg_high_res.off --eps 0.1 --surfacedensity 40 --volumedensity 10' % build_dir)
elif test_name == 'spot':
  os.system('python3 main.py --builddir %s --outdir ../spot --mesh example/spot/csg_high_res.off --eps 0.1 --surfacedensity 4000 --volumedensity 100 --timeout 180' % build_dir)
elif test_name == 'double_torus':
  os.system('python3 main.py --builddir %s --outdir ../double_torus --mesh example/double_torus/csg_high_res.off --eps 0.1 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'bunny':
  os.system('python3 main.py --builddir %s --outdir ../bunny --mesh example/bunny/csg_high_res.off --eps 0.1 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'ex_163':
  os.system('python3 main.py --builddir %s --outdir ../ex_163 --mesh example/163/csg_high_res.off --eps 0.05 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_164':
  os.system('python3 main.py --builddir %s --outdir ../ex_164 --mesh example/164/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'ex_165':
  os.system('python3 main.py --builddir %s --outdir ../ex_165 --mesh example/165/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 100' % build_dir)
elif test_name == 'ex_166':
  os.system('python3 main.py --builddir %s --outdir ../ex_166 --mesh example/166/csg_high_res.off --eps 0.05 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_167':
  os.system('python3 main.py --builddir %s --outdir ../ex_167 --mesh example/167/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_168':
  os.system('python3 main.py --builddir %s --outdir ../ex_168 --mesh example/168/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_169':
  os.system('python3 main.py --builddir %s --outdir ../ex_169 --mesh example/169/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_170':
  os.system('python3 main.py --builddir %s --outdir ../ex_170 --mesh example/170/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_171':
  os.system('python3 main.py --builddir %s --outdir ../ex_171 --mesh example/171/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_172':
  os.system('python3 main.py --builddir %s --outdir ../ex_172 --mesh example/172/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_173':
  os.system('python3 main.py --builddir %s --outdir ../ex_173 --mesh example/173/csg_high_res.off --eps 0.02 --surfacedensity 4000 --volumedensity 100' % build_dir)
elif test_name == 'ex_174':
  os.system('python3 main.py --builddir %s --outdir ../ex_174 --mesh example/174/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_175':
  os.system('python3 main.py --builddir %s --outdir ../ex_175 --mesh example/175/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_176':
  os.system('python3 main.py --builddir %s --outdir ../ex_176 --mesh example/176/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'base':
  os.system('python3 main.py --builddir %s --outdir ../base --mesh example/base/csg_high_res.off --eps 0.02 --surfacedensity 2000 --volumedensity 25' % build_dir)
elif test_name == 'ex_162':
  os.system('python3 main.py --builddir %s --outdir ../162 --mesh example/162/csg_high_res.off --eps 0.02 --surfacedensity 2000 --volumedensity 25' % build_dir)
elif test_name == 'hallway':
  os.system('python3 main.py --builddir %s --outdir ../hallway --mesh example/hallway/csg_high_res.off --eps 0.02 --surfacedensity 2000 --volumedensity 100' % build_dir)
elif test_name == 'ex_161':
  os.system('python3 main.py --builddir %s --outdir ../161 --mesh example/161/csg_high_res.off --eps 0.02 --surfacedensity 2000 --volumedensity 25' % build_dir)
elif test_name == 'ex_160':
  os.system('python3 main.py --builddir %s --outdir ../ex_160 --mesh example/160/csg_high_res.off --initsample 100 --countersample 100 --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_011':
  os.system('python3 main.py --builddir %s --outdir ../ex_011 --mesh example/011/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_023':
  os.system('python3 main.py --builddir %s --outdir ../ex_023 --mesh example/023/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25 --timeout 1800' % build_dir)
elif test_name == 'ex_039':
  os.system('python3 main.py --builddir %s --outdir ../ex_039 --mesh example/039/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_040':
  os.system('python3 main.py --builddir %s --outdir ../ex_040 --mesh example/040/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_041':
  os.system('python3 main.py --builddir %s --outdir ../ex_041 --mesh example/041/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_043':
  os.system('python3 main.py --builddir %s --outdir ../ex_043 --mesh example/043/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_045':
  os.system('python3 main.py --builddir %s --outdir ../ex_045 --mesh example/045/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_046':
  os.system('python3 main.py --builddir %s --outdir ../ex_046 --mesh example/046/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_050':
  os.system('python3 main.py --builddir %s --outdir ../ex_050 --mesh example/050/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_054':
  os.system('python3 main.py --builddir %s --outdir ../ex_054 --mesh example/054/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_056':
  os.system('python3 main.py --builddir %s --outdir ../ex_056 --mesh example/056/csg_high_res.off --eps 0.02 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_057':
  os.system('python3 main.py --builddir %s --outdir ../ex_057 --mesh example/057/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_059':
  os.system('python3 main.py --builddir %s --outdir ../ex_059 --mesh example/059/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_060':
  os.system('python3 main.py --builddir %s --outdir ../ex_060 --mesh example/060/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_062':
  os.system('python3 main.py --builddir %s --outdir ../ex_062 --mesh example/062/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_065':
  os.system('python3 main.py --builddir %s --outdir ../ex_065 --mesh example/065/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_066':
  os.system('python3 main.py --builddir %s --outdir ../ex_066 --mesh example/066/csg_high_res.off --eps 0.02 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_067':
  os.system('python3 main.py --builddir %s --outdir ../ex_067 --mesh example/067/csg_high_res.off --eps 0.05 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_068':
  os.system('python3 main.py --builddir %s --outdir ../ex_068 --mesh example/068/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_069':
  os.system('python3 main.py --builddir %s --outdir ../ex_069 --mesh example/069/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_072':
  os.system('python3 main.py --builddir %s --outdir ../ex_072 --mesh example/072/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_074':
  os.system('python3 main.py --builddir %s --outdir ../ex_074 --mesh example/074/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_075':
  os.system('python3 main.py --builddir %s --outdir ../ex_075 --mesh example/075/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_078':
  os.system('python3 main.py --builddir %s --outdir ../ex_078 --mesh example/081/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_079':
  os.system('python3 main.py --builddir %s --outdir ../ex_079 --mesh example/079/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_081':
  os.system('python3 main.py --builddir %s --outdir ../ex_081 --mesh example/081/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_082':
  os.system('python3 main.py --builddir %s --outdir ../ex_082 --mesh example/082/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_090':
  os.system('python3 main.py --builddir %s --outdir ../ex_090 --mesh example/090/csg_high_res.off --eps 0.05 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_091':
  os.system('python3 main.py --builddir %s --outdir ../ex_091 --mesh example/091/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_096':
  os.system('python3 main.py --builddir %s --outdir ../ex_096 --mesh example/096/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_098':
  os.system('python3 main.py --builddir %s --outdir ../ex_098 --mesh example/098/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_101':
  os.system('python3 main.py --builddir %s --outdir ../ex_101 --mesh example/101/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_102':
  os.system('python3 main.py --builddir %s --outdir ../ex_102 --mesh example/102/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_103':
  os.system('python3 main.py --builddir %s --outdir ../ex_103 --mesh example/105/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_104':
  os.system('python3 main.py --builddir %s --outdir ../ex_104 --mesh example/104/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_105':
  os.system('python3 main.py --builddir %s --outdir ../ex_105 --mesh example/105/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_106':
  os.system('python3 main.py --builddir %s --outdir ../ex_106 --mesh example/106/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_107':
  os.system('python3 main.py --builddir %s --outdir ../ex_107 --mesh example/107/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_108':
  os.system('python3 main.py --builddir %s --outdir ../ex_108 --mesh example/108/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_109':
  os.system('python3 main.py --builddir %s --outdir ../ex_109 --mesh example/109/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_111':
  os.system('python3 main.py --builddir %s --outdir ../ex_111 --mesh example/111/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_112':
  os.system('python3 main.py --builddir %s --outdir ../ex_112 --mesh example/112/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_114':
  os.system('python3 main.py --builddir %s --outdir ../ex_114 --mesh example/114/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_115':
  os.system('python3 main.py --builddir %s --outdir ../ex_115 --mesh example/115/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_117':
  os.system('python3 main.py --builddir %s --outdir ../ex_117 --mesh example/117/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_118':
  os.system('python3 main.py --builddir %s --outdir ../ex_118 --mesh example/118/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_122':
  os.system('python3 main.py --builddir %s --outdir ../ex_122 --mesh example/122/csg_high_res.off --eps 0.01 --surfacedensity 2000 --volumedensity 50' % build_dir)
elif test_name == 'ex_123':
  os.system('python3 main.py --builddir %s --outdir ../ex_123 --mesh example/123/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_126':
  os.system('python3 main.py --builddir %s --outdir ../ex_126 --mesh example/126/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_127':
  os.system('python3 main.py --builddir %s --outdir ../ex_127 --mesh example/127/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_128':
  os.system('python3 main.py --builddir %s --outdir ../ex_128 --mesh example/128/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_129':
  os.system('python3 main.py --builddir %s --outdir ../ex_129 --mesh example/129/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_130':
  os.system('python3 main.py --builddir %s --outdir ../ex_130 --mesh example/130/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_131':
  os.system('python3 main.py --builddir %s --outdir ../ex_131 --mesh example/131/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_133':
  os.system('python3 main.py --builddir %s --outdir ../ex_133 --mesh example/133/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_134':
  os.system('python3 main.py --builddir %s --outdir ../ex_134 --mesh example/134/csg_high_res.off --eps 0.05 --surfacedensity 1000 --volumedensity 10' % build_dir)
elif test_name == 'ex_139':
  os.system('python3 main.py --builddir %s --outdir ../ex_139 --mesh example/139/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_140':
  os.system('python3 main.py --builddir %s --outdir ../ex_140 --mesh example/140/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 50' % build_dir)
elif test_name == 'ex_142':
  os.system('python3 main.py --builddir %s --outdir ../ex_142 --mesh example/142/csg_high_res.off --eps 0.01 --surfacedensity 2000 --volumedensity 50' % build_dir)
elif test_name == 'ex_143':
  os.system('python3 main.py --builddir %s --outdir ../ex_143 --mesh example/143/csg_high_res.off --eps 0.01 --surfacedensity 1000 --volumedensity 200' % build_dir)
elif test_name == 'ex_144':
  os.system('python3 main.py --builddir %s --outdir ../ex_144 --mesh example/144/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_145':
  os.system('python3 main.py --builddir %s --outdir ../ex_145 --mesh example/145/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_146':
  os.system('python3 main.py --builddir %s --outdir ../ex_146 --mesh example/146/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_147':
  os.system('python3 main.py --builddir %s --outdir ../ex_147 --mesh example/147/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_148':
  os.system('python3 main.py --builddir %s --outdir ../ex_148 --mesh example/148/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_150':
  os.system('python3 main.py --builddir %s --outdir ../ex_150 --mesh example/150/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_151':
  os.system('python3 main.py --builddir %s --outdir ../ex_151 --mesh example/151/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_152':
  os.system('python3 main.py --builddir %s --outdir ../ex_152 --mesh example/152/csg_high_res.off --eps 0.01 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_153':
  os.system('python3 main.py --builddir %s --outdir ../ex_153 --mesh example/153/csg_high_res.off --eps 0.02 --surfacedensity 1000 --volumedensity 25 --timeout 600' % build_dir)
elif test_name == 'ex_155':
  os.system('python3 main.py --builddir %s --outdir ../ex_155 --mesh example/155/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_156':
  os.system('python3 main.py --builddir %s --outdir ../ex_156 --mesh example/156/csg_high_res.off --eps 0.01 --surfacedensity 4000 --volumedensity 200' % build_dir)
elif test_name == 'ex_157':
  os.system('python3 main.py --builddir %s --outdir ../ex_157 --mesh example/157/csg_high_res.off --eps 0.1 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_158':
  os.system('python3 main.py --builddir %s --outdir ../ex_158 --mesh example/158/csg_high_res.off --eps 0.1 --surfacedensity 250 --volumedensity 25' % build_dir)
elif test_name == 'ex_159':
  os.system('python3 main.py --builddir %s --outdir ../ex_159 --mesh example/159/csg_high_res.off --eps 0.025 --surfacedensity 250 --volumedensity 25' % build_dir)
else:
  print('Unknown test case: %s' % test_name)
  sys.exit(-1)
