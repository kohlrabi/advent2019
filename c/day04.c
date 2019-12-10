#include <stdio.h>
#include <string.h>

const int min = 367479;
const int max = 893698;

int part1(int p)
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

int part2(int p)
{
	int i;
	char s[7];
	int v, l;

	snprintf(s, 7, "%d", p);
	v = s[0];
	l = 1;
	for(i=1; i<6; i++) {
		if(s[i] == v) {
			l += 1;
		}
		else {
			if(l == 2) {
				return 1;
			}
			v = s[i];
			l = 1;
		}
	}
	return l == 2;
}

int main(int argc, char **argv)
{
	int i, s = 0, s2 = 0;

	for(i=min; i<max+1; i++) {
		if(part1(i)) {
			s++;
			if(part2(i)) {
				s2++;
			}
		}
	}

	printf("part1: %d\n", s);
	printf("part2: %d\n", s2);

	return 0;
}
