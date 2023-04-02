
import tkinter as tk
import math as m
#parameters: view trail, numplanets, xrange, vrange, mrange

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

b = m.log2(-1)
print(b)