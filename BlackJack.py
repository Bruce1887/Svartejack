from random import randint

def valör():
    a = ["Hjärter","Ruter","Spader","Klöver"]
    return(a)

def värde(m):
    a = []
    for n in range(13):
        a.append(str(n+1))
    return(a[m])

def kort():
    a = []
    for n in range(4):
        for m in range(13):
            a.append(valör()[n] + " " + värde(m))
    return(a)

def specialkort(m):
    if(m == 11):
        return("Knekt")
    elif(m == 12):
        return("Dam")
    elif(m == 13):
        return("Kung")
    elif(m == 1):
        return("Ess")
    else:
        return(str(m))
    
def bvärde(m):
    if(m >= 10):
        return(10)
    else:
        return(m)

def spelargiv():
    a = randint(0,52)
    x = kortlek[a]
    kortlek.remove(kortlek[a])
    b = randint(0,51)
    y = kortlek[b]
    kortlek.remove(kortlek[b])
    return(x,y)

def dealergiv():
    a = randint(0,50)
    x = kortlek[a]
    kortlek.remove(kortlek[a])
    b = randint(0,49)
    y = kortlek[b]
    kortlek.remove(kortlek[b])
    return(x,y)

'''
def spelarhand(x,y):
    if(x == 1):
    
    elif(x == 11):
    
    elif(x == 12):
    
    elif(x == 13):

'''


kortlek = kort()
dh = dealergiv()

print(f"Din hand: {spelargiv()}")
print(f"Dealerns hand: {dh[0]}, DOLT KORT")



