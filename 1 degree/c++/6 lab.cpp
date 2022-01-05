#include<iostream>
using namespace std;


int main()
{
	float u;
	float ax = -2., bx = 2., hx = 0.4;
	float ay = 1., by = 3., hy = 0.1;

	cout << " y\\x ";
	for (float x = ax; x < bx + hx / 2; x += hx)
	{
		cout.width(10);
		cout.precision(2);
		cout << x;
	}
	cout << endl;
	for (float y = ay; y < by + hy / 2; y += hy)
	{
		cout.width(6);
		cout.precision(2);
		cout << y;
		for (float x = ax; x < bx + hx / 2; x += hx)
		{
			u = sin(x*y) + cos(x/y);
			cout.width(10);
			cout.precision(4);
			cout << u;
		}
		cout << endl;
	}

}

/*	for (double y = 1; y <= 3; y += 0.1)
	{
		//cout << "---------------------------" << endl;
		
		cout << " | " << " y " << " | ";
		for (double x = -2; x <= 2; x += 0.4)
		{
			cout << fixed << setprecision(1) << y << "| ";
		}
		cout << endl;
		
		cout << " | " << " x " << " |";
		for (double x = -2; x <= 2; x += 0.4)
		{
			if (x < 0)
			{
				if ((x + 1) <= 0)	cout << fixed << setprecision(1) << x << "|";
				//else if ((x + 1) == double(-0.4)) cout << "== -0.4" << x;
				else cout << fixed << setprecision(1) << x << " ";

			}
			else cout << fixed << setprecision(1) << x << "   ";
			
			//cout << "|" <<  "U = " <<fixed << setprecision(1) << sin(x * y) + cos(x / y) << "|" << endl;
		}
		
		cout << endl;
		cout << endl;
		cout << endl;
	}
	//cout << "---------------------------" << endl;
	
	_getch();*/