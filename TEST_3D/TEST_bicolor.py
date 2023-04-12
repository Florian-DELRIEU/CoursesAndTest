from vpython import *
import time as t
import numpy as np

obj = sphere( texture="BicolorFish.jpg" )
a = pi / 10
t.sleep(0.1)
obj.rotate(angle=a,axis=vector(0,1,1))