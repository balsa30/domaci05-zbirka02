""" 
Za neku državu poznata je njena površina i broj stanovnika. Odrediti gustinu naseljenosti
te države.
"""

povrsina = int(input('Povrsina drzave u km²: '))
broj_stanovnika = int(input('Broj stanovnika: '))

gustina_naseljenosti = broj_stanovnika/povrsina

print(f'{gustina_naseljenosti} stanovnika po km²')