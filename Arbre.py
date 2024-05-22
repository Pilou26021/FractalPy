import matplotlib.pyplot as plt
import numpy as np
from random import*

# nombre d'itérations :
nbpoints=1000000

# Paramètres de la fractale en forme d'arbre
c = 0.255
r = 0.75
q = 0.625
theta1 = -np.pi / 8
theta2 = np.pi / 5

#constantes :
c = 0.255
r = 0.75
q = 0.625
pi = 3.141592
angle1 = -pi/8
angle2 = pi/5

#point de départ :
p=np.zeros((2,1))
 
def transformation1(p, c):
    T1 = np.array([[0, 0],
                   [0, c]])
    u1 = np.array([[0.5],
                   [0]])
    return np.dot(T1, p) + u1

def transformation2(p, c, r, theta1):
    T2 = np.array([[r * np.cos(theta1), -r * np.sin(theta1)],
                   [r * np.sin(theta1), r * np.cos(theta1)]])
    u2 = np.array([[0.5 - 0.5 * r * np.cos(theta1)],
                   [c - 0.5 * r * np.sin(theta1)]])
    return np.dot(T2, p) + u2

def transformation3(p, c, q, theta2):
    T3 = np.array([[q * np.cos(theta2), -r * np.sin(theta2)],
                   [q * np.sin(theta2), r * np.cos(theta2)]])
    u3 = np.array([[0.5 - 0.5 * q * np.cos(theta2)],
                   [0.6 * c - 0.5 * q * np.sin(theta2)]])
    return np.dot(T3, p) + u3

# Fonction pour choisir entre les transformations de l'arbre
def transforme(p, c, r, q, theta1, theta2):
    tirage = random()
    if tirage < 1/3:
        return transformation1(p, c)
    elif tirage < 2/3:
        return transformation2(p, c, r, theta1)
    else:
        return transformation3(p, c, q, theta2)

def construction(p, nbpoints):
    x = [p[0,0]]
    y = [p[1,0]]
    for i in range(nbpoints):
        p = transforme(p, c, r, q, theta1, theta2)
        x.append(p[0,0])
        y.append(p[1,0])
    
# Représentation graphique
    plt.plot(x, y, 'o', markersize=0.2, color='orange')
    plt.title('Arbre')
    plt.show()
    
construction(p,nbpoints)

