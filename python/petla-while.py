#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  petla4.py 


def main(args):
    start = int(input("pobierz tą liczbę 1 helpppppp: "))
    stop = int(input("podaj liczbę 2: "))
    
    while start >= stop: 
          print("za mała druga liczba: ")
    stop = int(input("pobierz ponownie drugą liczbę: "))
    
    if start >= stop:
        print("żle mongole!: " )
        exit(0)
    
    for i in range(start, stop + 1):
        if  i % 2 == 0:
            print(i)
        else:
            print("liczba nieparzysta")
    
    
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
