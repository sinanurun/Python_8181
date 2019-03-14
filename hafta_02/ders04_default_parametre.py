"""parametre girilmeyince kendisi parametre tanımlayan"""
#
# def pi(deger = 3.14):
#     print(deger)
#
# pi(3)

def d_alan(r,pi=3.14):
    alan = pi*r**2
    print(alan)

d_alan(6,3)
d_alan(6)