import random
import vpython as v
import time as t
import tkinter as tk

def gui_param(PADX, PADY):
    window = tk.Tk()
    window.resizable(width=False, height=False)

    ##variables
    view_trail = tk.BooleanVar()
    numplanets = tk.StringVar()
    xrange = tk.StringVar()
    vrange = tk.StringVar()
    mrange = tk.StringVar()


    frm_numplanets = tk.Frame(master=window)
    lbl_numplanets = tk.Label(master=frm_numplanets, text="Number of planets: ")
    ent_numplanets = tk.Entry(master=frm_numplanets, width=10, textvariable=numplanets)
    lbl_numplanets.grid(row = 0, column = 0, sticky = "w")
    ent_numplanets.grid(row = 0, column = 1, sticky = "e")
    frm_numplanets.grid(row = 0, column = 0, padx= PADX, pady= PADY)


    frm_xrange = tk.Frame(master=window)
    lbl_xrange = tk.Label(master=frm_xrange, text="Maximum initial position:  ")
    ent_xrange = tk.Entry(master=frm_xrange, width=10, textvariable=xrange)
    lbl_xrange.grid(row = 0, column = 0, sticky="w")
    ent_xrange.grid(row = 0, column = 1, sticky="e")
    frm_xrange.grid(row = 1, column = 0, pady= PADY)

    frm_vrange = tk.Frame(master=window)
    lbl_vrange = tk.Label(master=frm_vrange, text="Maximum initial velocity:  ")
    ent_vrange = tk.Entry(master=frm_vrange, width=10, textvariable=vrange)
    lbl_vrange.grid(row = 0, column = 0, sticky="w")
    ent_vrange.grid(row = 0, column = 1, sticky="e")
    frm_vrange.grid(row = 2, column = 0, pady= PADY)

    frm_mrange = tk.Frame(master=window)
    lbl_mrange = tk.Label(master=frm_mrange, text="Maximum mass:  ")
    ent_mrange = tk.Entry(master=frm_mrange, width=10, textvariable=mrange)
    lbl_mrange.grid(row = 0, column = 0, sticky="w")
    ent_mrange.grid(row = 0, column = 1, sticky="e")
    frm_mrange.grid(row = 3, column = 0, pady= PADY)

    frm_trails = tk.Frame(master=window)
    lbl_trails = tk.Label(master=frm_trails, text="View planet paths?")
    r1 = tk.Radiobutton(master=frm_trails, text="Yes", variable=view_trail, value=True)
    r2 = tk.Radiobutton(master=frm_trails, text="No", variable=view_trail, value=False)
    lbl_trails.grid(row=0, column=0, sticky="w")
    r1.grid(row = 1, column= 1, sticky="e")
    r2.grid(row=2, column=1, sticky="e")
    frm_trails.grid(row=4, column=0, pady=PADY)

    frm_button = tk.Frame(master=window)
    btn_exit = tk.Button(master=frm_button, text="Done", command=window.destroy)
    btn_exit.grid(row = 0, column=0)
    frm_button.grid(row = 5, column = 0, pady= (0.5 * PADY))

    window.mainloop()

    return [int(numplanets.get()), int(xrange.get()), int(vrange.get()), int(mrange.get()), view_trail.get()]

def gen_rand_bodies(num, xrange, vrange, mrange, viewtrails):
    bodies = []
    for i in range(num):
        body = v.sphere(pos = 1e7 * v.vector(random.randint(-xrange, xrange),
                                       random.randint(-xrange, xrange),
                                       random.randint(-xrange, xrange)),
                        radius = 6.4e6,
                        color = v.color.cyan,
                        make_trail = viewtrails
                        )
        scale = random.randint(1, mrange)
        body.m = scale * pow(10, random.randint(32, 33))
        body.radius = body.radius * (scale)
        body.v = 1e7 * v.vector(random.randint(-vrange, vrange),
                          random.randint(-vrange, vrange),
                          random.randint(-vrange, vrange))

        body.color = colors[random.randint(0, len(colors) - 1)]
        bodies.append(body)
    return bodies

