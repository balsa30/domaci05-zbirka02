"""
Napisati kod koji učitava brojeve x, a i b provjerava da li x pripada intervalu [a,b] i štampa
odgovarajuću poruku („Pripada“ ili „Ne pripada“).
"""

x = int(input('Unesite broj: '))
a = int(input('Unesite donju granicu intervala: '))
b = int(input('Unesite gornju granicu intervala: '))

if x in range(a,b):
    print ('Pripada.')
else:
    print ('Ne pripada.')

