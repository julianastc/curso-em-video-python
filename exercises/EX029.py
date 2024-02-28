import math

speed = int(input('Qual é a velocidade do carro? '))
speed_trafficticket = (speed - 80) * 7.00

if speed>=80: 
    print(f'\033[31mVocê foi multado em {speed_trafficticket:.2f}R$, pois ultrapassou o limite.\033[m ')
else: 
    print('Está dentro do permitido, \033[32mparabéns\033[m!')
