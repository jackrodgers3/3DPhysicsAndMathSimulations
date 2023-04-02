import vpython as v
import math as m
import numpy as np

v.scene.height = 720
v.scene.width = 1500
o = v.vector(0,0,0)
t = -5
deltat = 1e-2

initX = 3
step = 0.3
lim = 10
xaxis = v.box(pos = o, size = v.vector((2*lim)+1, 0.05, 0.05), color = v.color.red)
zaxis = v.box(pos = o, size = v.vector(0.05, 0.05, (2*lim)+1), color = v.color.red)
L1 = v.label(pos = v.vector((lim+1),0,0),
            text = "x",
            box = False)
L2 = v.label(pos = v.vector(0,0,(lim+1)),
            text = "t",
            box = False)

#define differential equation here
def dxdt(x):
    g = -1 * x
    return g

marker = v.sphere(pos = v.vector(initX,0,t), radius = 0.1, color = v.color.yellow, make_trail = True)


for i in np.arange(-1*lim, lim, step):
    for j in np.arange(-1*lim, lim, step):
        try:
            vij = v.vector(dxdt(i), 0, 1)
            v.arrow(pos=v.vector(i, 0, j), axis=v.hat(vij) * step, shaftwidth=step * 0.1, color=v.color.cyan)
        except ValueError as ve:
            pass

cancel = 0
while (abs(marker.pos.x) <= lim and abs(marker.pos.z) <= lim) and cancel == 0:
    v.rate(80)
    xc = marker.pos.x
    try:
        xprime = v.vector(dxdt(xc), 0, 1)
    except ValueError as ve:
        cancel = 1
    marker.pos = marker.pos + (xprime*deltat)
    t = t + deltat