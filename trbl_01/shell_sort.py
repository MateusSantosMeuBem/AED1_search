from util import *
import timeit
def ShellSort(nums):
    #definimos os valores para h, que será o responsavel pela ordenação.
    h = 1
    n = len(nums)
    while h > 0:
        #enquanto h for maior que 0, será feita a continua reorganização da lista
        for i in range(h, n):
            c = nums[i]
            j = i
            while j >= h and c < nums[j - h]:
                nums[j] = nums[j - h]
                j = j - h
                #h será subitraido a -1 até que a lista esta organizada
                nums[j] = c
        h = int(h / 2.2)
    return nums
#função para criar uma lista aleatoria, com os parametros:quantidade de itens na lista;se pode repetir os numeros;de onde começa;de onde termina.
values = [200000]
header = f'|Qtd.|Tempo 1|Tempo 2|Tempo 3|Tempo Medio|\n|--|--|--|--|--|\n'
with open('shell_sort_200k.md','w') as f:
    f.write(header)
    for v in values:
        avg = 0
        line = f'|{v}|'
        for i in range(1):
            print(f'Criando a {i + 1}ª lista de {v} valores')
            num = randomList(v, True, 0, v)
            print(f'Ordenando a {i + 1}ª lista de {v} valores')
            start = timeit.default_timer()
            my_list = ShellSort(num)
            end = timeit.default_timer()
            line += f'{(end - start):.8f}s|'
            avg += float(f'{(end - start):.8f}')
        avg /= 3
        line += f'{avg:.8f}s|\n'

        f.write(line)
#print(num)
