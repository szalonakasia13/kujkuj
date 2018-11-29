/*
 * horner.cpp
 * 
 * Copyright 2018  <>
 * 
 *W(x) = 2x^3 + 3x^2 + 5x + 4 => 6
 *w(x) = x (2x^2 +3x + 5) + 4
 *w(x) = x (x (2x + 3) + 5) + 4 => 3
 */


#include <iostream>
using namespace std;

void drukujw(int stopien, floar tbwsp[]) {
    
    for;
} 

int main(int argc, char **argv)
{
    float *tbwsp; //wskaznik - adres pamieci komputera 
    int stopien = 0;
	cout << "Podaj stopień wielomianu: ";
    cin >> stopien;
    tbwsp = new float [stopien + 1];
    cout << tbwsp;
    for(int i = 0; i <= stopien; i++)
        cout << "Podaj współczynnik prz potędze " << stopien-i << " : ";
        cin >> tbwsp[i]
	return 0;
}

