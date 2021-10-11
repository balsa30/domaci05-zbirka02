"""
Dat je cetvorocifreni prirodan broj. Ako su mu cifra jedinica i cifra hiljada jednake,
stampati kvadrat dvocifrenog broja koji se dobije kada se uklone cifra jedinica i cifra hiljada.
Ako te dvije cifre nisu jednake, stampati zbir kvadrata svih cifara.
"""

abcd = int(input('Unesite cetvorocifreni broj: '))
d = abcd%10
c = (abcd//10)%10
b = (abcd//100)%10
a = abcd//1000

def cifra_jedinica_i_hiljada_jednake(abcd):
    if abcd > 999 and abcd < 10000:
        if d == a:
            return (b * 10 + c) * (b * 10 + c)
        else:
            return (a*a + b*b + c*c + d*d)
    else:
        return ('Nijeste unijeli cetvorocifreni broj.')
        
print(cifra_jedinica_i_hiljada_jednake(abcd))



