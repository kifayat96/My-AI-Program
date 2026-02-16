def multiply_matrix(a, b):
    result = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]
print(multiply_matrix(m1, m2))
