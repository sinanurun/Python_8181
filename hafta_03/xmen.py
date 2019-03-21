import os  #dosya işlemleri için
class Admin():

    def __init__(self):
        pass

    def yemek_olustur(self):

        self.yemek_adi = input("Yemek Adı Giriniz")
        self.fiyat = float(input("Yemek Fiyatı Giriniz"))
        self.yemek = Meal(self.yemek_adi, self.fiyat)

    def yemek_bilgileri(self):
        self.yemek.yemek_bilgileri

    @staticmethod
    def yemek_listesi():
        f = open("yemekler.txt","r")
        for x in f:
            yemek_bilgisi = x.split("+")
            print("yemek adı:\t {}, yemek fiyatı:\t {}".format(yemek_bilgisi[0],yemek_bilgisi[1]))
            print("\t\tyemek malzemeleri: {}".format(yemek_bilgisi[2]))
        f.close()


class Meal():
    def __init__(self, yemek_adi, fiyat):
        self.yemek_adi = yemek_adi
        self.fiyat = fiyat
        self.yemek_malzeme_ekle()

    def yemek_malzeme_ekle(self):
        print(self.yemek_adi,"için gerekli malzemeleri virgül ile ayırarak girin")
        self.malzemeler = input()
        self.yemek_bilgileri()
        onay = input("Kaydetmek için E/H")
        if onay.upper() =="E":
            f = open("yemekler.txt","a")
            icerik = self.yemek_adi+"+"+ str(self.fiyat)+"+"+ self.malzemeler+"\n"
            f.write(icerik)
            f.close()

    def yemek_bilgileri(self):
        return print(self.yemek_adi, self.fiyat, self.malzemeler)

class Inventory():
    pass



class Costumer():
    def __init__(self):
        pass

    def yemek_listele(self):
        pass




yonetici = Admin()
musteri = Costumer()
durum = True
while durum:
    giris = input("Yönetici girişi için Y, Müşteri girişi için M tuşlayınız")
    if giris.upper() == "Y":
        print("Heş geldiniz Yönetici")
        yonetici = Admin()
        cevap = input("yemek oluşturmak için 1, var olan yemekleri listelemek için 2, ürün girmek için 3, kullanıcı değişmek için D, programdan çıkmak için ise E tuşlayınız")
        if cevap == "1":
            yonetici.yemek_olustur()
        elif cevap =="2":
            yonetici.yemek_listesi()
        elif cevap =="3":
            pass
        elif cevap.upper() =="D":
            pass
        elif cevap.upper()=="E":
            break



"""

13. Develop an meal ordering system with following features Admin
•Define meals and prices
•Define ingredients for each meal
•Manage inventory for ingredients
•Query sale transactions by date and meals
Customer
• Order a meal Manage order history 
"""
