#!/bin/bash

# 定义构建目录
BUILD_DIR="./build"

# 定义测试用例数组
#TEST_CASES=("one_cube" "rotated_cuboid" "two_cuboids" "one_sphere" "one_cylinder" "rotated_cylinder" "three_cuboids_one_cylinder" "torus" "torus_cube" "single_torus" "spot" "double_torus" "bunny" "ex_163" "ex_164" "ex_165" "ex_166" "ex_167" "ex_168" "ex_169" "ex_170" "ex_171" "ex_172" "ex_173" "ex_174" "ex_175" "ex_176" "base" "ex_162" "hallway" "ex_161" "ex_160" "ex_011" "ex_023" "ex_039" "ex_040" "ex_041" "ex_043" "ex_045" "ex_046" "ex_050" "ex_054" "ex_056" "ex_057" "ex_059" "ex_060" "ex_062" "ex_065" "ex_066" "ex_067" "ex_068" "ex_069" "ex_072" "ex_074" "ex_075" "ex_078" "ex_079" "ex_081" "ex_082" "ex_090" "ex_091" "ex_096" "ex_098" "ex_101" "ex_102" "ex_103" "ex_104" "ex_105" "ex_106" "ex_107" "ex_108" "ex_109" "ex_111" "ex_112" "ex_114" "ex_115" "ex_117" "ex_118" "ex_122" "ex_123" "ex_126" "ex_127" "ex_128" "ex_129" "ex_130" "ex_131" "ex_133" "ex_134" "ex_139" "ex_140" "ex_142" "ex_143" "ex_144" "ex_145" "ex_146" "ex_147" "ex_148" "ex_150" "ex_151" "ex_152" "ex_153" "ex_155" "ex_156" "ex_157" "ex_158" "ex_159")
# 定义测试用例数组
#TEST_CASES=(
#    "ABC_14"
#    "ABC_180"
#    "ABC_239"
#    "ABC_240"
#    "ABC_265"
#    "ABC_266"
#    "ABC_268"
#    "ABC_296"
#    "ABC_32"
#    "ABC_370"
#    "ABC_372"
#    "ABC_375"
#    "ABC_38"
#    "ABC_389"
#    "ABC_42"
#    "ABC_447"
#    "ABC_49"
#    "ABC_50"
#    "ABC_65"
#    "ABC_68"
#    "ABC_69"
#    "ABC_7"
#    "ABC_77"
#    "ABC_8"
#    "ABC_9"
#    "ABC_9000"
#    "ABC_9005"
#    "ABC_9013"
#    "ABC_9016"
#    "ABC_9017"
#    "ABC_9030"
#    "ABC_9031"
#    "ABC_9035"
#    "ABC_9039"
#    "ABC_9041"
#    "ABC_9043"
#    "ABC_9044"
#    "ABC_9045"
#    "ABC_9051"
#    "ABC_9052"
#    "ABC_9066"
#    "ABC_9072"
#    "ABC_9074"
#    "ABC_9077"
#    "ABC_9078"
#    "ABC_9090"
#    "ABC_9099"
#    "ABC_9103"
#    "ABC_9105"
#    "ABC_9108"
#    "ABC_9113"
#    "ABC_9120"
#    "ABC_9124"
#    "ABC_9808"
#    "ABC_9819"
#    "ABC_9829"
#    "ABC_9835"
#    "ABC_9865"
#    "ABC_9875"
#    "ABC_9887"
#    "ABC_9892"
#    "ABC_9893"
#    "ABC_9896"
#    "ABC_9924"
#    "ABC_9927"
#    "ABC_9931"
#    "ABC_9934"
#    "ABC_9947"
#    "ABC_9951"
#    "ABC_9954"
#    "ABC_9959"
#    "cube_cube"
#    "cube_cube_cylinder"
#    "cylinder_cylinder"
#    "cylinder_ring"
#    "Model_101"
#    "Model_14"
#    "Model_28"
#    "Model_32"
#    "Model_87"
#    "Model_89"
#    "Model_9"
#    "No000256_ASSY_part0"
#    "No000256_ASSY_part10"
#    "No000256_ASSY_part14"
#    "No000256_ASSY_part6"
#    "sphere_sphere"
#    "temp_7"
#    "temp_8"
#    "UpSmokeBox"
#)
# 定义测试用例数组
TEST_CASES=(
#    "ABC_32"
#    "ABC_68"
#    "ABC_77"
    "ABC_180"
#    "ABC_265"
#    "ABC_266"
#    "ABC_375"
#    "ABC_447"
#    "ABC_9000"
#    "ABC_9013"
#    "ABC_9044"
#    "ABC_9072"
#    "ABC_9078"
#    "ABC_9099"
#    "ABC_9113"
#    "ABC_9120"
#    "ABC_9124"
#    "ABC_9808"
#    "ABC_9829"
#    "ABC_9875"
#    "ABC_9892"
#    "ABC_9896"
#    "ABC_9924"
#    "ABC_9934"
#    "ABC_9954"
)

# 定义保存测试时间的文件
TEST_TIME_LOG="test_time_log.txt"

# 循环遍历测试用例并执行测试
for TEST_NAME in "${TEST_CASES[@]}"
do
  echo "Running test: $TEST_NAME"

  # 记录测试开始时间
  START_TIME=$(date +%s)

  # 执行测试
  python3 run_tests.py "$BUILD_DIR" "$TEST_NAME"

  # 记录测试结束时间
  END_TIME=$(date +%s)

  # 计算测试运行时间（秒）
  ELAPSED_TIME=$((END_TIME - START_TIME))

  # 将测试用例名称和运行时间写入日志文件
#  echo "$TEST_NAME: $ELAPSED_TIME seconds" >> "$TEST_TIME_LOG"
done

echo "All tests completed. Test times logged in $TEST_TIME_LOG"