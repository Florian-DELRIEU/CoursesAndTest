from vpython import *
import time

def normvector(vec):
    """
    Donne la norme du vecteur
    """
    if type(vec) is vector: return sqrt(vec.x**2+vec.y**2+vec.z**2)
def showaxis():
    """
    Affiche les trois axes du repère
    """
    Origin = vector(0,0,0)
    Xaxis = arrow(pos=Origin,axis=vector(1,0,0),color=color.blue)
    Yaxis = arrow(pos=Origin,axis=vector(0,1,0),color=color.red)
    Zaxis = arrow(pos=Origin,axis=vector(0,0,1),color=color.green)

scene = canvas(center=vector(2.5,0.5,0))
showaxis()
#OriginDot = sphere(radius=0.1,color=color.red,pos=vector(0,0,0))
Ball = sphere(radius=0.1,pos=vector(0,1,0),color=color.blue)
Floor = box(pos=vector(2.5,-0.02,0),size=vector(5,0.04,1),color=color.green)
gravity = vector(0,-9.81,0)
trail = curve(color=color.white)
VelocityVector = arrow()
dt,t = 1e-3,0

AirDensity = 1.2
Ball.DragCoeff = 1
Ball.SurfaceResistance = 1/2* 4*pi*Ball.radius**2  # 1/2 car moitie de la surface totale en contact
Impact = False
Ball.velocity = vector(1,0.1,0)
Ball.mass = 0.25

graph = gcurve(color=color.blue)
while t < 10:
    graph.plot(pos=(t,Ball.pos.y))
    trail.append(pos=Ball.pos)
    VelocityVector.pos = Ball.pos
    VelocityVector.axis = .25* Ball.velocity  # .25 pour modifier la taille du vecteur
    time.sleep(dt)  # Pour duree simulation réaliste
    Ball.Force = gravity*Ball.mass
    try:
        Ball.Force += .5*AirDensity*Ball.SurfaceResistance*normvector(Ball.velocity)**2\
                                                            *Ball.DragCoeff*(-Ball.velocity/normvector(Ball.velocity))
    except: pass
    Ball.pos += Ball.velocity * dt
    Ball.velocity += Ball.Force/Ball.mass*dt
    t += dt
    if Ball.pos.y < Ball.radius and not Impact:
        print("Impact velocity: {} m/s".format(normvector(Ball.velocity)))
        Ball.velocity.y = - Ball.velocity.y
        Impact = True  # Etat de contact
    if Ball.pos.y > Ball.radius and Impact:  # L'impact prends fin quand la sphere quitte le plan
        Impact = False