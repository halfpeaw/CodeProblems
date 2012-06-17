/*
 * problem4.c
 *
 *  Created on: Jan 21, 2012
 *      Author: halfpeaw
 */
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

char* revStr(char* str)
{
  int end= strlen(str)-1;
  int start = 0;

  while( start<end )
  {
    str[start] ^= str[end];
    str[end] ^=   str[start];
    str[start]^= str[end];

    ++start;
    --end;
  }

  return str;
}

int  isPalindrome (char* buf, int size) {
	if (size %2 != 0) {
		printf("Not even length");
		return -1;
	}
	char str1[size/2+1];
	char str2[size/2+1];

	strncpy(str1,buf,size/2);
	strncpy(str2,buf+(size/2),size/2);
	str1[size/2] = '\0';
	str2[size/2] = '\0';

	if (strcmp (str1,revStr(str2)) == 0) {
		printf("String is Palindrome: %s\n",buf);
		return 0;
	} else {
		return -1;
	}

}

void problem4() {
	int num = 123456;
	int size = 6;
	int high = 0;
	char buf[size+1];
	for (int y = 999; y > 0; y--) {
		for (int x = 999; x > 0; x--) {
			num = x * y;
			itoa(num, buf, 10);
			if (isPalindrome(buf,size) == 0) {
				if (x*y > high) {
					high = x * y;
				}

			}

		}
	}
	printf("Result %d\n", high);
	return;
}

