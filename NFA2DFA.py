def isContained(cp, newVal):
    n = len(cp)
    k = len(newVal)

    for i in range(1, k):
        if newVal[i] == newVal[i-1]:
            return True

    for i in range(n):
        if newVal == cp[i]:
            return True

    return False
    

def nfa2dfa(nfa):
    n =  len(nfa.keys())
    print(n)
    k = 2**n -1

    alphabet = []
    nfakeys = list(nfa)
    print(nfakeys)
    for i in range(n):
        val = nfakeys[i]
        alphabet.append([val])

    alphabet = sorted(alphabet)
    print(alphabet)
    conjunto_potencia = alphabet
    i = 0
    while i < len(conjunto_potencia):
        j = 0 
        while j < len(conjunto_potencia):
            newVal = sorted(conjunto_potencia[i] + conjunto_potencia[j]) 
            if not isContained(conjunto_potencia, newVal):  
                conjunto_potencia.append(newVal)
                j = 0
                i = 0
            j += 1
        i += 1
    print(conjunto_potencia)


nfa = {"q0" : {"0" : {"q0", "q1"}, "1": {"q0"} }, "q1" : { "0" : {}, "1" : {"q2"}}, "q2" : {"0" : {}, "1": {}}}
print(nfa)
nfa2dfa(nfa)