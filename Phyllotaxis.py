from tkinter import *
import random
import math


def draw():

    try:

        n, c = 0, 5
        angle = float("{:.3f}".format(random.uniform(130.000, 150.000)))
        label_text.set("Angle: " + str(angle) + "°")
        for _ in range(2500):
            a = n * math.radians(angle)
            r = c * math.sqrt(n)
            x = r * math.cos(a) + width / 2
            y = r * math.sin(a) + height / 2

            color = lambda: random.randint(0, 255)
            canvas.create_oval(x, y, x + 6, y + 6, fill='#%02X%02X%02X' % (color(),color(),color()))
            canvas.update()
            n += 1

        canvas.after(1000, canvas.delete('all'))
        draw()

    except TclError:

        window.quit()


window = Tk()
window.title("Phyllotaxis")
window.resizable(False, False)

width, height = 560, 560
canvas = Canvas(window, width=width, height=height, background="#000000", highlightthickness=0)
canvas.pack()

label_text = StringVar()
Label(
    canvas,
    textvariable=label_text,
    foreground="#FFFFFF",
    background="#000000",
    font=("Helvetica", 9)
).place(x=width - width, y=height - height)
draw()
