#include <iostream>

using namespace std;

//Task 1
double P(double X, double Y, double T, double U, double V)
{
	
	double Arr[5] = { X, Y, T, U, V };
	double Temp = Arr[0];

	for (int i = 0; i < 5; i++) 
	{
		if (Arr[i] > Temp) Temp = Arr[i];
		else continue;
	}
	return Temp;
}
// Task 2
double Fact(double B) 
{
	if (B != 1) return B * Fact(B - 1);
	else return B;
}

double Min(double* A)
{
	double Temp = A[0];

	for (int i = 0; i < 10; i++)
	{
		if (A[i] < Temp) Temp = A[i];
		else continue;
	}
	return Temp;
}

double ArithmeticMean(double* S)
{
	double serAr = 0;
	double close;

	for (int i = 0; i < 10; i++)
	{
		serAr += S[i];
		if (i == 9) serAr / i;
	}
	close = S[0];
	for (int i = 0; i < 10; i++)
	{
		if (fabs(S[i] - serAr) < fabs(close - serAr)) close = S[i];
		else continue;
	}
	return close;
}

double SummaMinus(double* K)
{
	double sumM = 0;

	for (int i = 0; i < 10; i++)
	{
		if (K[i] < 0) sumM += 1;
		else continue;
	}
	return sumM;
}
int main() 
{
	cout << "************Task 1************ \n\n";
	//Task 1
	int A = 5, B = 20, C = 43;
	double Z;

	Z = P(2*A, A * B * pow(C, 2), 0.2 * A * B, 5 * A * C, 0.25 * B * C) + 
		P(2.3 * B * C, pow (A, 2) * B, 0.65 * A * C, 3.14 * A * pow(C, 2), 0.62 * pow(B,2) * C);

	cout << "Z = " << Z << endl;

	//Task 2
	cout << "************Task 2************ \n\n";
	double A1[10], B1[10], C1[10];

	
	
	
	cout << "*****Filling the array A and B*****" << endl;
	for (int k = 0; k < 10; k++)
	{
		cout << "Enter A[" << k << "]: ";
		cin >> A1[k];

		if (k == 0)
			B1[k] = cos(12 * k) / Fact(1);
		B1[k] = cos(12 * k) / Fact(1);
	}
	system("cls");

	for (int i = 0; i < 10; i++)
	{
		if (B1[i] > 0) C1[i] = Min(A1);
		else C1[i] = B1[i];
	}

	cout << "The number of the element, array A1, closest to the arithmetic mean: " << ArithmeticMean(A1) << endl;
	cout << "The number of the element, array B1, closest to the arithmetic mean: " << ArithmeticMean(B1) << endl;
	cout << "The number of the element, array C1, closest to the arithmetic mean: " << ArithmeticMean(C1) << endl;
	cout << endl;
	cout << "The sum of all negative elements A1: " << SummaMinus(A1) << endl;
	cout << "The sum of all negative elements B1: " << SummaMinus(B1) << endl;
	cout << "The sum of all negative elements C1: " << SummaMinus(C1) << endl;
	
	return 0;
}