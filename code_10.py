import os
import math
import numpy as np

# 作業ディレクトリ取得
current_dir = os.getcwd()
# 指定したディレクトリ内にあるファイルを取得
result = os.listdir(current_dir)
print(result)

# ルート2をクオーテーション型で取得
result2 = math.sqrt(2)
print(result2)

x = np.array([1, 2, 3])
y = np.array([10, 11, 12])
n = np.array([[2, 4, 5], [5, 6, 7]])
print(x + y)
print(n[0][1])
print(n[1][2])
print(x + y + n[1])
print(x + y + n[1][0])