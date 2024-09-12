import random

def random_array(arr):
    for i in range(len(arr)):
        shuffled_num = random.randint(1,100)
        arr[i] = shuffled_num
    return arr
