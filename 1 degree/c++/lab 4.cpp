#include <iostream>
#include <conio.h>

using namespace std;

int main() {
	int A = 1, A1 = 1, A2 = 1;
	int N = 5, i = 1;
	// for
	cout << "*********** for () *************" << endl;
	for (int i = 1; i <= N; i++) {
		if (i % 2 == 0) {
			A2 = A;
			A = A2 + 2 * A1;
		}
		else {
			A1 = A;
			A = A1 + 2 * A2;
		}

		cout << "A " << i << " = " << A << endl;
		if (i != N)
			cout << "-----------------------------" << endl;
	}
	// while
	cout << endl;
	cout << "*********** while () *************" << endl;
	A = 1; A1 = 1; A2 = 1;
	while (i <= N) {
		if (i % 2 == 0) {
			A2 = A;
			A = A2 + 2 * A1;
		}
		else {
			A1 = A;
			A = A1 + 2 * A2;
		}
		cout << "A " << i << " = " << A << endl;
		if (i != N)
			cout << "-----------------------------" << endl;
		i++;
	}
	// do while
	cout << endl;
	cout << "*********** do while () *************" << endl;
	A = 1; A1 = 1; A2 = 1; i = 1;
	do {
		if (i % 2 == 0) {
			A2 = A;
			A = A2 + 2 * A1;
		}
		else {
			A1 = A;
			A = A1 + 2 * A2;
		}
		cout << "A " << i << " = " << A << endl;
		if (i != N)
			cout << "-----------------------------" << endl;
		i++;
	} while (i <= N);

	_getch();
	return 0;
}