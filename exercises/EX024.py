city = input('Em que cidade você nasceu? ')

city_att = city.strip().lower()
city_rule = city_att[0:3]

answer = 'san' in city_rule

print(f'{answer}')