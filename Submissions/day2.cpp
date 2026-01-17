#include <iostream>
#include <string>
using namespace std;

int main() {
    int choice;
    cout << "Choose option:\n";
    cout << "1. Even or Odd\n";
    cout << "2. Voting Eligibility\n";
    cout << "3. Largest of Two Numbers\n";
    cout << "4. Login Check\n";
    cout << "Enter choice: ";
    cin >> choice;

    if (choice == 1) {
        int n;
        cout << "Enter number: ";
        cin >> n;

        if (n % 2 == 0)
            cout << "Even";
        else
            cout << "Odd";
    }

    else if (choice == 2) {
        int age;
        cout << "Enter age: ";
        cin >> age;

        if (age >= 18)
            cout << "Eligible to vote";
        else
            cout << "Not eligible to vote";
    }

    else if (choice == 3) {
        int a, b;
        cout << "Enter two numbers: ";
        cin >> a >> b;

        if (a > b)
            cout << "Largest: " << a;
        else
            cout << "Largest: " << b;
    }

    else if (choice == 4) {
        string pass;
        cout << "Enter password: ";
        cin >> pass;

        if (pass == "Zero_Theory")
            cout << "Login Successful";
        else
            cout << "Incorrect Password";
    }

    else {
        cout << "Invalid choice";
    }

    return 0;
}
