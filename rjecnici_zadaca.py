'''
Koristeći listu imena svakom studentu generirati nasumičnu
ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)
'''
from random import randint

imena = ['Ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan', 'Zvjezdan', 'Ivan', 'Mihaela', 'Ružica',
'Dorijan', 'Petra', 'Matej', 'Filip', 'Magdalena', 'Mate', 'Iva', 'Danis', 'Josip',
'Nebojša', 'Ante', 'Luka', 'Ante', 'Lorena', 'Ivan', 'Nikola', 'Ivan', 'Helena', 'Ivan',
'Gabrijela', 'Andrija', 'Regina', 'Petar', 'Dino', 'Marija', 'Semir', 'Gabriela', 'Borna',
'Filip', 'Krešimir', 'Ivana', 'Gabrijel', 'Vinko', 'Vinko', 'Romana', 'Viktorija', 'Mija',
'Matej', 'Vinko', 'Luka', 'Antea', 'Ivan', 'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']

brojanje = dict()
ocjene = []

for i in imena:
    ocj = randint(1,5)
    ocjene.append(ocj)

for i in ocjene:
    if i in brojanje:
        brojanje[i] += 1
    else:
        brojanje[i] = 1
 
for i in brojanje:
    print("Ocjena ", i, ": ", brojanje[i], sep = "")

brojProlaznih = 0
for i in brojanje:
    if i != 1:
        brojProlaznih += brojanje[i]

print("Postotak prolaznosti je:", int(round(brojProlaznih / len(ocjene), 2) * 100), "%")

