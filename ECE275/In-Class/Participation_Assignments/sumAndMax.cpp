#include <iostream>
#include <string>
#include <iomanip>

using namespace std;
int main() {
    int input;
    
    cin >> input;
    int max = 0;
    int sum = 0;
    int nums = 0;
    while (input >= 0)
    {
        if (input > max){
            max = input;
        }
        sum+=input;
        nums++;
        cin >> input;
    }
    cout << fixed << setprecision(2);
    if (nums > 0) {
        //cout << nums;
        cout << max << " " << static_cast<double> (sum) / nums;
    } else {
        cout << max << " " << 0;
    }
    cout << endl;
    
}