#include <iostream>

using namespace std;

int main()
{
    cout << "What's your name?" << endl;

    string name;

    cin >> name;

    cout << "Hello " + name << endl;

    cout << "What's your student ID?" << endl;

    string studentID;

    cin >> studentID;

    cout << "Your ID is " + studentID << endl;

    cout << "Enter number1" << endl;

    int number1;

    cin >> number1;

    cout << "Enter number2" << endl;

    int number2;

    cin >> number2;

    int sum = number1 + number2;
    int diff = number1 - number2;
    int prod = number1 * number2;

    cout << endl;

    cout << "Sum: " << sum << endl;

    cout << "Diff: " << diff << endl;

    cout << "Prod: " << prod << endl;

    cout << endl << "*" << endl << "**" << endl << "***";

    return 0;
}
