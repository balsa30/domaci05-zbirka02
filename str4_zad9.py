# Napisati kod koji za date stranice a, b i c kvadra računa površinu i zapreminu kvadra. 

a = int(input('Unesite stranicu a: '))
b = int(input('Unesite stranicu b: '))
c = int(input('Unesite stranicu c: '))

povrsina = 2 * (a*b + a*c + b*c)
zapremina = a*b*c

print(f'Povrsina: {povrsina}, Zapremina: {zapremina}')