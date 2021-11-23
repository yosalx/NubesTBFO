import re

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
        temp = Sliced
        
    sliced_base = []
    
    for each in temp:
        if each in operans:
            sliced_base.append(each)
        else:
            if (each == 'as' or 'is' or 'or' or  'in' or  'if' or 'and'): # avoid redundant
                sliced_base.append(each)
            else:
                split = list(each) # assumed variable
                sliced_base.extend(split)
            
    return sliced_base
    
    
        
    