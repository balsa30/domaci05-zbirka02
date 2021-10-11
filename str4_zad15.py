"""
Dat je četvorocifren broj. Odrediti broj koji se dobija zamjenom treće i druge cifre. Npr. od
5804 dobija se 5084.
"""

cetvorocif = int(input('Unesite cetvorocifreni broj: '))

prva = cetvorocif//1000
druga = (cetvorocif//100)%10
treca = (cetvorocif//10)%10
cetvrta = cetvorocif%10

druga, treca = treca, druga
cetvorocif = prva*1000 + druga*100 + treca*10 + cetvrta
print(cetvorocif)