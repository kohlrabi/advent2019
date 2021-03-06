#include <stdio.h>

int part1(int m)
{
	return m / 3 - 2;
}

int part2(int m)
{
	int sum = 0;

	while((m = part1(m)) > 0) {
		sum += m;
	}
	return sum;
}

int main(int argc, char **argv)
{
	int m, total = 0, total_fuel = 0;

	while(scanf("%d\n", &m) != EOF) {
		total += part1(m);
		total_fuel += part2(m);
	}

	printf("part 1: %d\n", total);
	printf("part 2: %d\n", total_fuel);

	return 0;
}
