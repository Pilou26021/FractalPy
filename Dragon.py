import matplotlib.pyplot as plt
import numpy as np
from random import*

# nombre d'itérations :
nbpoints=100000

#point de départ :
p=np.zeros((2,1))
 
def transformation1(p):
    f1 = np.array([[0.5, -0.5], [0.5, 0.5]])
    u1 = np.array([[0], [0]])
    return np.dot(f1, p) + u1
    # à compléter
    
     
def transformation2(p):
    f2 = np.array([[-0.5, -0.5], [0.5, -0.5]])
    u2 = np.array([[1], [0]])
    return np.dot(f2, p) + u2
    # à compléter
    

def transforme(p):
    # Choix aléatoire (avec équiprobabilité) entre les 2 transformations de fonctions
    tirage=random()
    if tirage <1/2 :
        res = transformation1(p)
    else :
        res = transformation2(p)
    return res

def construction(p, nbpoints):
    x = [p[0,0]]
    y = [p[1,0]]
    for i in range(nbpoints):
        p = transforme(p)
        x.append(p[0,0])
        y.append(p[1,0])
    
# Représentation graphique
    plt.plot(x, y, 'o', markersize=0.2, color='orange')
    plt.title('Dragon de Heighway')
    plt.show()
    
construction(p,nbpoints)
