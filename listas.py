import random as r

lista = ["Angelo", "Antonio", "Jorge"]
copiaLista = lista.copy()

lista.pop()

print(lista)
print(copiaLista)

elemento = lista[r.randint(0, (len(lista)))]

#lista.copy
