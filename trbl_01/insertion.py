from util import *
import timeit

def insert_sort(lista):
    contador = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        contador += 1

        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
            contador += 1

        lista[j + 1] = chave

    print('Número de comparações:', contador, '\n')
    return lista


valores = [100, 1000, 100000, 1000000]
cabecalho = f'|Qtd.|Tempo 1|Tempo 2|Tempo 3|Tempo Medio|\n|--|--|--|--|--|\n'
with open('insertion.md', 'w') as arquivo:
    arquivo.write(cabecalho)
    for valor in valores:
        media_tempo = 0
        linha = f'|{valor}|'
        for i in range(3):
            print('criando lista {} do valor {}'.format(i+1, valor))
            lista = randomList(valor, True, 0, valor)
            print('ordenando lista {} do valor {}'.format(i+1, valor))
            inicio = timeit.default_timer()
            lista_ordenada = insert_sort(lista)
            fim = timeit.default_timer()
            linha += f'{(fim - inicio):.8f}s|'
            media_tempo += float(f'{(fim - inicio):.8f}')

        media_tempo /= 3
        linha += f'{media_tempo:.8f}s|\n'

        arquivo.write(linha)


