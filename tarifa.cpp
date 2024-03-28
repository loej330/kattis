#include <iostream>
using namespace std;

int main() {
    int X, N, P, MB;
    cin >> X; cin >> N; MB = 0;
    for (int i = 0; i < N; i++) {
        cin >> P; 
        MB += (X-P);
    }
    MB += X;
    cout << MB << endl; 
    return 0;
}