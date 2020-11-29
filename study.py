import numpy as np
import matplotlib.pyplot as plt

# 配列x宣言
x = np.array([1.0, 2.0, 3.0])
print(x)

# 0~6の0.1刻みで指定
x = np.arange(0, 6, 0.1)
# yをsin関数で指定
y = np.sin(x)

# グラフ描画
plt.plot(x, y)
plt.show()

# グラフ描画
y = np.cos(x)
plt.plot(x, y)
plt.show()
