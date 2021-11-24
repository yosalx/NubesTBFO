#state start pada variabel
def start(var):
    if((ord(var) >= 65 and ord(var) <= 90) or (ord(var) == 95) or (ord(var) >= 97 and ord(var) <= 122)):
        return 1
    else :
        return 2

#state1 pada variabel
def state1(var):
    if((ord(var) >= 65 and ord(var) <= 90) or (ord(var) == 95) or (ord(var) >= 97 and ord(var) <= 122) or (ord(var) >= 48 and ord(var) <= 57)):
        return 1
    else :
        return 2

#fungsi utama DFA variabel
def isVariable(s):
    state = 0
    for i in range (len(s)):
        if (state == 0):
            state = start(s[i])
        if (state == 1):
            state = state1(s[i])
        if (state == 2):
            return False
    return True

#state start pada integer
def intStartState(s):
    if (ord(s) >= 48 and ord(s) <= 57):
        return 1
    else:
        return 2

#state 1 pada integer
def intState1(s):
    if (ord(s) >= 48 and ord(s) <= 57):
        return 1
    else:
        return 2

#fungsi utama pada DFA integer
def isInteger(s):
    state = 0
    for i in range (len(s)):
        if state == 0:
            state = intStartState(s[i])
        elif state == 1:
            state = intState1(s[i])
        elif state == 2:
            return False
    return True