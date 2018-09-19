#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sumuj(a, b):
    """
    Funkcja zwraca sumę dwóch podanych liczb
    """
    return a + b 
    
def roznica(a, b):
    """
    Funckja zwraca różnicę dwóch podanych liczb 
    """
    return a - b 
    
def iloraz(a, b):
    """
    Funkcja zwraca iloraz dwóch podanych liczb 
    """
    return a / b 
    
def iloczyn(a, b):
    """
    Funkcja zwraca iloczyn dwóch podanych liczb 
    """
    return a * b 
    
def main(args):
    a = int(input("podaj pierwsza liczbe: "))
    b = int(input ("Podaj 2 liczbę: "))
   
    print(sumuj(a, b))
    print(roznica(a, b))
    print(iloraz(a, b))
    print(iloczyn(a, b))
    
    

    return 0 
                        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
