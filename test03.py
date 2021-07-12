def min(a,b):
    if(a>b):
        return b
    else:
        return a

c = min(10,20)
print("{0}".format(c))

def printS(c):
    print(c)

printS("Hello")

def divide(a,b):
    return(a/b,a%b)


d,v=divide(12,3)
print(d,v)
print(type(d))