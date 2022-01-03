import random 
import matplotlib.pyplot as plt
import numpy as np

def AjoutBitParite(LeMessage):
    tmp=0
    for i in LeMessage:
        if(i=="1"):
            tmp+=1
    if(tmp%2==0):
        return LeMessage+"0"
    else:
        return LeMessage+"1"

#print(AjoutBitParite("0100001"))


def SimulTransmission(vecteur,p):
    resultat = ""
    for i in range(len(vecteur)):
        alea=np.random.choice(np.arange(0,2), p=[p,1-p])
        if alea==0:
            if vecteur[i]=="1":
                resultat+="0"
            else:
                resultat+="1"
        else:
            resultat+=vecteur[i]
    return resultat


def Controle():