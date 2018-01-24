A = [map(int,raw_input().split()) for i in range(5)]
pos = (0,0)
for i in range(5):
    for j in range(5):
        if A[i][j] == 1:
           pos = (i,j)
ans = abs(pos[0]-2) + abs(pos[1]-2)
print(ans)