params = gui_param(50, 20)

# you need an interstellar .wav file to play this, otherwise just comment it out. Or put your own music in.
from playsound import playsound
playsound(r"interstellar.wav", False)

v.scene.height = 720
v.scene.width = 1500

t = 0
deltat = 1e-2
tmax = 30
o = v.vector(0, 0, 0)
dia = v.vector(1, 1, 1)
G = 6.6743e-11
colors = [v.vector(116/255, 135/255, 166/255),
          v.vector(100/255, 181/255, 91/255),
          v.vector(176/255, 83/255, 117/255),
          v.vector(204/255, 162/255, 63/255),
          v.vector(158/255, 187/255, 255/255),
          v.vector(97/255, 122/255, 45/255),
          v.vector(156/255, 101/255, 47/255),
          v.vector(232/255, 179/255, 245/255),
          v.vector(198/255, 222/255, 166/255)]

L = v.label(pos = v.vector(40,25,0),
            text = "t = ",
            pixel_pos = True,
            box = False)

#time loop
cons = 0.25
bodies = gen_rand_bodies(params[0], params[1], params[2], params[3], params[4])
startmass = 0
for i in range(len(bodies)):
    startmass = startmass + bodies[i].m
while t < tmax:
    v.rate(100)
    L.text = "t = "+str(round(t, 4))
    for i in range(len(bodies)):
        for j in range(len(bodies)):
            if i != j and bodies[i].m != 0 and bodies[j].m != 0:

                #force implementation
                r = bodies[i].pos - bodies[j].pos
                rmag = v.mag(r)
                rhat = v.hat(r)
                Fg = -1 * G * bodies[i].m * bodies[j].m * rhat / (rmag**2)
                bodies[i].v = bodies[i].v + ((Fg/bodies[i].m) * deltat)

                #inelastic collision implementation
                if rmag <= (bodies[i].radius + bodies[j].radius):
                    pinit = (bodies[i].m * bodies[i].v) + (bodies[j].m * bodies[j].v)
                    if bodies[i].m > bodies[j].m:
                        bodies[i].m = bodies[i].m + (cons * bodies[j].m)
                        bodies[i].radius = bodies[i].radius + (cons * bodies[j].radius)
                        bodies[i].v = pinit / bodies[i].m
                        bodies[j].m = 0
                        bodies[j].radius = 0
                        bodies[j].make_trail = False
                        bodies[j].clear_trail()
                    elif bodies[i].m <= bodies[j].m:
                        bodies[j].m = bodies[j].m + (cons * bodies[i].m)
                        bodies[j].radius = bodies[j].radius + (cons * bodies[i].radius)
                        bodies[j].v = pinit / bodies[j].m
                        bodies[i].m = 0
                        bodies[i].radius = 0
                        bodies[i].make_trail = False
                        bodies[i].clear_trail()
    for i in range(len(bodies)):
        bodies[i].pos = bodies[i].pos + (bodies[i].v * deltat)
    t = t + deltat
L.text = "t = "+str(tmax)
maxmass = 0
maxrad = 0
for i in range(len(bodies)):
    if bodies[i].m > maxmass:
        maxmass = bodies[i].m
    if bodies[i].radius > maxrad:
        maxrad = bodies[i].radius
numleft = 0
endmass = 0
for i in range(len(bodies)):
    if bodies[i].m != 0:
        numleft = numleft + 1
    endmass = endmass + bodies[i].m

lostmass = abs(startmass - endmass)
print("SIMULATION SUMMARY\n-----------------------------------\nLargest radius: {} meters  ({} times the size of Earth's)\nLargest mass: {} "
      "kilograms\nNumber of original planets left: {}\nMass not conserved: {} kilograms".format(maxrad, str(round(maxrad / 6.378e6, 1)),maxmass,
                                                                                                numleft, lostmass))
while True:
    t.sleep(1)

