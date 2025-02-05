left, right = 0, 1

K, V, Productions = [],[],[]
variablesJar = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "V2", "W2", "X2", "Y2", "Z2",
"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3", "X3", "Y3", "Z3",
"A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4",
"A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5"]

for nonTerminal in V:
	if nonTerminal in variablesJar:
		variablesJar.remove(nonTerminal)

def isUnitary(rule, variables):
	if rule[left] in variables and rule[right][0] in variables and len(rule[right]) == 1:
		return True
	return False

def isSimple(K,V,rule):
    if rule[left] in V and rule[right][0] in K and len(rule[right]) == 1:
	    return True
    return False

def setupDict(productions, variables, terms):
	result = {}
	for production in productions:
		#
		if production[left] in variables and production[right][0] in terms and len(production[right]) == 1:
			result[production[right][0]] = production[left]
	return result

def cleanProduction(expression):
    result = []
	#remove spaces and explode on ";"
    rawRulse = expression.replace('\n','').split(';')
	
    for rule in rawRulse:
		#Explode evry rule on "->" and make a couple
        leftSide = rule.split(' -> ')[0].replace(' ','')
        rightTerms = rule.split(' -> ')[1].split(' | ')
        for term in rightTerms:
	        result.append( (leftSide, term.split(' ')) )
    return result

def cleanAlphabet(expression):
	return expression.replace('  ',' ').split(' ')

def loadModel(modelPath):
	file = open(modelPath).read()
	K = (file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n",""))
	V = (file.split("Variables:\n")[1].split("Productions:\n")[0].replace("Variables:\n","").replace("\n",""))
	P = (file.split("Productions:\n")[1])

	K = K.replace('  ',' ').split(' ')
	V = V.replace('  ',' ').split(' ')
	newP = []
	rawRules = P.replace('\n','').split(';')
	for rule in rawRules:
		lhs = rule.split(' -> ')[0].replace(' ','')
		rhs = rule.split(' -> ')[1].split(' | ')
		for term in rhs:
			newP.append( (lhs, term.split(' ')) )

	return K, V, newP

#Add S0->S rule––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––START
def START(productions, variables):
	variables.append('S0')
	return [('S0', [variables[0]])] + productions
#Remove rules containing both terms and variables, like A->Bc, replacing by A->BZ and Z->c–––––––––––TERM
def TERM(productions, variables,terminals):
	newProductions = []
	#create a dictionari for all base production, like A->a, in the form dic['a'] = 'A'
	dictionary = setupDict(productions, variables, terms=K)
	for production in productions:
		#check if the production is simple
		if isSimple(terminals,variables,production):
			#in that case there is nothing to change
			newProductions.append(production)
		else:
			for term in terminals:
				for index, value in enumerate(production[right]):
					if term == value and not term in dictionary:
						#it's created a new production vaiable->term and added to it 
						dictionary[term] = variablesJar.pop()
						#Variables set it's updated adding new variable
						variables.append(dictionary[term])
						newProductions.append( (dictionary[term], [term]) )
						
						production[right][index] = dictionary[term]
					elif term == value:
						production[right][index] = dictionary[term]
			newProductions.append( (production[left], production[right]) )
			
	#merge created set and the introduced rules
	return newProductions

#Eliminate non unitry rules––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––BIN
def BIN(productions, variables):
	result = []
	for production in productions:
		k = len(production[right])
		#newVar = production[left]
		if k <= 2:
			result.append( production )
		else:
			newVar = variablesJar.pop(0)
			variables.append(newVar+'1')
			result.append( (production[left], [production[right][0]]+[newVar+'1']) )
			i = 1
#TODO
			for i in range(1, k-2 ):
				var, var2 = newVar+str(i), newVar+str(i+1)
				variables.append(var2)
				result.append( (var, [production[right][i], var2]) )
			result.append( (newVar+str(k-2), production[right][k-2:k]) ) 
	return result
	

#Delete non terminal rules–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––DEL
# def DEL(productions):
# 	newSet = []
# 	#seekAndDestroy throw back in:
# 	#        – outlaws all left side of productions such that right side is equal to the outlaw
# 	#        – productions the productions without outlaws 
# 	outlaws, productions = helper.seekAndDestroy(target='e', productions=productions)
# 	#add new reformulation of old rules
# 	for outlaw in outlaws:
# 		#consider every production: old + new resulting important when more than one outlaws are in the same prod.
# 		for production in productions + [e for e in newSet if e not in productions]:
# 			#if outlaw is present in the right side of a rule
# 			if outlaw in production[right]:
# 				#the rule is rewrited in all combination of it, rewriting "e" rather than outlaw
# 				#this cycle prevent to insert duplicate rules
# 				newSet = newSet + [e for e in  helper.rewrite(outlaw, production) if e not in newSet]

# 	#add unchanged rules and return
# 	return newSet + ([productions[i] for i in range(len(productions)) 
# 							if productions[i] not in newSet])

def unit_routine(rules, variables):
	unitaries, result = [], []
	#controllo se una regola è unaria
	for aRule in rules:
		if isUnitary(aRule, variables):
			unitaries.append( (aRule[left], aRule[right][0]) )
		else:
			result.append(aRule)
	#altrimenti controllo se posso sostituirla in tutte le altre
	for uni in unitaries:
		for rule in rules:
			if uni[right]==rule[left] and uni[left]!=rule[left]:
				result.append( (uni[left],rule[right]) )
	
	return result

def UNIT(productions, variables):
	i = 0
	result = unit_routine(productions, variables)
	tmp = unit_routine(result, variables)
	while result != tmp and i < 1000:
		result = unit_routine(tmp, variables)
		tmp = unit_routine(result, variables)
		i+=1
	return result


def convert(modelPath):
	K, V, Productions = loadModel( modelPath )

	Productions = START(Productions, variables=V)
	Productions = TERM(Productions, variables=V, terminals=K)
	Productions = BIN(Productions, variables=V)
	# Productions = DEL(Productions)
	Productions = UNIT(Productions, variables=V)
	
def initDictionary(modelPath):
    
	def convert(modelPath):
		K, V, Productions = loadModel( modelPath )

		Productions = START(Productions, variables=V)
		Productions = TERM(Productions, variables=V, terminals=K)
		Productions = BIN(Productions, variables=V)
		# Productions = DEL(Productions)
		Productions = UNIT(Productions, variables=V)
		return Productions

	productions = convert(modelPath)

	dictionary = {}
	for production in productions :
	    if(production[left] in dictionary.keys()):
		    dictionary[production[left]].append(production[right])
	    else :
		    dictionary[production[left]] = []
		    dictionary[production[left]].append(production[right])
	return dictionary

#print(initDictionary(modelPath))

#print(START(productions. variables))
#print("******************************************")