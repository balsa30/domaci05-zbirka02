# Napisati kod koji provjerava da li je zbir cifara datog trocifrenog broj dvocifren broj. 

tr = int(input('Unesite trocifreni broj: '))
zbir_cifara = tr%10 + (tr/10)%10 + tr/100

def stampa_odgovor_ako_je_zbir_cif_dvocifren(tr): 
    if tr > 99 and tr < 1000:
        if  zbir_cifara > 9 and zbir_cifara < 100:
            return f'Zbir cifara {tr} JE dvocifren broj.'
        else: 
            return f'Zbir cifara {tr} NIJE dvocifren broj.'
    else:
        return 'Nijeste unijeli trocifreni broj.'


print(stampa_odgovor_ako_je_zbir_cif_dvocifren(tr))