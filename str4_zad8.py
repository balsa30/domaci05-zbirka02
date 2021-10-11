"""
Napisati kod koji za dati pozitivni realni broj r računa i štampa obim i površinu kruga
poluprečnika r. 
"""

r = float(input('Unesite poluprecnik kruga: '))

obim = 2*r*3.14
povrsina = r*r*3.14

print(f'Povrsina: {povrsina}, Obim: {obim}')