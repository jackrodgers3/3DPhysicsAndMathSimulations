import vpython as v
import math as m
import numpy as np

v.scene.height = 720
v.scene.width = 1500
o = v.vector(0,0,0)
t = -3
deltat = 1e-3

initX = -3
initT = t
step = 0.3
lim = 20
xaxis = v.box(pos = o, size = v.vector((2*lim), 0.05, 0.05), color = v.color.red)
zaxis = v.box(pos = o, size = v.vector(0.05, 0.05, (2*lim)), color = v.color.red)
L1 = v.label(pos = v.vector((lim),0,0),
            text = "x",
            box = False)
L2 = v.label(pos = v.vector(0,0,(lim)),
            text = "t",
            box = False)
L3 = v.label(pos = v.vector(100,125,0),
            text = "",
            pixel_pos = True,
            box = False)

#comment out to freely move around sim
v.scene.camera.pos = v.vector(0, lim-1, 0)
v.scene.forward = v.vector(0, -1, 0)


#define differential equation here
def dxdt(x, t):
    g = ((t**2) - 5) / (-6 * (x**2))
    return g

marker = v.sphere(pos = v.vector(initX,0,t), radius = 0.05, color = v.color.yellow, make_trail = True)
mradscale = 0.3 * m.log10(lim)
marker.trail_radius = marker.trail_radius * mradscale

for i in np.arange(-1*lim, lim, step):
    for j in np.arange(-1*lim, lim, step):
        try:
            vij = v.vector(dxdt(i, j), 0, 1)
            v.arrow(pos=v.vector(i, 0, j), axis=v.hat(vij) * step, shaftwidth=step * 0.1, color=v.color.cyan)
        except ValueError as ve:
            pass

cancel = 0
while (abs(marker.pos.x) <= lim and abs(marker.pos.z) <= lim) and cancel == 0:
    v.rate(800)
    xc = marker.pos.x
    zc = marker.pos.z
    try:
        xprime = v.vector(dxdt(xc, zc), 0, 1)
    except ValueError as ve:
        cancel = 1
    marker.pos = marker.pos + (xprime*deltat)
    t = t + deltat
L3.text = "Path ("+str(initT)+"<"+"t"+"<"+str(int(t))+") complete"