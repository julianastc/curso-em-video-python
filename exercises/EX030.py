import math
number = int(input('Digite um número: '))
even = number % 2 == 0

if even:
    print(f'O número \033[36m{number}\033[m é \033[30;46mpar\033[m!')
else: 
    print(f'O número \033[33m{number}\033[m é \033[97;43mímpar\033[m! ')