def obrni(s):
    
    if s  == s[0]:
        return s[0]
    
    return s[-1] + obrni(s[:-1])