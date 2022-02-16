'''
    Author: Arman C. Heidari
'''

import numpy as np


def multiply(k, v):
    return map((lambda x: x * k), v)


def proj(v1, v2):
    k = np.dot(v2, v1) / np.dot(v1, v1)
    return multiply(k, v1)


def gram_schmidt(X, row_vecs=True, norm=True):
    if not row_vecs:
        X = X.T
    Y = X[0:1, :].copy()
    for i in range(1, X.shape[0]):
        proj = np.diag(
            (X[i, :].dot(Y.T)/np.linalg.norm(Y, axis=1)**2).flat).dot(Y)
        Y = np.vstack((Y, X[i, :] - proj.sum(0)))
    if norm:
        Y = np.diag(1/np.linalg.norm(Y, axis=1)).dot(Y)
    if row_vecs:
        return Y
    else:
        return Y.T


A = np.array([[3, 1], [2, 2]])

print(np.array(gram_schmidt(A)))
