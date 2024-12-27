#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    int numberOfTestCases;
    cin >> numberOfTestCases;
    for (int i = 0; i < numberOfTestCases; i++) {
        int n;
        cin >> n;
        string answer;
        cin >> answer;
        int numofA = std::count(answer.begin(), answer.end(), 'A');
        int numofB = std::count(answer.begin(), answer.end(), 'B');
        int numofC = std::count(answer.begin(), answer.end(), 'C');
        int numofD = std::count(answer.begin(), answer.end(), 'D');
        int noAnswer = std::count(answer.begin(), answer.end(), '?');
        int marks = min(n, numofA) + min(n, numofB) + min(n, numofC) + min(n, numofD);
        cout << marks << endl;   
    }
}