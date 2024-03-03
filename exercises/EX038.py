
first_number = int(input('Digite um número inteiro: '))
second_number = int(input('Digite outro número inteiro: '))

if first_number > second_number:
    print('O primeiro valor é maior! ')
elif second_number > first_number:
    print('O segundo valor é maior!')
elif second_number == first_number:
    print('Não existe valor maior, os dois valores são iguais!')
    