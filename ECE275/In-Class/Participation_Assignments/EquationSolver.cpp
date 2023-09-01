#include <iostream>
#include <string>

using namespace std;
int main() {
    int a1, b1, c1;
    int a2, b2, c2;
    cin >> a1; cin >> b1; cin >> c1;
    cin >> a2; cin >> b2; cin >> c2;

    for(int x = -10; x < 11; x++) {
        for(int y = -10; y < 10; y++) {
            if(a1 * x + b1 * y == c1 && a2 * x + b2 * y == c2) {
                cout << "x = " << x << " y = " << y << endl;
                return 0;
            }
        }
    }
    cout << "No match" << endl;
    return 0;

}