rows = int(input("rows: "))
col = int(input("columns: "))

matrix = []
print("entries row-wise:")

for i in range(rows):
    row = []
    for j in range(col):
        row.append(int(input()))    # user input for rows
    matrix.append(row)  # adding rows to the matrix

print("\n2D matrix is:")

for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()
