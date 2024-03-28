#include <iostream>

/*
S = (R1 + R2)/2
2S = R1 + R2
2S - R1 = R2
*/

int main() {
    int R1, S;
    scanf("%d %d", &R1, &S);
    printf("%d\n", (S * 2) - R1);
    return 0;
}