import random

import vpython as v
import time as t
'''
class particle:
    def __init__(self, mass, charge, initpos):
        self.mass = mass
        self.charge = charge
        self.initpos = initpos
        if self.charge == -1:
            self.col = color.blue
        elif self.charge == 1:
            self.col = color.red
        else: self.col = color.grey
        self.part = sphere(pos = self.initpos, radius = 1, color = self.col)
    def move(self, initvel, deltat):
        self.initvel = initvel
        self.part.pos = self.part.pos + (self.initvel*deltat)
'''

v.scene.height = 600
v.scene.width = 1000
t = 0
deltat = 1e-2
tmax = 10
o = v.vector(0, 0, 0)
dia = v.vector(1, 1, 1)
e = 1.60217663e-19
k = 9e9
nm = 1e-9

def gen_rand_particles(num, xrange, vrange, qrange):
    particles = []
    for i in range(num):
        part = v.sphere(pos = nm * v.vector(random.randint(-xrange, xrange),
                                       random.randint(-xrange, xrange),
                                       random.randint(-xrange, xrange)),
                        radius = 0.1 * nm,
                        color = v.color.cyan,
                        make_trail = True
                        )
        part.m = 1
        part.q = e * random.randint(-qrange, qrange)
        part.v = nm * v.vector(random.randint(-vrange, vrange),
                          random.randint(-vrange, vrange),
                          random.randint(-vrange, vrange))
        if part.q < 0:
            part.color = v.color.blue
        elif part.q > 0:
            part.color = v.color.red
        else:
            part.color = v.vector(213 / 255, 213 / 255, 213 / 255)
        particles.append(part)
    return particles


particles = gen_rand_particles(20, 7, 0, 10)
while t < tmax:
    v.rate(80)
    for i in range(len(particles)):
        for j in range(len(particles)):
            if i != j:
                r = particles[i].pos - particles[j].pos
                rmag = v.mag(r)
                rhat = v.hat(r)
                Fel = k* particles[i].q * particles[j].q * rhat / (rmag**2)
                particles[i].v = particles[i].v + ((Fel/particles[i].m) * deltat)
    for i in range(len(particles)):
        particles[i].pos = particles[i].pos + (particles[i].v * deltat)
    t = t + deltat
while True:
    t.sleep(1)
