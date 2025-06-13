# Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje
# kao prvo slovo vašeg imena, a završava kao prvo slovo prezimena.
# String mora sadržavati bar jedan broj između 0 i 5 i razmak.

import re
encoding = 'utf-8'

regKrajevi = r'^(A).*(Ć)$'
regBroj = r'[0-5]'
regRazmak = r'\s'

while 1:
    unos = input('Unesite tekst: ')
    
    if not re.search(regKrajevi, unos):
        print('Tekst mora početi slovom "A" i završiti slovom "Ć".')
        continue

    if not re.search(regBroj, unos):
        print('Tekst mora sadržavati bar jedan broj između 0 i 5.')
        continue

    if not re.search(regRazmak, unos):
        print('Tekst mora sadržavati barem jedan razmak.')
        continue

    print('Uspješan unos!')
    break

