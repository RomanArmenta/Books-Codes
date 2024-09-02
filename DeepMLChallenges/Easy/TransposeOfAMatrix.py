def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	n_ren, n_col = len(a), len(a[0])
	b = [[0 for i in range(n_ren)] for j in range(n_col)]
	for i in range(n_col):
		for j in range(n_ren):
			b[i][j] = a[j][i]
	return b