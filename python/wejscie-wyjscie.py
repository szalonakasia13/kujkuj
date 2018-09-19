#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szablon.py.py
#  
 def hello ():
     print ("witam kujkuj jetsme ")
     print ("jak masz na imie ?") 
     imie = input ("odpowiedz:")
     print("witaj" , imie )
     
def suma (l1,l2):
    print ("suma:", l1 + l2)
    
    
def suma2(a,b):
    #zmienne lokalne, o zasięgu lokalnym 
    a = int(input("podaj pierwsza liczbe: "))
    print(a)
    b = int(input ("Podaj 2 liczbę: "))
    print(b)
    #print ("suma:" ,a + b)
    #print("różnica" , a - b)
    #print("iloczyn" , a * b)
    #print("iloraz" , a / b)
    hello()
def suma(l1,l2):
    print("suma:", l1 + l2)
def różnica(l1 , l2):
    print("różnnica:" l1 - l2)
def iloczyn(l1 , l2):
    print("iloczyn" l1 * l2) 
def iloraz(l1 * l2): 
    print("iloraz" l1 / l2)
def suma2(l1,l2):
    print("suma:", l1 + l2)
    
def suma2(a, b):
    """
    funkcja sumuje dwie liczby i zwraca wynik 
    """
    return a + b
    
    
    
        
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
