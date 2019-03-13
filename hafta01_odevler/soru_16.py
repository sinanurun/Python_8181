sayi1 = int(input("bir sayı giriniz"))
sayi2 = int(input("farklı bir sayı daha giriniz"))
if sayi1<sayi2:
    kucuk = sayi1
    buyuk = sayi2
else:
    kucuk = sayi2
    buyuk = sayi1
for dd in range(kucuk,buyuk):
    asal_durumu = 0
    for aa in range(2,dd):
        if dd%aa==0: #mod aldık kalana baktık
            asal_durumu = asal_durumu + 1
    if asal_durumu == 0:
        print(dd,"bir asal saydır")

