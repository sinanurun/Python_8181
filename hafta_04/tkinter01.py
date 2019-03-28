# from tkinter import *
#
# app = Tk()
#
# dugme = Button(app)
# dugme.config(background="red",text="merhaba")
# dugme.pack()
#
# app.mainloop()

from tkinter import *
def degis():
    yazi.config(text=" örnek degisti",fg="white")

pencere = Tk()



pencere.geometry("500x450")
pencere.title("python8181")

rakam1 = Button(text = "buton 1",fg="red",bg="yellow")
rakam2 = Button(text = "buton 2",fg="blue",bg="yellow")
rakam3 = Button(text = "buton 3",fg="green",bg="yellow",command = degis)

rakam1.pack(side=RIGHT)
rakam2.pack()
rakam3.pack(side = LEFT)
#
#
yazi = Label(text = "Merhaba Python severler",bg="blue")

yazi.pack(side = LEFT)



pencere.mainloop()