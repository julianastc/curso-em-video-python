import math
number = int(input('Digite um número: '))
even = number % 2 == 0

if even:
    print(f'O número {number} é par!')
else: 
    print(f'O número {number} é ímpar! ')