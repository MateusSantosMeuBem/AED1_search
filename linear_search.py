def procura(lista, elemento):
    assert isinstance(lista, list)
    for indice in range(len(lista)):
        if lista[indice] == elemento:
            return indice
    else:
        return None

my_list = [1,2,3,6,4]

print(my_list[procura(my_list, 6)])