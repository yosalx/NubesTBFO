from basedSlice import basedSlice
import cfg2cnf
import sys

def cyk(w,grammar):
    n = len(w)

	#init table
    tab = [[set([]) for j in range(n)] for i in range(n)]

	#isi table
    for j in range(0, n):
        for rule in grammar.items():
                for terminal in rule[1]:
                    if len(terminal) == 1 and terminal[0] == w[j]: #ketemu terminal
                        tab[j][j].add(rule[0])

    for k in range(2, n+1):
        for j in range (0, n-k+1):
            i = j+k-1
            for l in range (j,i):
                for rule in grammar.items():
                    for terminal in rule[1] :
                        if len(terminal) == 2 :
                            if(terminal[0] in tab[j][l]) and (terminal[1] in tab[l+1][i]): #ketemu terminal
                                tab[j][i].add(rule[0])
    if "S0" in tab[0][n-1] :
        print("Accepted")
    else :
        print("Syntax Error")
        
if len(sys.argv) > 1:
    	modelPath = str(sys.argv[1])
else:
	modelPath = 'grammar.txt'
        
print("start compile...")
print("\n")

cnf = cfg2cnf.initDictionary(modelPath)

sliced,var_inspect = basedSlice('input.txt')

if var_inspect == True :
	cyk(sliced,cnf)