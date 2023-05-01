import random

numbers = [i for i in range(1,46)]



def select_num(T):
    for i in range(T):
        print(*random.sample(numbers, 6))

if __name__ == '__main__':
    select_num(int(input()))
