# Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
# Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 
# Nedovoljan 0-49%
# Dovoljan 50-65%
# Dobar 65-80%
# Vrlo dobar 80-90%
# Izvrstan 90-100%

import csv

# vraca prezime
def prez(tup):
    return tup[1]

with open('rezultati_25.csv', newline='', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    rez = [tuple(row[:3]) for row in reader]

sortirano = sorted(rez, key = prez)

brojOcj = {
'Nedovoljan' : 0,
'Dovoljan' : 0,
'Dobar' : 0,
'Vrlo dobar' : 0,
'Izvrstan' : 0
    }

for ime, prezime, bodovi in sortirano:
    if int(bodovi) < 50:
        brojOcj['Nedovoljan'] += 1
    elif 50 <= int(bodovi) < 65:
        brojOcj['Dovoljan'] += 1
    elif 65 <= int(bodovi) < 80:
        brojOcj['Dobar'] += 1
    elif 80 <= int(bodovi) < 90:
        brojOcj['Vrlo dobar'] += 1
    else:
        brojOcj['Izvrstan'] += 1

for ocjena in brojOcj:
    print(ocjena, brojOcj[ocjena])
