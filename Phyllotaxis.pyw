from math import radians, sqrt, cos, sin, floor
from random import randint, uniform
from tkinter import *


def draw():

    limit, value = 255, lambda: randint(0, limit)
    rgb, color = [value(), value(), value()], []
    for i in range(len(rgb)):
        for _ in range(limit):
            if rgb[i] != limit:
                color.append("#" + "".join(["0{0:x}".format(j) if j < 16 else "{0:x}".format(j) for j in [int(k) for k in rgb]]))
                rgb[i] += 1

    angle = float("{:.3f}".format(uniform(1.000, 1000.000)))
    label_text.set("Angle: " + str(angle) + "°")

    color, n, c = sorted(color * floor(2500/len(color))), 0, 5
    color.reverse()

    for _ in range(len(color)):
        a, r = n * radians(angle), c * sqrt(n)
        x = r * cos(a) + (width / 2)
        y = r * sin(a) + (height / 2)

        canvas.create_text(x, y, text="⃝", fill=color[n], font=("Helvetica", 8))
        canvas.update()
        n += 1

    canvas.after(1500, canvas.delete('all'))
    draw()


window = Tk()
window.title("Phyllotaxis")
window.resizable(False, False)

width, height = 560, 600
canvas = Canvas(window, width=width, height=height, bg="#000000", highlightthickness=0)
canvas.pack()

label_text = StringVar()
Label(canvas, textvariable=label_text, fg="#FFFFFF", bg="#000000", font=("Consolas", 9)).place(x=4, y=4)
draw()
