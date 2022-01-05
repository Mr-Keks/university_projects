#include <iostream>
#include <conio.h>
#include <math.h>

using namespace std;

double sqrtt(double a, double b) {
	return pow(a, 1.0 / b);
}

int main() {
	double A, B, C, X, Y;
	double U, V, Z;

	A = 1.592;
	B = 0.382;
	C = 0.5348;
	X = 1.2;
	Y = 21.5;

	U = ((pow(A, 2) / sqrtt(B, 3)*sin(3)) + (sqrtt(B, 4) / (pow(C, 2)*pow(A, B)))*(pow(tan(3), 3)));
	V = (exp(2)*sin(3 * atan(2 * sqrt(3) + 2 * acos(1 / 7))));
	Z = log(fabs(X) + 5 * fabs(Y));

	
	cout << "U = " << U << endl;
	cout << "V = " << V << endl;
	cout << "Z = " << Z << endl;




	_getch();
	return 0;
}