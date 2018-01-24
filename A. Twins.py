n = int(raw_input())
vals = map(int,raw_input().split(" "))
s = sum(vals)
vals = sorted(vals)
b = 0
ans = n
for i in range(n-1,-1,-1):
    b += vals[i]
    if b*2 > s:
        ans = n-i
        break
print(ans)


