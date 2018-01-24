# encoding=utf8
import sys
import fileinput

produccionesB = {}


# Se aplana una lista de listas
def flatten(arr):
    return [item for sublist in arr for item in sublist]


# algoritmo cyk
def CYK(cadena, simbolo_inicial):
    tabla = [[] for i in range(len(cadena))]

    k = 0

    for i in range(len(cadena) - 1, -1, -1):
        tablaTemporal = []

        for j in range(len(cadena) - k):

            if cadena[j] not in produccionesB:
                return False

            if i == len(cadena) - 1:
                tablaTemporal.append(produccionesB[cadena[j]])
            else:
                productions = []
                z = k
                m = 1
                while (z >= 1):
                    for elem in tabla[i + k][j]:
                        prod = ""

                        for elem2 in tabla[i + m][j + m]:
                            prod = elem + elem2

                            if (prod in produccionesB):
                                if (prod not in productions):
                                    productions.append(produccionesB[prod])

                    m += 1
                    z -= 1
                tablaTemporal.append(flatten(productions))

        k += 1
        tabla[i] = tablaTemporal

    return simbolo_inicial in tabla[0][0]


# leer stdin
# texto = sys.stdin.read().split('\n')
texto = []
for line in "aaaaa":
    texto.append(line)

j = 0
for i, v in enumerate(texto):
    if ' ' not in v:
        j = i
        break

for prod in texto[:j]:
    arr = prod.split(" ")  # lo hace para separar las producciones

    for element in arr[1:]:
        if element not in produccionesB:
            produccionesB[element] = []

        produccionesB[element].append(arr[0])
# determina si es aceptada o no
for t in texto[j:-1]:
    if CYK(t, texto[0][0]):
        print('Accepted')
    else:
        print('Rejected')