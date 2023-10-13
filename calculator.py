from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("644x900")
root.title("calculator by shyam")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="licida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="green")
b = Button(f, text="9", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="8", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="7", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)
f.pack()
f = Frame(root, bg="green")
b = Button(f, text="6", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="5", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="4", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)
f.pack()
f = Frame(root, bg="green")
b = Button(f, text="3", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="2", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="1", padx=5, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)
f.pack()
f = Frame(root, bg="green")
b = Button(f, text="0", padx=8, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="-", padx=8, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="*", padx=8, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)
f.pack()
f = Frame(root, bg="green")
b = Button(f, text="/", padx=6, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="+", padx=4, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)

b = Button(f, text="=", padx=4, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button>", click)
f.pack()
f = Frame(root, bg="green")
b = Button(f, text="C", padx=3, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=5)
b.bind("<Button>", click)

b = Button(f, text=".", padx=3, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=5)
b.bind("<Button>", click)

b = Button(f, text="00", padx=3, pady=5, font="lucida 35 bold")
b.pack(side=LEFT, padx=4, pady=5)
b.bind("<Button>", click)
f.pack()

root.mainloop()