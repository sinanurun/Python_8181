# -*- coding: utf-8 -*-
# dosya = open("deneme.txt","r",encoding="utf-8")
# print(dosya.read())
# print(dosya.read(8))
# print(dosya.readlines())
# for dd in dosya:
#     print(dd)
# print(dosya.readlines())
# dosya.close()

dosya = open("kaan.txt","r",encoding="utf-8")
# print(dosya.read())
# print(dosya.read(50))
# print(dosya.readline(2))
# print(dosya.readline())
#
# n = 1
# for dd in dosya.readlines():
#     print(n,dd)
#     n+=1
print([x for x in dosya][0])