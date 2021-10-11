def binarySearch(A, item):

    left, right = 0, len(A) - 1
    counter = 0
    while left <= right:
        counter += 1
        center = (left + right) // 2
        if A[center] == item:
            return center, counter
        elif A[center] > item:
            right = center - 1
        else:
            left = center + 1
    return -1, counter

A = [int(i) for i in range(10000)]
print(A)

print(f'Pesquisa com sucesso: {binarySearch(A, 0)}')
print(f'Pesquisa com sucesso: {binarySearch(A, 20)}')
print(f'Pesquisa com sucesso: {binarySearch(A, 70)}')
print(f'Pesquisa com sucesso: {binarySearch(A, 100)}')