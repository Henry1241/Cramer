import numpy as np
from fractions import Fraction

def cramer(A,b):
    n = len(b)      #Longitud del vector b
    D = np.linalg.det(A)    #Determinante de A
    x = np.zeros(n) #Crea un nuevo array que puede ser usado para las determinantes de x, y & z

    for k in range(n): #Se encarga de realizar operaciones dentro del rango "n" en este caso la longitud de b que es 3
        Ak = A.copy()   #Copia la determinante de A para reemplazar su valor anterior
        Ak[:,k] = b     #Reemplaza la columna k por el vector b
        Dk = np.linalg.det(Ak) #Encuentra la variable de x, y o z
        x[k] = Dk/D #Obtiene el resultado de la variable de x, y o z dividida sobre la Determinante
        print('x', k + 1, '=', ((Fraction(x[k])))) #El for imprime cada resultado de k+1 que termina con el resultado de cada determinante

x1 = print('Valores para x: ',input())
x2 = input()
x3 = input()
y1 = input()
y2 = input()
y3 = input()
z1 = input()
z2 = input()
z3 = input()
X = input()
Y = input()
Z = input()

A = np.array([[x1,x2,x3], 
              [y1,y2,y3], 
              [z1,z2,z3]])
b = np.array([X,Y,Z])
cramer(A,b)