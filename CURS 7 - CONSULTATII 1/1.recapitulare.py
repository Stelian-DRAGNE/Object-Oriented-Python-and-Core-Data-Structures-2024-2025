
"""

matrix =    [(0,0), (0,1), (0,2),
            (1,0), (1,1), (1,2),
            (2,0), (2,1), (2,2)]

"""
matrix = []

for i in range(3):
    for j in range(3):
        print("i =", i, "j =", j)
        matrix.append((i, j))

print(matrix)


matrix = [ ((i, j)) for i in range(3) for j in range(3) ]
print(matrix)

matrix = [ [((i, j)) for i in range(3)] for j in range(3) ]
print(matrix)

matrix = str(matrix)
matrix = matrix.replace("],", ",\n").replace("[[", "[")
print(matrix)

matrix = str([ [((i, j)) for i in range(3)] for j in range(3) ]).replace("],", ",\n").replace("[[", "[")
print(matrix)