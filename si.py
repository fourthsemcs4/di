from numpy import array
from numpy import tensordot
A=array([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[11,12,13],[14,15,16],[17,18,19]],
    [[21,22,23],[24,25,26],[27,28,29]]
])
print(A.shape)
print("A matrix is:\n",A)
B=array([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[11,12,13],[14,15,16],[17,18,19]],
    [[21,22,23],[24,25,26],[27,28,29]]
])
print(B.shape)
print("B matrix is:\n",B)
print("tensor addition\n")
C=A+B
print(C.shape)
print("the addition result c matrix:\n",C)
print("tensor subtraction\n")
S=A-B
print(S.shape)
print("the difference s matrix:\n",S)
print("tensor multiplication\n")
M=A*B
print(M.shape)
print("the product of scalar matrix:\n",M)
print("tensor division\n")
DI=A/B
print(DI.shape)
print("the quotient of DI:\n",DI)
D=array([1,2])
E=array([3,4])
F=tensordot(D,E,axes=0)
print("result wen axis=0:\n",F)
F=tensordot(D,E,axes=1)
print("result wen axis=1:\n",F)
