import random
import vpython as v
import time as t
import math as m
colors = [v.vector(116/255, 135/255, 166/255),
          v.vector(100/255, 181/255, 91/255),
          v.vector(176/255, 83/255, 117/255),
          v.vector(204/255, 162/255, 63/255),
          v.vector(158/255, 187/255, 255/255),
          v.vector(97/255, 122/255, 45/255),
          v.vector(156/255, 101/255, 47/255),
          v.vector(232/255, 179/255, 245/255),
          v.vector(198/255, 222/255, 166/255)]
v.scene.height = 720
v.scene.width = 1500

t = 0
deltat = 1e-3
tmax = 30
o = v.vector(0, 0, 0)
dia = v.vector(1, 1, 1)

floor = v.box(pos = o, size = v.vector(10, 1, 10), color = colors[0])
wall = v.box(pos = v.vector(0, 3, (-floor.size.z/2)), size = v.vector(5, 5, 0.01), color = colors[1])
spring = v.arrow(pos = wall.pos - v.vector(0,2,0), axis = v.vector(0,0,9), shaftwidth = 0.1, color = colors[2])
boxinq = v.box(pos = spring.pos + spring.axis, size = dia, color = colors[3])

#Physical variables
initL = 9
eqL = initL / 2
initV = 0
spring.k = 10
boxinq.m = 1
w = m.sqrt(spring.k / boxinq.m)
spring.axis = v.vector(0,0, initL)
spring.v = initV
f = w / (2*m.pi)

L1 = v.label(pos = v.vector(70,50,0),
            text = "Frequency: "+str(round(f, 3))+" Hz",
            pixel_pos = True,
            box = False)
L2 = v.label(pos = v.vector(60,25,0),
            text = "t = ",
            pixel_pos = True,
            box = False)
L3 = v.label(pos = v.vector(60,75,0),
            text = "Period: "+str(round(1/f, 3))+" s",
            pixel_pos = True,
            box = False)
L4 = v.label(pos = v.vector(65,100,0),
            text = "",
            pixel_pos = True,
            box = False)
L5 = v.label(pos = v.vector(65,125,0),
            text = "",
            pixel_pos = True,
            box = False)
L6 = v.label(pos = v.vector(65,150,0),
            text = "",
            pixel_pos = True,
            box = False)

KE = 0
PE = 0
E = 0
while t < tmax:
    v.rate(1000)
    KE = 0.5 * boxinq.m * (spring.v **2)
    L2.text = "t = " + str(round(t, 4)) + " s"
    L4.text = "KE = " + str(round(KE, 3)) + " J"
    L5.text = "PE = " + str(round(PE, 3)) + " J"
    PE = spring.k * ((v.mag(spring.axis) - eqL)**2) * 0.5
    E = KE + PE
    L6.text = "E = " + str(round(E, 3)) + " J"
    Fsp = -1 * spring.k * (v.mag(spring.axis) - eqL)
    spring.v = spring.v + (Fsp*deltat)
    spring.axis.z = spring.axis.z + (spring.v*deltat)
    boxinq.pos.z = spring.pos.z + spring.axis.z + 0.5
    t = t + deltat

while True:
    t.sleep(1)