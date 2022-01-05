#include <iostream>
#include <conio.h>

using namespace std;

int main() {
	//Task 1
	/*
	float a, b, c;
	cin >> a >> b;
	c = a + b;
	cout << "a+b = " << c;
	return 0;
	*/
	//Task 2

	float a, a1, a2;
	cout << "Enter your value: ";
	cin >> a;
	system("cls");іфв
	a1 = a * a;
	cout << a << " in 2 = " << a1 << endl;
	a2 = a1 * a;
	cout << a << " in 3 = " << a2 << endl;
	a1 = a2 * a1;
	cout << a << " in 5 = " << a1 << endl;
	a2 = a1 * a1;
	cout << a << " in 10 = " << a2 << endl;
	a1 = a2 * a1;
	cout << a << " in 15 = " << a1 << endl;

	_getch();
	return 0;
}

