#  http://pythonfiddle.com/dfa-simple-implementation/
import re

states_NFA = set()  # All the states of the NFA 
input_datum_NFA = set() # All the possible inputs for the NFA
nfa_trans_fun = dict()
dfa_trans_fun = dict()

def make_dfa_trans_fun(dfa_states):
    for state in dfa_states:
        print("hola")


def make_nfa_trans_fun(reg):
    
    allTrans = re.findall("[^\(|\)|\,]+", reg);
     # allTrans[i*3]  -> The input for the NFA
    # allTrans[i*3+1]  -> The state you start
    # allTrans[i*3+2]  -> The state you move to
    
    for i in range(len(allTrans)//3):
        try: #Check if the input and state already exits
            temp = nfa_trans_fun[allTrans[i*3],allTrans[i*3+1]]
            temp.append(allTrans[i*3+2])
            nfa_trans_fun[allTrans[i*3],allTrans[i*3+1]] = temp
        except:
            nfa_trans_fun[allTrans[i*3],allTrans[i*3+1]] = [allTrans[i*3+2]]

        states_NFA.add(allTrans[i*3+1])
        input_datum_NFA.add(allTrans[i*3])

    
def print_trans_fun(trans_func):
    print("The transition function is: ")
    for keys,values in trans_func.items():
        transition = "   {} -> {}".format(keys, values)
        print(transition)
    print()

def createFile():
    path = "./files/writeFile.txt"
    f = open(path, "w+")
    for i in range(20):
        f.write("this is line %d\r\n" % (i+1))
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