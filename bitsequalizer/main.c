#include <stdio.h>
#include <string.h>
#define max_input 101

int convert(char *S, char *T) {
    int _x0 = 0; //Should only sub
    int _x1 = 0; //sub or swap (with a bonus cost)
    int _01 = 0; //sub or swap 
    int _10 = 0; //Must swap
    for (int i = 0; i < strlen(S); i++) {
        if (T[i] == '0') {
            if (S[i] == '?') _x0++; 
            else if (S[i] == '1') _10++;
        } else {
            if (S[i] == '?') _x1++;
            else if (S[i] == '0') _01++;
        }
    }
    if ( _10 > (_01 + _x1) ) //More swaps needed than available
        return (-1);
    if ( _10 > _01) //Must convert some ? to 0's before swapping
        return (_x0 + _x1 + _01 + (_10 - _01));
    //Only direct conversion or direct swaps 
    return (_x0 + _x1 + _01 );
}

int main() {
    char S[max_input];
    char T[max_input];
    int cases;
    scanf("%d", &cases); getchar();
    for (int i = 0; i < cases; i++) {
        fgets(S, sizeof(S), stdin);
        fgets(T, sizeof(T), stdin);
        S[strlen(S) - 1] = '\0';
        T[strlen(T) - 1] = '\0';
        printf("Case %d: %d\n", i+1, convert(S, T));
    }
}
