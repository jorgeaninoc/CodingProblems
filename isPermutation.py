def isPermutation(string1,string2):
    if len(string1) > len(string2) or len(string1) < len(string2):
        return False
    sum1 = 0
    sum2 = 0
    for i in string1:
        sum1 += ord(i)
    for i in string2:
        sum2 += ord(i)
    if sum1 == sum2:
        return True
    return False


print(isPermutation("hola","ahloo"))
