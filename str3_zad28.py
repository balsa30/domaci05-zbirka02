"""
Za prirodan broj k stampati frazu "Na izletu mo ubrali k pecuraka", gdje zavrsetak 
rijeci pecurka prilagodite broju k. Npr. 101 pecurku, 1204 pecurke, 506 pecuraka.
"""

k = int(input('Koliko ste pecuraka ubrali: '))

def mijenjanje_rijeci_po_broju(k):
    if k%10 == 1:
        return (f'Ubrali smo {k} pecurku.')
    elif k%10 > 1 and k%10 <5:
        return (f'Ubrali smo {k} pecurke.')
    else:
        return (f'Ubrali smo {k} pecuraka.')    

print(mijenjanje_rijeci_po_broju(k))