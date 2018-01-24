x = list(map(int,raw_input().split()))
k = x[0]
n = x[1]
w = x[2]
s = 0
for i in range(w):
    s += k * (i+1)

if n - s >= 0:
    print(0)
else:
    print(abs(n-s))