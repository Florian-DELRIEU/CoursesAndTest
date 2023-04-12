def div(entier,diviseur):
    assert (type(entier) and type(diviseur)) == int
    
    p_e = entier // diviseur
    reste = entier % diviseur
    return p_e , reste