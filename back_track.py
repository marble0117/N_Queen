import numpy as np
"""
0: 空
1: Queenが存在
2: 配置不可
左から処理
"""
def counter():
    counter.count += 1

def print_mat(mat):
    temp = np.full(mat.shape, '.')
    temp[mat == 1] = 'Q'
    for l in temp:
        print(" ".join(l))
    print()


def update_mat(mat_old, i, j):
    mat = mat_old.copy()
    mat[i, j] = 1
    for k in range(j+1, N):
        mat[i, k] = 2
        if i+k-j < N:
            mat[i+k-j, k] = 2
        if i-k+j >= 0:
            mat[i-k+j, k] = 2
    return mat

def queen(mat, i, j, N):
    mat = update_mat(mat, i, j)
    # complete
    if j == N-1:
        print_mat(mat)
        counter()
    else:
        for k in range(N):
            if mat[k, j+1] == 0:
                queen(mat, k, j+1, N)


N = int(input())
#N = 13
counter.count = 0

mat = np.zeros((N, N))
for i in range(N):
    queen(mat, i, 0, N)

print("total: ", counter.count)
