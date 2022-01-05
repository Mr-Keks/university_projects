#include <iostream>
#include <conio.h>

using namespace std;

double fact(double a) {
	if (a == 0) 
		return 1;
	return a * fact(a - 1);
}

double serarf(double arr[]){
	double sarff = 0;
	double pr, res;
	res = 0;
	for (int i = 0; i < 10; i++) {
		sarff =  sarff + arr[i];
	}
	sarff = sarff / 10;
	cout << "sarff = " << sarff << endl;
	pr = sarff - arr[0];
	for (int i = 0; i < 10; i++) {
		if (fabs((sarff-arr[i])) < fabs(pr)) {
			pr = fabs((sarff - arr[i]));
			//if (fabs((sarff - arr[i])) < pr)
			res = arr[i];
		}
	}
	return res;
}

double SumaMinusElem(double arr[]) {
	double schet = 0;

	for (int i = 0; i < 10; i++) {
		if (arr[i] < 0)
			schet += arr[i];
	}
	return schet;
}

int main() {

	double A[10];
	double B[10];
	double C[10];
	double k[10];
	double min;
	double saA,saB,saC;

	cout << "***Filling the array***" << endl;
	min = A[0];
	for (int i = 0; i < 10; i++) {
		cout << "enter " << i << "value: ";
		cin >> A[i];
		k[i] = i;
		B[i] = (cos(12.0 * k[i]) / fact(k[i]));
		if (i == 0) min = A[0];
		if (min > A[i]) min = A[i];
	}
	system("cls");
	
	for (int i = 0; i < 10; i++) {
		if (B[i] < 0)
			C[i] = B[i];
		else 
			C[i] = min;

		cout << "Your " << i << " value A: " << A[i] << endl;
		cout << "Your " << i << " value B: " << B[i] << endl;
		cout << endl;
		cout << C[i] << endl;

	}
	//system("cls");
	// serarf
	saA = serarf(A);
	saB = serarf(B);
	saC = serarf(C);
	
	cout << "serarefmetuchne z A = " << saA << endl;
	cout << "serarefmetuchne z B = " << saB << endl;
	cout << "serarefmetuchne z C = " << saC << endl;
	system("cls");
	cout << "schet A = " << SumaMinusElem(A) << endl;
	cout << "schet B = " << SumaMinusElem(B) << endl;
	cout << "schet C = " << SumaMinusElem(C) << endl;

	_getch();
	return 0;
}