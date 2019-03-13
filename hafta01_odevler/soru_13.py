"""
bir satranç turnuvası düşünelim
katılım şartları ortaokula gitmek ve
satranç biliyor olmak olsun
"""
okul = input("hangi okula gidiyorsun i/o/l")
bilgi = input("satranç biliyor musunuz e/h")
if okul == "o" and bilgi == "e":
    print("turnuvaya katılabilirsiniz")
else:
    print("turnuvaya katılamazsınız")