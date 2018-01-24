n = int(raw_input())
def func(n):
    a = [4,7,47,74,447,474,477,774,747,744]
    for i in a:
        if(i == n or n%i == 0):
            print("YES")
            return
    print("NO")
func(n)