'''
	author: Amir Arshia Adiban
'''

import numpy as np

def coeff(vi, v):
	return np.dot(vi, v) / np.dot(v, v)

def orthogonolize(U):
	"""
	Orthogonolize the matrix U (d x n) using Gram-Schmidt process.

	"""

	## TODO ##
	##################################
	V = []
    for x in X:
        tmp = x
        for v in V:
            proj = coff(x, v) * v
            tmp = tmp - proj
        V.append(tmp)
	##################################

	return V


if __name__ == "__main__":

	# each row is a vector
	U1 = np.array([[3.0, 1.0],
                   [2.0, 2.0]])

	U2 = np.array([[1.0, 1.0, 0.0],
                   [1.0, 3.0, 1.0],
                   [2.0, -1.0, 1.0]])

	V1 = orthogonolize(U1)
	print(V1)

	V2 = orthogonolize(U2)
	print(V2)