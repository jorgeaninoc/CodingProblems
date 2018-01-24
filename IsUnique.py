def isUnique(string):
    for i in range(len(string)):
        if string[i] in string[i+1:]:
            return False
    return True


print(isUnique("holaa"))