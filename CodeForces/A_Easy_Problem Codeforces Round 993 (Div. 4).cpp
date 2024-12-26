// #include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;  // Read the number of test cases

    while (t--) {
        int n;
        cin >> n;  // Read the integer for the current test case
        // Process the input here
        int result = 0;
        for (int i = 0; i < n; i++) {
            int num1 = n - (i+1);
            int num2 = (i+1);
            if (num1 > 0 && num2 > 0) {
                result += 1;
                // cout << "(" << num1 << "," << num2 << ")";
            }
        }
        cout << result << endl;
    }

    return 0;
}
