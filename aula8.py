lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'tigre', 'arara', 'raposa' ]
print (lista)
print (lista_animal)
print (lista_animal[1])
soma = 0
for x in lista:
    print (x)
    soma += x
print (soma)
print (sum(lista))
print (max(lista))
print (min(lista))
print (min(lista_animal))
nova_lista = lista_animal * 3
print (nova_lista)

if 'lobo' in lista_animal:
    print ('existe um lobo na lista')
else:
    print ('não existe um lobo na lista, ele será incluído')
    lista_animal.append('lobo')
    print (lista_animal)
lista_animal.pop()
print(lista_animal)
lista_animal.pop(1)
print(lista_animal)
lista_animal.remove ('elefante')
print(lista_animal)
lista.sort()
lista_animal.sort()
print(lista)
print (lista_animal)
lista_animal.reverse()
print (lista_animal)