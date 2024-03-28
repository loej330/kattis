#include <iostream>
using namespace std;

int main() {
    int n, day;
    long junk, min;
    min = 10000000000; day = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> junk; 
        if (junk < min) {
            min = junk;
            day = i;
        }
    }
    printf("%d\n", day);
    return 0;
}