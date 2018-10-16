#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  obliczanie potęgi 


def silnia_it(n):
    # 0! = 1 
    # n! = 1 * ... *n dla <1;n>
    wynik = 1
    for liczba in range(1,n + 1):
        wynik = wynik * liczba
    return wynik
    
   

   
   
   
    
    for i in range(n):
        wynik = wynik * a 
        print(wynik)
    
    return wynik
    
def main(args):
    #n = 0
    #print("{}! = {}".format(n, silnia_it(n)))
    assert(silnia_it(0) == 1)
    assert(silnia_it(4) == 24)
    assert(silnia_it(10) == 3628800)
    return 0
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
