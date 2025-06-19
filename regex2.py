# Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata 
# ime.prezime@fpmoz.sum.ba
# Nakon toga napisati regex za provjeru eduId koji mora biti formata 
# iprezimeX@sum.ba
# gdje je i prvo slovo imena + prezime.
# X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati
# (može biti samo iprezime@sum.ba).
# Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.

import re

def unos(regex):
    podatak = None      # podatak - mail/eduID
    
    while not podatak:
        string = input()

        podatak = re.search(regex, string)

        if not podatak:
            print('Pogrešan unos. Pokušajte ponovno:')
        else:
            break

    return podatak.string


regMail = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'

print('Unesite mail:')
mail = unos(regMail)

# izvlačimo ime i prezime iz maila
krajIme = mail.find('.')
krajPrezime = mail.find('@')

ime = mail[:krajIme]
prezime = mail[krajIme + 1: krajPrezime]

# ime i prezime u mailu i ID-u se moraju podudarati    
regID = fr'^{ime[0]}{prezime}\d*@sum.ba$'

print('\nUnesite eduID:')
eduID = unos(regID)

print('\nUspješno ste unijeli podatke.')

input()
