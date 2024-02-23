#Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).

year = int(input('Digite um ano: '))

leap_year_rule_one = year % 4 == 0 
leap_year_rule_two = year % 100 != 0
is_year_leap = leap_year_rule_one and leap_year_rule_two

if is_year_leap:
    print(f'O ano {year} é bissexto. ')
else: 
    print(f'O ano {year} NÃO é bissexto. ')