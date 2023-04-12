import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import SSG_Library.Math as math

def dydt(y,t):
    """
    :param y:
    :param t: Meme si :t: n'est pas utilisé dans la fonction, il faut le mettre car il sert d'argument lors
              de l'intégration
    :return:
    """
    return np.sin(y)

t = np.arange(0,10,0.1)
t2 = np.arange(0,1,0.01)
y0 = 0

f = lambda t: np.sin(t)

int1 = integrate.quad(f,0,1)
int2 = math.integr(f(t2),t2)

print(int1)
print(int2)
print("Erreur relative"+ str(abs(int1-int2)/int2))
