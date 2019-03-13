toplam = 0
for dd in range(10):
    print(dd+1,". sayıyı giriniz")
    sayi = int(input())
    toplam = toplam + sayi
print("girilen sayıların toplamı",toplam)
print("girilen sayıların ortalaması",toplam/10)