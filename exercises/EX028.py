from random import choice

number_attempt = int(input('Eu escolhi um número entre 0 e 5. Tente adivinhar qual é esse número! '))
number_options = [0, 1, 2, 3, 4, 5]
number_choose = choice(number_options)

if number_attempt == number_choose:
    print('Parabéns! Você acertou.')
else:
    print(f'Que pena, você errou. A resposta era {number_choose} ')