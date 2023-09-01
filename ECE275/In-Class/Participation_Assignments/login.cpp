#include <iostream>
#include <string>

using namespace std;
int main() {
    string login = "";
    string first;
    string last;
    int number;
    cin >> first;
    cin >> last;
    cin >> number;
    if(last.size() < 5) {
        login += last;
    } else {
        login += last.substr(0, 5);
    }
    login.push_back(first.at(0));
    login.push_back((number % 100 / 10) + '0');
    login.push_back(number%10 + '0');
    cout << "Your login name: " << login << endl;


    return 0;
}