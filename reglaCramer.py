import numpy as np
from fractions import Fraction

def cramer(x1,x2,x3,y1,y2,y3,z1,z2,z3,X,Y,Z):

    # x1 = int(input('Valores para x1: '))
    # x2 = int(input('Valores para x2: '))
    # x3 = int(input('Valores para x3: '))
    # y1 = int(input('Valores para y1: '))
    # y2 = int(input('Valores para y2: '))
    # y3 = int(input('Valores para y3: '))
    # z1 = int(input('Valores para z1: '))
    # z2 = int(input('Valores para z2: '))
    # z3 = int(input('Valores para z3: '))
    # X = int(input('Valores para X: '))
    # Y = int(input('Valores para Y: '))
    # Z = int(input('Valores para Z: '))

    A = np.array([[x1,x2,x3], 
              [y1,y2,y3], 
              [z1,z2,z3]])
    b = np.array([X,Y,Z])

    n = len(b)      #Longitud del vector b
    D = np.linalg.det(A)    #Determinante de A
    x = np.zeros(n) #Crea un nuevo array que puede ser usado para las determinantes de x, y & z
    resultados = []
    for k in range(n): #Se encarga de realizar operaciones dentro del rango "n" en este caso la longitud de b que es 3
        Ak = A.copy()   #Copia la determinante de A para reemplazar su valor anterior
        Ak[:,k] = b     #Reemplaza la columna k por el vector b
        Dk = np.linalg.det(Ak) #Encuentra la variable de x, y o z
        x[k] = Dk/D #Obtiene el resultado de la variable de x, y o z dividida sobre la Determinante
        resultados+=[('x' + str(k + 1)+ "="+str((Fraction(x[k]))))]#El for imprime cada resultado de k+1 que termina con el resultado de cada determinante
        print('x' + str(k + 1),"=", str(((Fraction(x[k]))))) #El for imprime cada resultado de k+1 que termina con el resultado de cada determinante
    return resultados