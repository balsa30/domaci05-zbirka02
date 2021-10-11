"""
Data su tri cijela broja A, B, C. Odrediti da li među njima ima bar jedan paran broj i bar
jedan neparan broj. Ulaz: Prvi red ulaza sadrži tri cijela broja A, B i C (1 ≤ A ≤ 1000). Izlaz:
Štampati „YES“ ili „NO“. 
"""

A = int(input('Unesite prvi broj: '))
B = int(input('Unesite drugi broj: '))
C = int(input('Unesite treci broj: '))

if ((A%2 == 0 or B%2 == 0 or C%2 == 0) and (A%2 != 0 or B%2 != 0 or C%2 != 0)):
    print('YES')
else: 
    print('NO')