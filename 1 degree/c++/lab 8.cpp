#include <iostream>
#include <conio.h>

using namespace std;

int main() {
	const int rows = 3;
	const int cols = 3;

	int A [rows][cols];
	int B [rows][cols];

	int* a;
	a = new int [cols];
	a[0] = 0; a[1] = 0; a[2] = 0;

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			cout << "Enter " << j << "elem " << i << " rowsa: ";
			cin >> A[i][j];
			if (A[i][j] > 0) {
				a[i] += 1;
			}
		}
	}
	for (int i = 0; i <= rows; i++) {
		int k = 1;
		for (int j = 0; j < cols; j++) {
			if (k == 3) {
				B[i][j] = a[i];
			}
			else
				B[i][j] = A[i][k];
			k++;
		}
	}
	
	system("cls");

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (j == 0)
				cout << "|";
			if (B[i][j] >= 0)
				cout << " " << B[i][j];
			else
				cout << B[i][j];
			if (j == 2)
				cout << "|";
		}
		cout << endl;
	}
		

	_getch();
	return 0;
}