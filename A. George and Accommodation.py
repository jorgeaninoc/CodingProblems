n = int(raw_input())
cnt = 0
for i in range(n):
    r = list(map(int,raw_input().split()))
    if (r[1]-r[0]) >= 2:
        cnt +=1
print(cnt)