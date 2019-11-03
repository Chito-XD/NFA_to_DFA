import re
from itertools import chain

states_NFA = set()  # All the states of the NFA 
states_DFA = set() # All the states of the DFA
input_datum_NFA = set() # All the possible inputs for the NFA
nfa_trans_fun = dict()
dfa_trans_fun = dict()
conjunto_potencia = []
accept_states = []
q0 = []

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
    
def nfa2dfa(nfakeys): # Method to make the set of subsets for the DFA
    
    global conjunto_potencia

    n = len(nfakeys)

    for i in range(n):
        val = nfakeys[i]
        conjunto_potencia.append([val])

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
    
    conjunto_potencia = sorted(conjunto_potencia, key = sortConjunto)

def sortConjunto(x):
    return len(x)

def getValue(datum, element):
    global nfa_trans_fun
    global dfa_trans_fun

    try:
        # The value is not null in the NFA
        temp = nfa_trans_fun[datum, element]
        value = set(temp)
    except:
        # the value is null in NFA
        value = None
    
    return value


def make_dfa_trans_fun():
    global conjunto_potencia
    global input_datum_NFA
    global nfa_trans_fun
    global dfa_trans_fun
    
    # First, the empty string
    for datum in input_datum_NFA:
        dfa_trans_fun[datum, ''] = { }


    for subset in conjunto_potencia:
        for datum in input_datum_NFA:
            values = set()
            for element in subset:
                tempValues = getValue(datum, element)
                if tempValues != None:
                    values = set(chain(values, tempValues))
            if len(values) == 0:
                dfa_trans_fun[datum, key1] = { }
            else:
                key1 = ""
                key1 = ', '.join([str(el) for el in subset])
                dfa_trans_fun[datum, key1] = values
            states_DFA.add(key1)
    

def make_nfa_trans_fun(reg):
    
    allTrans = re.findall("[^\(|\)|\,]+", reg);
     # allTrans[i*3]  -> The input for the NFA
    # allTrans[i*3+1]  -> The state you start
    # allTrans[i*3+2]  -> The state you move to

    global states_NFA
    global input_datum_NFA
    
    for i in range(len(allTrans)//3):
        try: #Check if the input and state already exits
            temp = nfa_trans_fun[allTrans[i*3],allTrans[i*3+1]]
            temp.append(allTrans[i*3+2])
            nfa_trans_fun[allTrans[i*3],allTrans[i*3+1]] = temp
        except:
            nfa_trans_fun[allTrans[i*3],allTrans[i*3+1]] = [allTrans[i*3+2]]

        states_NFA.add(allTrans[i*3+1])
        input_datum_NFA.add(allTrans[i*3])
    
    states_NFA = sorted(list(states_NFA))
    input_datum_NFA = sorted(list(input_datum_NFA))

    
def print_trans_fun(trans_func):
    for keys,values in trans_func.items():
        transition = "   {} -> {}".format(keys, list(values))
        print(transition)
    print()

def createFile():
    global dfa_trans_fun
    global accept_states

    path = "./files/writeFile.txt"
    f = open(path, "w+")
    states = "{}".format((conjunto_potencia))
    f.write("The states for the DFA are:\n");
    f.write("%s\n\n" %(states));

    f.write("The alphabet is: ");
    alfa = "{}".format(input_datum_NFA);
    f.write("%s\n\n" %(alfa));
    
    f.write("The accepted states are: ");
    ac_st = "{}".format(accept_states);
    f.write("%s\n\n" %(ac_st));

    f.write("The initial state is: ");
    q = "{}".format(q0);
    f.write("%s\n\n" %(q));

    f.write("The transition function is: \n");
    for keys,values in dfa_trans_fun.items():
        transition = "{} -> {}".format(keys, list(values))
        f.write("%s\n" % (transition))
    f.close()


def readFile():
    path = "./files/test_file.txt"
    f = open(path, "r")
    if f.mode == "r":
        contents = f.read()
    x = re.findall("(\(.+\))", contents)[0];
    return x


def findAcceptStates(accept):
    global conjunto_potencia

    global accept_states

    for subset in conjunto_potencia:
        if accept in subset:
            accept_states.append(subset)


    

# MAIN METHOD #
inicial = input("¿Cual es el estado inicial? \n")
q0.append(inicial)

accept_state = input("¿Cual es el estado de aceptacion? \n")

contentFile = readFile()

make_nfa_trans_fun(contentFile)

nfa2dfa(states_NFA)

make_dfa_trans_fun()

findAcceptStates(accept_state)

createFile()

