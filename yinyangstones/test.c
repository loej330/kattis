#include <stdio.h>
#include <string.h>
#define max_input 100000

int main() {
    char stones[max_input];
    fgets(stones, sizeof(stones), stdin);
    int len_stones = (int)(strchr(stones, '\n') - stones);
    stones[len_stones] = '\0';

    int w_count = 0;
    int b_count = 0;
    for (int i = 0; i < len_stones; i++) {
        if (stones[i] == 'W') w_count++;
        else b_count++;
    }

    if (w_count == b_count) printf("1\n");
    else printf("0\n");

    return 0;
}
