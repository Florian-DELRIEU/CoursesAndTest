from vpython import *
origin = vector(0,0,0)

Ball = sphere(pos=origin,radius=0.5)
WallR = box(pos=vector(5.1,0,0),size=vector(0.2,10,10),color=color.green)
WallL = box(pos=vector(-5.1,0,0),size=vector(0.2,10,10),color=color.green)