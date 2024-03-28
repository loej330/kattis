#include <iostream>
using namespace std;

//Needs to throw out the king
//King does not follow the order; never the first or last

int main() {
    int n, g, pos, iExpected, iActual;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> g >> iExpected;
        iActual = iExpected; pos = 1;
        do { cin >> iActual; iExpected++; pos++; } while (iActual == iExpected);
        printf("%d\n", pos);
        cin.ignore(4096, '\n');
    }
    return 0;
}