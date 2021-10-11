# Dat je cetvorocifreni prirodan broj abcd. Stampati poruku "Super" ako vazi a c = b d.

abcd = int(input('Unesite cetvorocifreni broj: '))
d = abcd%10
c = (abcd//10)%10
b = (abcd//100)%10
a = abcd//1000

def odstampaj_super_za_ac_jednako_bd(abcd):
    if abcd > 999 and abcd < 10000:
        if a == b and c == d:
            print('Super')
    else:
         print('Nijeste unijeli cetvorocifreni broj.')

odstampaj_super_za_ac_jednako_bd(abcd)