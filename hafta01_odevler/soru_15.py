katilim = 0
k_sayisi = 0 # sorulan kişi sayısını bulmak için
while katilim<=50:
    okul = input("hangi okula gidiyorsun i/o/l")
    bilgi = input("satranç biliyor musunuz e/h")
    if okul == "o" and bilgi == "e":
        print("turnuvaya katılabilirsiniz")
        katilim +=1
    else:
        print("turnuvaya katılamazsınız")
    k_sayisi +=1
print("turnuvaya katılmaya hakkazanan kişi sayısı",katilim)
print("toplam sorulan kişi sayısı = ",k_sayisi)