import numpy as np

def AND (x1, x2) :
    w1,w2,theta = 0.5, 0.5 , 0.7
    tmp = w1*x1 + w2*x2
    if tmp <= theta :
        return 0
    elif tmp > theta :
        return 1

def BiasAND (x1, x2) :
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0 :
        return 0
    else :
        return 1

print(AND(0,1))
print(AND(1,1))
print(BiasAND(1,1))

#XOR은 나타낼 수 없습니다. 0,0 0,1 1,0 1,1 네 점을 직선 하나로 분할 불가능하기 떄문에
#하지만 비선형, 즉 곡선이면 가능합니다.

