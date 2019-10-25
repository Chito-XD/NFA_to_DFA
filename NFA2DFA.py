#  http://pythonfiddle.com/dfa-simple-implementation/
import re
from itertools import chain

states_NFA = set()  # All the states of the NFA 
input_datum_NFA = set() # All the possible inputs for the NFA
nfa_trans_fun = dict()
dfa_trans_fun = dict()
conjunto_potencia = []

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
        print('the subset is')
        print(subset)
        for datum in input_datum_NFA:
            print('the datum is:')
            print(datum)
            values = set()
            for element in subset:
                print('the element is:')
                print(element)
                tempValues = getValue(datum, element)
                if tempValues != None:
                    values = set(chain(values, tempValues))
            print('the values are')
            print(values)
            if len(values) == 0:
                dfa_trans_fun[datum, key1] = { }
            else:
                key1 = ""
                key1 = ', '.join([str(el) for el in subset])
                dfa_trans_fun[datum, key1] = values
    

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
    print("The transition function is: ")
    for keys,values in trans_func.items():
        transition = "   {} -> {}".format(keys, list(values))
        print(transition)
    print()

def createFile():
    global dfa_trans_fun
    path = "./files/writeFile.txt"
    f = open(path, "w+")
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
    
contentFile = readFile()
make_nfa_trans_fun(contentFile)
print_trans_fun(nfa_trans_fun)
print(states_NFA)
print(input_datum_NFA)
nfa2dfa(states_NFA)
print(conjunto_potencia)
print("el conjunto potencia es de longitud {}".format(len(conjunto_potencia)))

print('----')
print('bien lo bueno')

make_dfa_trans_fun()
print('la funcion del dfa esssssssssssssssssssssssssssssssssssssss:')
print_trans_fun(dfa_trans_fun)
createFile()