from random import randint

def randomList(qtt = 0, repeat = False, start = 0, end = 0):
    numbers = []
    while len(numbers) < qtd:
        number = randint(start, end)
        if not repeat:
            if number not in numbers:
                numbers.append(number)
        else:
                numbers.append(number)
    return numbers