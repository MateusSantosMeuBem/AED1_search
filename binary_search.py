def binarySearch(A, item):

    left, right = 0, len(A) - 1
    counter = 0
    while left <= right:
        center = (left + right) // 2
        counter += 1
        if A[center] == item:
            return center, counter
        if A[center] > item:
            right = center - 1
        counter += 1
        if A[center] > item:
            left = center + 1
            
    return -1, counter

A = [int(i) for i in range(10000)]
# A = [7 , 10 , 15 , 27, 32 ,48 , 54 , 63 , 77]
print(A)

print(f'Pesquisa com sucesso: {binarySearch(A, 54)}')
print(f'Pesquisa com sucesso: {binarySearch(A, 20)}')
print(f'Pesquisa com sucesso: {binarySearch(A, 70)}')
print(f'Pesquisa com sucesso: {binarySearch(A, 100)}')