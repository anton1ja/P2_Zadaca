# Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.

def parni(maks):
    a = 0
    
    while a < maks:
        yield a
        a += 2

def neparni(maks):
    b = 1

    while b < maks:
        yield b
        b += 2

parametar = int(input('Unesite maksimalnu vrijednost: '))

print(f'Parni brojevi manji od {parametar}:')

parni_gen = parni(parametar)
for i in parni_gen:
    print(i)

print(f'Neparni brojevi manji od {parametar}:')

neparni_gen = neparni(parametar)
for i in neparni_gen:
    print(i)
