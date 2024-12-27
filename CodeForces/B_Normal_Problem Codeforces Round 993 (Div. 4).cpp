#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;  // Read the number of test cases

    while (t--) {
        string line;
        string result;
        cin >> line;
        for (char c : line) {
            if (c == 'q') {
                result.insert(0, 1, 'p');
            }
            else if (c == 'p') {
                result.insert(0, 1, 'q');
            }
            else if (c == 'w') {
                result.insert(0, 1, 'w');
            }
        }
        cout << result << endl;        
    }

    return 0;
}