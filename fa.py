def start(var):
    if((ord(var) >= 65 and ord(var) <= 90) or (ord(var) == 95) or (ord(var) >= 97 and ord(var) <= 122)):
        return 1
    else :
        return 2

def state1(var):
    if((ord(var) >= 65 and ord(var) <= 90) or (ord(var) == 95) or (ord(var) >= 97 and ord(var) <= 122) or (ord(var) >= 48 and ord(var) <= 57)):
        return 1
    else :
        return 2

def isVariable(s):
    state = 0
    for i in range (len(s)):
        if (state == 0):
            state = start(s[i])
        if (state == 1):
            state = state1(s[i])
        if (state == 2):
            print("Variable invalid")
            return False
    print("Variable valid")
    return True