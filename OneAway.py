def oneAway(string1,string2):
    aux1 = sorted(string1)
    aux2 = sorted(string2)
    cnt = 0
    i = 0
    j = 0
    if len(aux1)>=len(aux2):
        while i < len(aux1):
           if aux1[i] != aux2[j]:
               cnt +=1
               i += 1
           else:
               i += 1
               j += 1
           if cnt > 1:
               return False
    elif len(aux2) > len(aux1):
        while i < len(aux2):
           if aux2[i] != aux1[j]:
               cnt +=1
               i+=1
           else:
               i+=1
               j+=1
           if cnt > 1:
               return False
    return True
