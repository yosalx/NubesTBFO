import re
from fa import isInteger as isInt, isVariable as isVar

def file_handler(filename):
    
    file = open(filename, "r") # read from filename and save as 'file'
    file_r = file.read()
    
    # regex to slice each string at each whitespace
    file_n = re.split(r'\s+', file_r)
    
    file.close()
    
    return file_n

def basedSlice(filename):
    file = file_handler(filename)
    
    # base
    operans = ['def', 'return', 'for', 'import', 'from', 'with', 'true', 'false', 'none', 'not', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'range', 'raise', 'class', 'open', 'print', '>', '<', '>=', '<=', '=', '==', '!=', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)', r'\{', r'\}', r'\[', r'\]' ]
    var_operans = ['def', 'return', 'for', 'import', 'from', 'with', 'true', 'false', 'none', 'not', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'range', 'raise', 'class', 'open', 'print', '>', '<', '>=', '<=', '=', '==', '!=', ':', ',', '/', '-', '+', '*', '**', " , ", '"', '(', ')', '{', '}', '[', ']' ]
    
    # slice on each line based on operans
    for each in operans:
        Sliced = []
        for line in file :
            elmt = re.split(r'[A..z]*(' + each + r')[A..z]*', line)
            
            for sliced in elmt:
                if sliced == '': 
                    continue # skip blank
                else :
                    Sliced.append(sliced) 
        file = Sliced
        
    sliced_base = []
    
    var_inspect = True
    for each in file:
        if each in var_operans:
            sliced_base.append(each)
        else:
            if (each == 'as' or each == 'is' or each == 'or' or each == 'in' or each == 'if' or each == 'and'): # avoid redundant
                sliced_base.append(each)
            else:
                if(isVar(each)):
                    split = list(each) # assumed variable
                    sliced_base.extend(split)
                elif (isInt(each)):
                    split = list(each)
                    sliced_base.extend(each)
                else:
                    print("Error... terdapat kesalahan variabel pada: "+each)
                    var_inspect = False
                    break
    return sliced_base, var_inspect
    
    
        
    