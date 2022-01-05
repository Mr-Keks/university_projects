#include <iostream>
#include <conio.h>
#include <algorithm>

using namespace std;

int main() {
	double A[10];
	double B[10];
	double C[10];

	cout << "***Filling array***" << endl;
	for (int i = 1; i <= 10; i++) {
		cout << "Enter " << i << "element array: ";
		cin >> A[i];
		B[i] = i * sin(2 * i) + 2 * i*sin(i);
	}
	for (int i = 1; i <= 10; i++) {
		C[i] = max(A[i], B[i]);
	}
	system("cls");
	for (int i = 1; i <= 10; i++) {
		cout << "A[" << i << "] = " << A[i] << endl;
		cout << "B[" << i << "] = " << B[i] << endl;
		cout << "C[" << i << "] = " << C[i] << endl;
		if (i != 10)
			cout << "----------------------------------" << endl;
	}

	_getch();
	return 0;
}