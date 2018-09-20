#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py


def main(args):
    a = int(input("podaj  1 liczbe: "))
    b = int(input("Podaj 2 liczbę: "))
    c = int(input("Podaj 3 liczbę: "))
    
    if a >b:
       if a > c:
           print("maks: ", a)
    else:
           print("maks: ", c)
        
        
    return 0
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
