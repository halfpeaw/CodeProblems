/*
 * problem12.c
 *
 *  Created on: Feb 1, 2012
 *      Author: halfpeaw
 */
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

void problem12(void) {
	printf("The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.\n");
	printf("What is the value of the first triangle number to have over five hundred divisors?\n");
	long long sum = 1;
	long long next = 2;
	int divisors = 0;
	int greatest = 0;
	long long counter = 0;
	while (divisors < 501) {
		counter++;
		//reset
		if (counter > sum / 2) {
			if (divisors > greatest) {
				printf("sum: %llu, num div: %d\n",sum,divisors);
				greatest = divisors;
				fflush(stdout);
			}
			if (sum > 2147400000) {
				printf("There might be a problem\n");
				printf("sum: %llu, num div: %d\n",sum,divisors);
				fflush(stdout);
			}
			counter = 1;
			divisors = 0;
			sum += next;
			next += 1;
		}
		if (sum % counter == 0) {

			divisors += 1;
		}
	}
	printf("Results: %d\n",sum);

}

