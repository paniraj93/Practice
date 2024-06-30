mat = [[1,2,2,3],[3,1,4,2],[1,5,3,3],[1,2,1,1]]
res =[]
n = len(mat)-1
m = len(mat[0])-1
i = j = s = 0
s = mat[i][j]
while i<n and j<m:
        if mat[i][j+1]<mat[i+1][j]:
            j += 1
        else:
            i += 1
        s += mat[i][j]
        res.append(mat[i][j])

if i==n:
    while j<m:
        j+=1
        s += mat[i][j]
        res.append(mat[i][j])
elif j==m:
    while i<n:
        i+=1
        s += mat[i][j]
        res.append(mat[i][j])
print(res,s)