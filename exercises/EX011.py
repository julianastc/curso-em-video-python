WallWidth = float(input("Qual a largura da parede? "))
WallHeigth = float(input("Qual a altura da parede? "))
#WallSize = WallWidth , "x" , WallHeigth 
WallArea = WallWidth*WallHeigth
WallPaint = WallArea / 2
print(f'''Sua parede tem dimensão de {WallWidth}x{WallHeigth} e sua área é de {WallArea}.
Para pintar essa parede, você precisará de {WallPaint}L de tinta.
  ''')