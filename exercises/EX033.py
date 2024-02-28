payment = float(input('Qual é o seu salário atual? '))

payment_base = 1251.00
payment_increase_for_bigger_than_base = payment + (payment * (10/100))
payment_increase_for_smaller_than_base = payment + (payment * (15/100))

if payment >= payment_base:
    print(f"O aumento será de 10%, ou seja \033[34m{payment_increase_for_bigger_than_base:.2f}")
else:
    print(f'O aumento será de 15%, ou seja, \033[35m{payment_increase_for_smaller_than_base:.2f}')

