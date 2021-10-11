"""
Napisati kod koji za datu godinu odreñuje da li je prestupna i štampa odgovarajuću
poruku.
"""

godina = int(input('Unesite godinu: '))

def prestupna_godina(godina):
    if godina%4 == 0:
        if godina%100 == 0:
            if godina%400 == 0:
                return f'{godina} je prestupna godina.'   
        else:
            return f'{godina} je prestupna godina.'       
    else:
        return f'{godina} nije prestupna godina.'

print(prestupna_godina(godina))