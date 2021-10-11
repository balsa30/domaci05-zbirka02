# Dat je trocifren broj. Odrediti broj koji se dobija zamjenom prve i posljednje cifre. 

trocif = int(input('Unesite trocifreni broj: '))
p = trocif//100
s = (trocif//10)%10
z = trocif%10


p, z = z, p
trocif = p*100 + s*10 + z
print(trocif)