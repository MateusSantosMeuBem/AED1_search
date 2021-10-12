def bublleSort(vet):
    aux = 0
    interactions = 0
    for b in range(len(vet)):
        for a in range(len(vet)):
            if a + 1 != len(vet):
                if vet[a] > vet[a + 1]:
                    interactions += 1
                    aux = vet[a]
                    vet[a] = vet[a + 1]
                    vet[a + 1] = aux
        print(interactions)
        interactions = 0
    return vet

# my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
my_list = [int(i) for i in range(10)]

print(bublleSort(my_list))