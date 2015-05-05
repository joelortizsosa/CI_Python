import math
from cmath import *
import sys

#Position dans le space, eviter utilisée le 0 absolute x) 
x=20
y=0.1
z=0.1
#//////////////////////
l1=12 #taille de bras en cm
l2=15 #taille de avant-bras en cm
#x = raw_input("Ingresa coordenada X: ")
#y = raw_input("Ingresa coordenada Y: ")
#z = raw_input("Ingresa coordenada Z: ")
Cq2 = (x**2 + y**2 + z**2 - l1**2 - l2**2)/(2*l1*l2)
q2 = -acos(Cq2)
q1 = atan(z/math.sqrt(x**2 + y**2)) - atan(-l2*math.sqrt(1-Cq2**2)/(l1+l2*Cq2) )
q0 = -atan(x/y)

q2=q2*180/math.pi
q1=q1*180/math.pi
q0=q0*180/math.pi
q2=round(q2.real)
q1=round(q1.real)
q0=round(q0.real)
print(q0)
print(q1)
print(q2)
