import math

speed = int(input('Qual é a velocidade do carro? '))
speed_trafficticket = (speed - 80) * 7.00

if speed>=80: 
    print(f'Você foi multado em {speed_trafficticket:.2f}R$, pois ultrapassou o limite. ')
else: 
    print('Está dentro do permitido, parabéns!')
