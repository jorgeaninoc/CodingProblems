def compressString(string):
    new = ""
    aux = dict()
    last = string[0]
    for i in string:
        if i != last:
            new = new + str(last)+str(aux[last])
            aux[last] = 0
        if i in aux.keys():
            aux[i] +=1
        else:
            aux[i] = 1
        last = i
    new = new+str(last)+str(aux[last])
    return new

print(compressString("asfasdfasdfasdf"))