/*
 * znaki.cpp
 * 
 */

#include <iostream>

using namespace std;

int zlicz(char tab[]) {
    int i = 0; // indeks znaków w tablicy
    while (tab[i] != '\0') i++;
    return i;
}

void drukuj(char tab[], int roz) {
    for(int i=0; i<roz; i++) {
        cout << tab[i] << " ";
    }
}

void liczznaki(char tab[], int roz) {
    int spacje = 0;
    int interpunkcja = 0;
    int symbole = 0;
    for(int i=0; i<roz; i++) {
        if (tab[i] == ' ') spacje++;
        else if (tab[i] == '.' || tab[i] == ',') symbole++;
    }
    
int main(int argc, char **argv)
{
	const int rozmiar = 100;
    char tab[rozmiar]; 
    cout << "jak się nazywas?" << endl;
    // cin >> tab;
    cin.getline(tab, rozmiar);
    // cout << "cześć " << tab << "!" << endl; 
    drukuj(tab, zlicz(tab));
    return 0;
}

