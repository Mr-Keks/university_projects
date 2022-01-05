#include <iostream>
#include <conio.h>
#include <algorithm>

using namespace std;
//using std::max;
//using std::min;

void MinMax(double a, double b) {
	if (a > b) {
		cout << "Max a ------ " << a << endl;
		cout << "Min b ------ " << b << "\n\n" << endl;
	}
	else if (b > a) {
		cout << "Max b ------ " << b << endl;
		cout << "Min a ------ " << a << "\n\n" << endl;
	}
	else {
		cout << "a and b equl";
	}
}
int main()
{
	//Task 1
	double a = 20, b = 5;
	double c = 21.6, d = 21.7;
	double v = 100.0, t = 100;
	//cout << "max "<< max(a, b) << " min " << min(a, b); // First way
	cout << "When a = 20, b = 5" << endl;
	MinMax(a, b);
	cout << "When a = 21.6, b = 21.7" << endl;
	MinMax(c, d);
	cout << "When a = 100.0, b = 100" << endl;
	MinMax(v, t);


	//Task 2
	double a1, b1, c1, d1;

	cout << "Enter values a,b,c \n";
	cin >> a1 >> b1 >> c1;
	d1 = b1 * b1 - 4 * c1;
	if (d1 < 0)
		cout << "(-inf;" << a1 << "] \n";
	else {
		if (d1 == 0) {
			double x0 = -b1 / 2;
			if (a1 < x0)
				cout << "(-inf; " << a1 << "] U [" << a1 << ";" << x0 << ")";
			else
			{
				if (a1 == x0)
					cout << "(-inf; " << a1 << "]\n";
				else
					cout << "(-inf; " << x0 << ") U (" << x0 << ";" << a1;
			}
		}
		else {
			double x1 = (-b1 - sqrt(d1)) / 2;
			double x2 = (-b1 + sqrt(d1)) / 2;
			if (a1 < x1)
				cout << "(-inf; " << a1 << ") U (" << a1 << "; " << x1 << ")\n";
			else
			{
				if (a1 <= x2)
					cout << "(-inf; " << x1 << ") U (" << x1 << "; " << x1 << ")";
				else
					cout << "(-inf" << x1 << ")\n";
			}
		}


		_getch();
		return 0;

	}
}

