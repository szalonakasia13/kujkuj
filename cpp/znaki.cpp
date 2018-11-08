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

void ascii(char tab[], int roz) {
    int kod = 0; //kod ascii znaku
    for(int i=0; i<roz; i++) {
        kod = (int)tab[i];
        if (kod > 96 && kod < 123)
            cout << (char)(kod-32) << " ";
        if (kod < 96 && kod >123)
            cout << (char)(kod+32) << " ";
        else
         cout << (int)tab[i] << " ";
    }
}

void liczznaki(char tab[], int roz) {
    int spacje = 0;
    int interpunkcja = 0;
    int symbole = 0;
    int reszta = 0;
    for(int i=0; i<roz; i++) {
        //~if (tab[i] == ' ') spacje++;
        //~else if (tab[i] == '.' || tab[i] == ',') symbole++; 
          //~interpunkcja++;
        //~else if (tab[i] == '.' || tab[i] == ',') symbole++; 
        switch (tab[i]) {
            case ' ':
            case '\t':
                spacje++;
            break;
            case '.':
            case ',':
                interpunkcja++;
            break;
            case '(':
            case ')':
                symbole++;
            break;
            default:
                reszta++;
            }
        }
        cout << "spacje: " << spacje << endl;
        cout << "interpunkcja: " << interpunkcja << endl;
        cout << "symbole: " << symbole << endl;
        cout << "reszta: " << reszta << endl;
    }
    
int main(int argc, char **argv)
{
	const int rozmiar = 100;
    char tab[rozmiar]; 
    cout << "jak się nazywas?" << endl;
    // cin >> tab;
    cin.getline(tab, rozmiar);
    // cout << "cześć " << tab << "!" << endl; 
    ascii(tab, zlicz(tab));
    cout << endl;
    liczznaki(tab, zlicz(tab));
    return 0;
}

