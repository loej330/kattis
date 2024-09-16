#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int x;
    struct Node *next;
    struct Node *prev;
} Node;

int main() {
    int N, x, i, j, odd;
    char S[32];
    Node *back, *middle, *front, *current, *temp;
    
    scanf("%d", &N); getchar();
    fgets(S, sizeof(S), stdin); 
    S[strcspn(S, "\n")] = '\0';
    x = atoi(S + strcspn(S, " "));
    odd = 1;
    back = middle = front = current = (Node *)malloc(sizeof(Node));
    current->x = x;
    current->next = NULL;
    current->prev = NULL;

    for (i = 0; i < N-1; i++) {
        fgets(S, sizeof(S), stdin); 
        S[strcspn(S, "\n")] = '\0';
        x = atoi(S + strcspn(S, " "));
        if (S[0] == 'p') {
            odd = !odd;
            current = (Node *)malloc(sizeof(Node));
            current->x = x;
            switch(S[5]) {
                case 'f':
                    current->next = back;
                    current->prev = NULL;
                    back->prev = current;
                    back = current;
                    if (odd) {
                        middle = middle->prev;
                    }
                    break;
                case 'm':
                    if (odd) {
                        current->next = middle;
                        current->prev = middle->prev;
                        middle->prev->next = current;
                        middle->prev = current;
                    } else {
                        current->next = middle->next;
                        current->prev = middle;
                        middle->next->prev = current;
                        middle->next = current;
                    }
                    middle = current;
                    break;
                case 'b':
                    current->next = NULL;
                    current->prev = front;
                    front->next = current;
                    front = current;
                    if (!odd) {
                        middle = middle->next;
                    }
                    break;
            }
        } else {
            current = back;
            for (j = 0; j < x; j++) {
                current = current->next;
            }
            printf("%d\n", current->x);
        }
    }
    current = back;
    while (1) {
        temp = current->next;
        free(current);
        if (temp == NULL) { break; }
        current = temp;
    }
    return 0;
}
