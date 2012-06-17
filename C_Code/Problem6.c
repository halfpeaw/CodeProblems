/*
 * Problem6.c
 *
 *  Created on: Jan 21, 2012
 *      Author: halfpeaw
 */
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

int sum(int start, int end) {
	int result = 0;
	result = ((end * (end + 1)) / 2) - ((start * (start + 1)) / 2);
	return result;
}
int sumSquare(int start, int  end) {
	int result = 0;
	result = (end * (end + 1) * (2*end+1)) / 6;
	result = result - ((start * (start + 1) * (2*start+1)) / 6);
	return result;
}
void problem6(void) {
	printf("Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.\n");
	int summation = sum(0,100);
	int sumSqr = sumSquare(0,100);
	int result = (summation * summation) - sumSqr;
	printf("Result: %d", result);
}

