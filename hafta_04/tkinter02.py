from tkinter import *

pencere = Tk()
asilisim = "mahmut"
asilparola = "mehmet"


def girisyapma():
    parola = parolagiris.get()
    isim = isimgiris.get()
    if (parola == asilparola and isim == asilisim):
        girisdurumu.config(text="Doğru", bg="green")
    else:
        girisdurumu.config(text="Yanlış", bg="red",fg ="yellow")
        giris.config(image=photo)
#
#
isim = Label(pencere, text="adınız")
isim.grid(row=0, column=0)
isimgiris = Entry(pencere, width="8")
isimgiris.grid(row=0, column=1)
parola = Label(pencere, text="şiferniz")
parolagiris = Entry(pencere, width="8", show="*")
parola.grid(row=1, column=0)
parolagiris.grid(row=1, column=1)
sifremihatirla = Checkbutton(pencere, text="şifremi hatırla")
sifremihatirla.grid(row=2, columnspan=2)
giris = Button(pencere, text="giriş", command=girisyapma)
giris.grid(row=3, column=0)
girisdurumu = Label(pencere, text="bilgileriniz girniz")
girisdurumu.grid(row=3, column=1)
photo = PhotoImage(file="pythonn.png")
resim = Label(pencere,image=photo)
resim.grid(row=4,column=0)

pencere.mainloop()