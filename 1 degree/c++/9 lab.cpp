#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
	char A[50];
	int NumberOfWords = 1;

	cout << "Enter A: ";
	gets_s(A);

	for (int i = 0; i < strlen(A); i++)
	{
		if (A[i] == ' ') NumberOfWords += 1;
		if (A[i] == 's' || A[i] == 'S') A[i] = 'c';
	}

	cout << NumberOfWords << endl;
	cout << A;

	_getch();
	return 0;
}