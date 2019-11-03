# NFA_to_DFA

This project converts a NFA to its correct DFA

## Instructions

In order to run the program correctly it is neccessary a txt file which store the transition function of an NFA. This file must be inside the `files` folder.
<br> The format the txt file must have is the following: 

        {(0,p,p),(0,p,q),(1,p,p),(0,q,r),(1,q,r),(0,r,s),(0,s,s),(1,s,s)}

This represent a transition function which has three elements. The input, the actual state and the final state respectively. It must be done for every single element of the NFA. 

- New txt file

If you want to test a different NFA from a different file it has to be as said, in the `files` folder and insert the new file name ino the path in the `readFile` method. Here is how: 

    def readFile():
        path = "./files/<<filename>>.txt"
        f = open(path, "r")
        if f.mode == "r":
        contents = f.read()
        x = re.findall("(\(.+\))", contents)[0];
        return x