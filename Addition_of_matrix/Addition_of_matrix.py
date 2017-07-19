# Addition of two matrix
print("\t\t\t\t\t       ---Addition of two 3/3 matrix---")

X = [[0,0,0], [0,0,0], [0,0,0]]
Y = [[0,0,0], [0,0,0], [0,0,0]]

print("Enter the value of first matrix: ",end = '')

for a in range(len(X)):
    for b in range(len(X[0])):

        X[a][b] = input()

print("Enter the value of second matrix: ",end = '')

for c in range(len(Y)):
    for d in range(len(Y[0])):

        Y[c][d] = input()


print("")

R = [[X[x][y] + Y[x][y] for y in range(len(X[0]))] for x in range(len(X))]


print("")

for r in R:
    print(R)