#  Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.

def obrni(s): 
    if s  == s[0]:
        return s[0]
    
    return s[-1] + obrni(s[:-1])

string = input('Unesite string: ')

print('Rezultat: ', obrni(string))
