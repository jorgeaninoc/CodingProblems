s = raw_input()
w = "hello"
aux = ""
length = range(len(s))
index = 0

for i in s:
    if i in "hello":
        s = s.replace(i,"")
        aux += i

aux2 = ""

for i in aux:
    if index < len(w) and i==w[index]:
        aux2 += i
        index+=1

if aux2 == "hello":
    print("YES")
else:
    print("NO")