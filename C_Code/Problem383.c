#include <stdio.h>
#include <math.h>
int calcFirstFunc(long n);

void problem383(void) {
	printf("Problem 383\n");
	printf("Let f5(n) be the largest integer x for which 5^x divides n.\n");

	printf("CalcFirstFunc Result: %d\n",calcFirstFunc(625000));
}

int calcFirstFunc(long n) {
	if (n < 5) {
		return 0;
	}
	int x = 0;
	int result = 0;
	while (pow(5,x) < n) {
		long l = pow(5,x);
		printf("t: %i\n",(l));
		printf("x: %d\n",(x));
		if (n % pow(5,x) == 0) {
			result = x;
		}
		x++;
	}
	return (result);
}
