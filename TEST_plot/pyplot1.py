"""
https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,cos

# ----------------------------- DATA --------------------------------
x = np.linspace(0,10,100)
f1 = sin(x)
f2 = cos(x)

# ---------------------------- PLOTS ---------------------------------
fig,ax = plt.subplots(2,1)
line1, = ax[0].plot(x,f1,label='sine')           # Retourne une liste contenant :Line2D:
line2, = ax[0].plot(x,f2,label='cosine')        # Retourne un objet :Line2D:
line3 = ax[1].plot(x,(f1+f2),label="sum" )

# ---------------------------- LABEL ---------------------------------
ax[0].set_title("sin et cos")
ax[1].set_title("sin + cos")
plt.show()

# ---------------------------- LEGENDS ---------------------------------
Legend_1 = ax[0].legend(handles=[line1],loc="upper left")
Legend_2 = ax[0].legend(handles=[line2],loc="lower right") # efface la legend d'avant
ax[0].add_artist(Legend_1)  # ajoute une legend sans effacer l'ancien