#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py

def liczby2():
    """
    Funkcja drukuje wszystkie liczby dwucyfrowe, w których nie powtarzają 
    się cyfry.  NA KONIEC ZWRACA ILOŚĆ takich liczb wykluczone liczby: 11 22 
    """
    ile = 0 #licznik liczb 
    for i in range(1, 10): #pętla dziesiątek 
        for j in range(10): #pętla jednostek 
            if i != j:
                print("{}{} ".format(i, j), end="")
                ile = ile + 1 #zliczanie liczb 
    return ile


def main(args):
    print("Liczba 2-cyfrowych:", liczby2())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

def liczby3():
    
    ile = 0 #licznik liczb 
    for i in range(1, 10): #pętla setek 
        for j in range(10): #pętla dziesiątek
            for k in range(10): #pętla jednostek 
            if i != j: and != k and j != k:
                print("{}{}{} ".format(i, j, k), end="")
                ile = ile + 1 #zliczanie liczb 
    return ile 
    
def main(args):
    print ("\n\nLiczb 2 cyfrowych:", liczby 2 
