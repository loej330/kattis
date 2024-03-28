#include <iostream>
using namespace std;
#define MAX_SUM 2001
#define TARGET 1000

int main() {
    int n; cin >> n; int weight;
    int sums[MAX_SUM] = { 0 }; sums[0] = 1;
    for (int i = 0; i < n; i++) { 
        cin >> weight;
        for (int j = MAX_SUM-1; j >= 0; j--) {
            if (sums[j] == 1 && j + weight < MAX_SUM-1) { sums[j + weight] = 1; }
        }
    }
    int close, dist, best; close = MAX_SUM + 1;
    for (int j = MAX_SUM-1; j >= 0; j--) {
        if (sums[j] == 0) { continue; }
        dist = abs(j - TARGET);
        if (dist < close) { close = dist; best = j; }
        else if (dist == close ) { break; }
    }
    printf("%d\n", best);
    return 0;
}