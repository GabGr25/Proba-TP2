import random 
import matplotlib.pyplot as plt


def organisation_sondages(nbSondage, nbPersonne) :
    proba_o : 0.49
    nbRepTotal = {}
    for i in range(nbSondage+1) : 
        total_o = 0
        for j in range(nbPersonne) :
            reponse = random.randint(1,100)
            if reponse <= 49 :
                total_o += 1
        nbRepTotal[i] = total_o / nbPersonne
    return nbRepTotal

print(organisation_sondages(500,1000))

def diagramme_boite():
    fig = plt.figure()
    data = []
    sondage = [organisation_sondages(500, 1000), organisation_sondages(500, 5000)]
    for i in range(2):
        data.append([])
        for j in range(len(sondage[i])):
            data[i].append(sondage[i][j])
    plt.boxplot(data)
    plt.savefig('DiagrammeBoite.png')
    plt.show()

diagramme_boite()

#Oui