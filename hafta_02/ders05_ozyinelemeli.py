"""kendi kendini yineleyen recursive hanoi kuleleri gibi """


def faktoriyel(n):

 if n == 0:
    return 1
 else:
    return n * faktoriyel(n-1)
# 6*5*4*3*2*1*1

print(" 6! = ", faktoriyel(6))

def toplama(m):
    if m ==0 :
        return 0
    else:
        return m+toplama(m-1)

print(toplama(5))


# def main():
#
#  print(" 0! = ", faktoriyel(0)) # 1
#  print(" 1! = ", faktoriyel(1)) # 1*1
#  print(" 6! = ", faktoriyel(6)) # 6*5*4*2*1*1
#  print("10! = ", faktoriyel(10))
# main()