import os
# a , w , x

if os.path.exists("kaan.txt"):
    print("dosya var")
    print("dosyayı siliyorum")
    os.remove("kaan.txt")
else:
    dosya = open("kaan.txt", "x", encoding="utf-8")
    dosya.write("dördüncü ders merhaba hocalarım nasılsınız")
    dosya.close()