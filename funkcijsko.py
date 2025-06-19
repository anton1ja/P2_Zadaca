# Definirati dvije funkcije koje kao parametar primaju ime ali vraćaju različitu poruku dobrodošlice.
# Jedna neka ispisuje “Pozdrav {ime}!”, a druga “Dobrodošao {ime}!”
# Jedna od funkcija neka bude definirana lambda izrazom, a druga standardnim načinom.
# Zatim definiraj treću funkciju koja kao parametar prima naziv funkcije za ispis dobrodošlice i poziva je tako 
# što pošalje vaše ime u nju.
# Pozvati treću funkciju prosljeđujući joj neku od prve dvije definirane funkcije.

def pozdrav(ime):
    return 'Pozdrav ' + ime + '!'

dobrodosao = lambda ime: 'Dobrodošao ' + ime + '!'

unos = input('Vaše ime: ')

ispis = lambda naziv: naziv(unos)

print(ispis(pozdrav))
print(ispis(dobrodosao))
