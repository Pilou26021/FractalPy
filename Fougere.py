import matplotlib.pyplot as plt
import numpy as np
from random import*

# nombre d'itérations :
nbpoints=100000

#point de départ :
p=np.zeros((2,1))
 
def transformation1(p):
    f1 = np.array([[0, 0], [0., 0.16]])
    u1 = np.array([[0], [0]])
    return np.dot(f1, p) + u1
    # à compléter
    
     
def transformation2(p):
    f2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
    u2 = np.array([[0], [1.6]])
    return np.dot(f2, p) + u2
    # à compléter
    
def transformation3(p):
    f3 = np.array([[0.2, -0.26], [0.23, 0.22]])
    u3 = np.array([[0], [1.6]])
    return np.dot(f3, p) + u3
    # à compléter

def transformation4(p):
    f4 = np.array([[-0.15, 0.28], [0.26, 0.24]])
    u4 = np.array([[0], [0.44]])
    return np.dot(f4, p) + u4
    # à compléter

def transforme(p):
    # Choix aléatoire (avec équiprobabilité) entre les 2 transformations de fonctions
    tirage=random()
    if tirage <0.01 :
        res = transformation1(p)
    elif tirage <0.86 :
        res = transformation2(p)
    elif tirage <0.93 :
        res = transformation3(p)
    else :
        res = transformation4(p)
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
    plt.title('Fougère de Barnsley')
    plt.show()
    
construction(p,nbpoints)
