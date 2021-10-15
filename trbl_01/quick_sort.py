import timeit
from util import *

def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p-1)
        # recursivamente na sublista à direita (maiores)
        quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

values = [12]
header = f'|Qtd.|Tempo 1|Tempo 2|Tempo 3|Tempo medio|\n|--|--|--|--|--|\n'
with open("test.md", "w") as f:
    f.write(header) 
    for v in values:
        avg = 0
        line = f'|{v}|'
        for i in range(3):
            print(f'Criando a {i+1}ª lista de {v} valores...')
            a = randomList(v, True, 0, v)
            print(f'Ordenando a {i+1}ª lista de {v} valores...')
            print(a)
            start = timeit.default_timer()
            quicksort(a)
            end = timeit.default_timer()
            print(a)
            line += f'{(end - start):.8f}s|'
            avg += float(f'{(end - start):.8f}')
        avg /= 3
        line += f'{avg:.8f}s|\n'

        f.write(line) 