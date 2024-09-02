def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	
	c = [0 for i in range(len(a))]
	for i in range(len(a)):
		for j in range(len(a[0])):
			c[i] += a[i][j]*b[j]
	
	return c