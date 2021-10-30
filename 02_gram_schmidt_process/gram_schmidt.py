import numpy as np

def orthogonolize(U):
	"""
	Orthogonolize the matrix U (d x n) using Gram-Schmidt process.

	Args:
		U (numpy.array): d x n matrix with columns that need to be orthogonolized.

	Returns:
		(numpy.array): d x n orthogonal matrix.
	"""

	V = np.array([])
	## TODO ##
	#################

	#################

	return V


if __name__ == "__main__":

	U = np.array(([[3, 1],
				  [2, 1]]))

	V = orthogonolize(U)
	print(V)

	assert V.shape == U.shape