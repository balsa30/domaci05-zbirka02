"""
Napisati kod koji učitava dva cijela broja m i n štampa poruku „x je djeljiv sa y” ili „x nije
djeljiv sa y“. Npr. „15 je djeljiv sa 3“ ili „15 nije djeljiv sa 4“.
"""

m = int(input('Unesite prvi broj: '))
n = int(input('Unesite drugi broj: '))

def djeljivost_2_broja():
    if m%n == 0:
        return 'x je djeljiv sa y'
    else:
        return 'x nije djeljiv sa y'

print(djeljivost_2_broja())