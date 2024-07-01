import numpy as np

# 创建一个 2x2x2 的三维数组
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# 沿 axis=0 进行求和
sum_axis_0 = np.sum(array_3d, axis=0)  # [[ 6  8]
                                       #  [10 12]]

# 沿 axis=1 进行求和
sum_axis_1 = np.sum(array_3d, axis=1)  # [[ 4  6]
                                       #  [12 14]]

# 沿 axis=2 进行求和
sum_axis_2 = np.sum(array_3d, axis=2)  # [[ 3  7]
                                       #  [11 15]]

print(f"三维数组:\n{array_3d}")
print(f"按0轴计算(axis=0):\n{sum_axis_0}")
print(f"按1轴计算(axis=1):\n{sum_axis_1}")
print(f"按2轴计算(axis=2):\n{sum_axis_2}")
