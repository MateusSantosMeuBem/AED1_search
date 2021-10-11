def recursivBinarySearch(A, left, right, item):

    if right < left:
        return -1
    
    center = (left + right) // 2

    if A[center] == item:
        return center
    elif A[center] > item:
        return recursivBinarySearch(A, left, center - 1, item)
    else:
        return recursivBinarySearch(A, center + 1, right, item)

A =  [0, 10, 20, 30, 40, 50, 60, 70]

print(f'Pesquisa com sucessor: {recursivBinarySearch(A, 0, len(A) - 1, 20)}')
print(f'Pesquisa com sucessor: {recursivBinarySearch(A, 0, len(A) - 1, 0)}')
print(f'Pesquisa com sucessor: {recursivBinarySearch(A, 0, len(A) - 1, 70)}')
print(f'Pesquisa com sucessor: {recursivBinarySearch(A, 0, len(A) - 1, 100)}')