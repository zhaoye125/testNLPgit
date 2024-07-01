#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   np_axis_2d
@Time    :   2024/7/1 11:48
@Author  :   abu
@WeChart :   knidly
@Contact :   z2615@163.com
"""
import numpy as np

# 创建一个 2x3 的二维数组
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# 沿 axis=0 进行求和（每一列求和）
sum_axis_0 = np.sum(array_2d, axis=0)  # [5, 7, 9]

# 沿 axis=1 进行求和（每一行求和）
sum_axis_1 = np.sum(array_2d, axis=1)  # [6, 15]

print(f"二维数组:\n{array_2d}")
print(f"按0轴计算(axis=0，columns): {sum_axis_0}")
print(f"按1轴计算(axis=1，rows): {sum_axis_1}")

