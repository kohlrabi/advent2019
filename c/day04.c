#include <stdio.h>
#include <string.h>

const int min = 367479;
const int max = 893698;

int password(int p)
{
	int i;
	char s[7];
	int two = 0;

	snprintf(s, 7, "%d", p);
	for(i=0; i<5; i++) {
		if(s[i] > s[i+1]) {
			return 0;
		}
		if(s[i] == s[i+1]) {
			two = 1;
		}
	}
	return two;
}

int main(int argc, char **argv)
{
	int i, s = 0;

	for(i=min; i<max+1; i++) {
		if(password(i)) {
			s++;
		}
	}

	printf("part1: %d\n", s);

	return 0;
}
