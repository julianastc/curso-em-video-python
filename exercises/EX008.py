m = float(input("Uma distância em metros: "))
k = m / 1000
h = m / 100
da = m / 10
d = m * 10
c = m * 100
mil = m * 1000
print (f'''
A medida de {m}m corresponde a
{k}km
{h}hm
{da}dam
{d:.0f}dm
{c:.0f}cm
{mil:.0f}mm
''')