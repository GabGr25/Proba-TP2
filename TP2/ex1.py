import random 
import matplotlib.pyplot as plt


def tirage_de():
    tmp=random.randint(1,6)
    return tmp

#print(tirage_de())    

def moyenne(N):
    assert N >0
    tmp=0
    for nb_tirage in range(N):
        tmp+=tirage_de()
    tmp/=N
    return tmp #pour mettre en int: int(tmp)   

#print(moyenne(7))

def frequence(N):
    assert N>0
    tableau=[]
    rep=[]
    for i in range(N):
        tableau.append(tirage_de())
    for y in range(1,7):
        rep.append(tableau.count(y)/N)
    return rep

def affichageBaton(fonction):
    x=[1,2,3,4,5,6]
    height=fonction(1000)
    plt.stem(x,height)
    plt.show()

affichageBaton(frequence)
#OUI