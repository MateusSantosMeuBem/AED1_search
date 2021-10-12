from util import *
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

num = randomList(10000000,False,0,10000000)
#função para criar uma lista aleatoria, com os parametros:quantidade de itens na lista;se pode repetir os numeros;de onde começa;de onde termina.
ShellSort(num)
print(num)
