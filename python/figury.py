#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py

def prostokata1(a, b, znak):
    
    for i in range(a):
        for j in range(b):
            print(znak, end='')
        print() #znaku końca lini, przejśćie do następnego wiersza 
def prostokat2(a, b, znak):
    
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b - 1:
                print(znak, end= '')
        else:
            print(" ", end='') #znak
        print()
    

def choinka1(h, znak):
    pass 
   



def choinka2(h, znak):
    pass
    
    
    
def main(args):
   a = int(input("podaj 1 bok prostokata: "))
   b = int(input("podaj 2 bok prostokata: "))
   znak = input("podaj znak: ")
   prostokat1(a, b, znak)
   print()
   prostokat2(a, b, znak)
   
   
   return 0
   
if __name__ == '__main__':
    import sys
    sys.exit(
    
    main(sys.argv))

