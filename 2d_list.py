def add_matrix(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]
print(add_matrix(m1, m2))
