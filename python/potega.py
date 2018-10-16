#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  obliczanie potęgi 


def potega_it(a, n):
    wynik = 1

    for i in range(n):
        wynik = wynik * a 
        print(wynik)
    
    return wynik
    
def main(args):
    #a, n = 3, 4
    #print("potęga {} do {} wynosi {}".format(a, n, potega_it(a, n)))
    assert(silnia_it(1, 2) == 1)
    assert(silnia_it(2, 2) == 4)
    assert(silnia_it(3, 2) == 9)
    assert(silnia_it(4, 2) == 16)
    assert(silnia_it(5, 3) == 125)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
