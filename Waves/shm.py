import random
import vpython as v
import time as t
import math as m

v.scene.height = 720
v.scene.width = 1500

t = 0
deltat = 1e-2
tmax = 30
o = v.vector(0, 0, 0)
dia = v.vector(1, 1, 1)
shm = v.sphere(pos = o, radius = 1, color = v.color.red, make_trail = True)
shm.p = 1
shm.w = 5
shm.A = 1
shm.m = 1
shm.KE = 0
f = shm.w / (2*m.pi)
L1 = v.label(pos = v.vector(80,50,0),
            text = "Frequency: "+str(round(f, 4))+" Hz",
            pixel_pos = True,
            box = False)
L2 = v.label(pos = v.vector(40,25,0),
            text = "t = ",
            pixel_pos = True,
            box = False)
L3 = v.label(pos = v.vector(60,75,0),
            text = "Period: "+str(round(1/f, 3))+" s",
            pixel_pos = True,
            box = False)
L4 = v.label(pos = v.vector(80,100,0),
            text = "",
            pixel_pos = True,
            box = False)
L5 = v.label(pos = v.vector(80,125,0),
            text = "",
            pixel_pos = True,
            box = False)


while t < tmax:
    v.rate(100)
    L2.text = "t = " + str(round(t, 4)) + " s"
    shm.pos.x = shm.A*m.cos((shm.w*t) + shm.p)
    shm.v = -1*shm.w*shm.A*m.sin((shm.w*t) + shm.p)
    shm.KE = 0.5*shm.m*(shm.v**2)
    L4.text = "Velocity: "+str(round(shm.v, 2))+" m/s"
    L5.text = "Kinetic Energy: " + str(round(shm.KE, 2)) + " J"
    t = t + deltat
L2.text = "t = "+str(tmax)+" s"
while True:
    t.sleep(1)