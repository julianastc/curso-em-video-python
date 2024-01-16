n = (input('Digite algo '))
print(f'''
    O tipo primitivo desse valor é:  {type(n)}
    Só tem espaços?  {n.isspace()} 
    É um número?     {n.isnumeric()}
    É alfabético?    {n.isalpha()}
    É alfanumérico?  {n.isalnum()}
    É decimal?       {n.isdecimal()}
    É maiúsucula?    {n.isupper()}
    É minúsculo?     {n.islower()}
    Está capitalizado? {n.istitle()}
    ''')