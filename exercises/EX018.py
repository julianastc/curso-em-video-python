from math import sin, tan, cos, degrees, radians

angulo_graus = int(input("Qual é o valor do ângulo? "))
angulo_rad = radians(angulo_graus)

#seno
seno_ang = sin(angulo_rad)

# cos
cos_ang = cos(angulo_rad)

#tan
tan_ang = tan(angulo_rad)

print(f'''O seno de {angulo_graus}° é {seno_ang:.4f}, o cosseno é {cos_ang:.4f} e a tangente é {tan_ang:.4f}.
    ''')

