import numpy as np
from numpy.random import rand

def num_of_zeros(M):
    C = np.ones(M.shape, M.dtype)
    count = 0
    for i in range(M.shape[0]): # satırları dolaşıyoruz
        for j in range(M.shape[1]): # sütunları dolaşıyoruz
            if (M[i][j] == 0): # eğer sıfır varsa
                C[i][j] = 0
                count = count + 1
    return count, C

minVal, maxVal, r, c = -10, 10, 6, 15
A = (maxVal-minVal)*rand(r,c)+minVal
B = np.round(A).astype(int)
print('A matrisinin veri tipi %s' %(A.dtype))
print('B matrisi')
print(B)
print('B matrisinin veri tipi %s' %(B.dtype))
numOfZeros, C = num_of_zeros(B)
print('B matrisindeki sıfır sayısı %i' %numOfZeros)
print('C matrisi')
print(C)