katilim = 0
for dd in range(100):
    okul = input("hangi okula gidiyorsun i/o/l")
    bilgi = input("satranç biliyor musunuz e/h")
    if okul == "o" and bilgi == "e":
        print("turnuvaya katılabilirsiniz")
        katilim +=1
    else:
        print("turnuvaya katılamazsınız")
print("turnuvaya katılmaya hakkazanan kişi sayısı",katilim)