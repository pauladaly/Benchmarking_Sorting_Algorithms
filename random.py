from random import randint

def random_array(n):
    array = []
    for i in range(0,n, 1):
        array.append(randint(0,100))
    return array


print(random_array(5))