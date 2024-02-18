import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0,4.0,6.0])
#둘의 크기가 같아야 연산이 가능하다.
print(x+y)
print(type(x))

A = np.array([[1,2],[3,4]])
print(A)
# 2차원 배열 np

print(A.shape) # NXM 표시

# 브로드캐스트
A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print(A*B)
print()

#원소 접근
X = np.array([[51,55], [14,19], [0,4]])
print(X)
for row in X :
    print(row[0])

#평탄화
X = X.flatten()
print(X)
print(X>15)

#matplotlib
import matplotlib.pyplot as plt
from matplotlib.image import imread

x = np.arange(0,6,0.1) # 0에서 6까지 0.1 간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label = "sin")
plt.plot(x,y2, linestyle = "--", label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin&cos')
plt.legend()
plt.show()

# 이미지 표시하기

img = imread('../bbakk.png')
plt.imshow(img)
plt.show()

