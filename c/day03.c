#include <stdio.h>
#include <limits.h>

#define SIZE (8192*2)

void walk(char c, int d, int map[SIZE*2][SIZE*2], int pos[2], int wire)
{
	int i;
	int x = pos[0];
	int y = pos[1];

	switch(c) {
		case 'L':
			for(i=0; i<d; i++) {
				map[x-i][y] += wire;
			}
			pos[0] -= d;
			break;
		case 'R':
			for(i=0; i<d; i++) {
				map[x+i][y] += wire;
			}
			pos[0] += d;
			break;
		case 'D':
			for(i=0; i<d; i++) {
				map[x][y-i] += wire;
			}
			pos[1] -= d;
			break;
		case 'U':
			for(i=0; i<d; i++) {
				map[x][y+i] += wire;
			}
			pos[1] += d;
			break;
	}
}

int part1(int map[SIZE*2][SIZE*2]) {
	int i, j, x, y, min = INT_MAX;
	for(i=0; i<SIZE*2; i++) {
		for(j=0; j<SIZE*2; j++) {
			if(map[i][j] == 3 && SIZE != i && SIZE != j) {
				x = i<SIZE ? SIZE-i : i-SIZE;
				y = j<SIZE ? SIZE-j : j-SIZE;
				min = min < x+y ? min : x+y;
			}
		}
	}
	return min;
}



int main(int argc, char **argv)
{
	static int map[SIZE*2][SIZE*2] = { 0 };
	int pos[2] = { SIZE, SIZE };
	char c;
	int d;
	int wire = 1;

	while(scanf("%c%d,", &c, &d) != EOF) {
		if(c == '\n') {
			pos[0] = SIZE;
			pos[1] = SIZE;
			wire *= 2;
			continue;
		}
		walk(c, d, map, pos, wire);
	}

	printf("part1: %d\n", part1(map));

	return 0;
}
