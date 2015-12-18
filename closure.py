# Program to find the closure of a set of attributes
# Author : Meenal Jain

#function that calculates the closure of an attribute
def closure():              
    att = []
    att = input("Attribute to find closure with space:\n")
    att = set(att.split())
    for i in range(fdn):
        if (set(fdl[i]) <= att):
            att = att | set(fdr[i])
        for i in range(fdn):
            if (set(fdl[i]) <= att):
                att = att | set(fdr[i])
    print("Closure of given Attribute is:  ")
    print(att)
    
#programs starts from here
    
attNo = int(input("Enter number of attributes of schema:\n"))   
print ("Enter attributes of schema\n")
schema = []
for i in range(attNo):
    s = input()
    schema.append(s)
fdn = int(input("Enter Number of FD's:\n"))
fdl = []
fdr = []
x='yes'
for i in range(fdn):
    l = input("Enter left FD's with space\n")
    l = l.split()
    fdl.append(l)
    r = input("Enter right FD's with space\n")
    r = r.split()
    fdr.append(r)
while x in ('yes','y'):
    x = 'no'
    closure()         # calling function closure
    print("Do you want to find another closure of Attributes: 'yes' or 'no'\n")
    x = input()
    

    
