#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int m, a, b, c;
        cin >> m >> a >> b >> c;
        int firstSeatMonkies = min(m, a);
        if (a < m && c > 0) {
            int difference = m -a;
            if (c > difference) {
                firstSeatMonkies += difference;
                c -= difference;
            }
            else if (c <= difference) {
                firstSeatMonkies += c;
                c = 0;
            }
        }
        int backSeatMonkies = min(m, b);
        if (b < m && c > 0) {
            int difference = m - b;
            if (c > difference) {
                backSeatMonkies += difference;
                c -= difference;
            }
            else if(c <= difference) {
                backSeatMonkies += c;
                c = 0;
            }
        }

        cout << firstSeatMonkies + backSeatMonkies << endl;   
    }
    return 0;
}