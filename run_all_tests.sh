#!/bin/bash

# 定义构建目录
BUILD_DIR="./build"

# 定义测试用例数组
#TEST_CASES=("one_cube" "rotated_cuboid" "two_cuboids" "one_sphere" "one_cylinder" "rotated_cylinder" "three_cuboids_one_cylinder" "torus" "torus_cube" "single_torus" "spot" "double_torus" "bunny" "ex_163" "ex_164" "ex_165" "ex_166" "ex_167" "ex_168" "ex_169" "ex_170" "ex_171" "ex_172" "ex_173" "ex_174" "ex_175" "ex_176" "base" "ex_162" "hallway" "ex_161" "ex_160" "ex_011" "ex_023" "ex_039" "ex_040" "ex_041" "ex_043" "ex_045" "ex_046" "ex_050" "ex_054" "ex_056" "ex_057" "ex_059" "ex_060" "ex_062" "ex_065" "ex_066" "ex_067" "ex_068" "ex_069" "ex_072" "ex_074" "ex_075" "ex_078" "ex_079" "ex_081" "ex_082" "ex_090" "ex_091" "ex_096" "ex_098" "ex_101" "ex_102" "ex_103" "ex_104" "ex_105" "ex_106" "ex_107" "ex_108" "ex_109" "ex_111" "ex_112" "ex_114" "ex_115" "ex_117" "ex_118" "ex_122" "ex_123" "ex_126" "ex_127" "ex_128" "ex_129" "ex_130" "ex_131" "ex_133" "ex_134" "ex_139" "ex_140" "ex_142" "ex_143" "ex_144" "ex_145" "ex_146" "ex_147" "ex_148" "ex_150" "ex_151" "ex_152" "ex_153" "ex_155" "ex_156" "ex_157" "ex_158" "ex_159")
# 定义测试用例数组
TEST_CASES=(
    "cube_cube_cylinder"
    "cube_cube"
    "cylinder_cylinder"
    "cylinder_ring"
    "Model_101"
    "Model_14"
    "Model_28"
    "Model_32"
    "Model_87"
    "Model_89"
    "Model_9"
    "No000256_ASSY_part0"
    "No000256_ASSY_part10"
    "No000256_ASSY_part14"
    "No000256_ASSY_part6"
    "sphere_sphere"
    "temp_7"
    "temp_8"
    "UpSmokeBox"
)

# 循环遍历测试用例并执行测试
for TEST_NAME in "${TEST_CASES[@]}"
do
  echo "Running test: $TEST_NAME"
  python3 run_tests.py "$BUILD_DIR" "$TEST_NAME"
done