import timeit
from util import *

def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):
    # para uma versão com partição aleatória
    # descomente as próximas três linhas:
    # from random import randrange
    # rand = randrange(ini, fim)
    # a[rand], a[fim - 1] = a[fim - 1], a[rand]
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] > pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
    return ini - 1

values = [100, 1000, 100000, 1000000]
header = f'|Qtd.|Tempo 1|Tempo 2|Tempo 3|Tempo medio|\n|--|--|--|--|--|\n'
with open("quick_sort.md", "w") as f:
    f.write(header) 
    for v in values:
        avg = 0
        line = f'|{v}|'
        for i in range(3):
            print(f'Criando a {i+1}ª lista de {v} valores...')
            a = randomList(v, True, 0, v)
            print(f'Ordenando a {i+1}ª lista de {v} valores...')
            start = timeit.default_timer()
            list_sorted = quick_sort(a)
            end = timeit.default_timer()
            line += f'{(end - start):.8f}s|'
            avg += float(f'{(end - start):.8f}')
        avg /= 3
        line += f'{avg:.8f}s|\n'

        f.write(line) 