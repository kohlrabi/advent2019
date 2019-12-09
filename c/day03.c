#include <stdio.h>
#include <limits.h>

#define SIZE (8192*2)

void walk(char c, int d, int map[SIZE*2][SIZE*2][3], int pos[2], int wire, int *len)
{
	int i;
	int x = pos[0];
	int y = pos[1];
	int l = *len;

	int *m;

	switch(c) {
		case 'L':
			for(i=0; i<d; i++) {
				m = map[x-i][y];
				m[0] += wire;
				m[wire] = m[wire] == 0 ? l + i : m[wire-1];
			}
			pos[0] -= d;
			break;
		case 'R':
			for(i=0; i<d; i++) {
				m = map[x+i][y];
				m[0] += wire;
				m[wire] = m[wire] == 0 ? l + i : m[wire-1];
			}
			pos[0] += d;
			break;
		case 'D':
			for(i=0; i<d; i++) {
				m = map[x][y-i];
				m[0] += wire;
				m[wire] = m[wire] == 0 ? l + i : m[wire-1];
			}
			pos[1] -= d;
			break;
		case 'U':
			for(i=0; i<d; i++) {
				m = map[x][y+i];
				m[0] += wire;
				m[wire] = m[wire] == 0 ? l + i : m[wire-1];
			}
			pos[1] += d;
			break;
	}
	*len = l + d;
}

int part1(int map[SIZE*2][SIZE*2][3]) {
	int i, j, x, y, min = INT_MAX;
	for(i=0; i<SIZE*2; i++) {
		for(j=0; j<SIZE*2; j++) {
			if(map[i][j][0] == 3 && SIZE != i && SIZE != j) {
				x = i<SIZE ? SIZE-i : i-SIZE;
				y = j<SIZE ? SIZE-j : j-SIZE;
				min = min < x+y ? min : x+y;
			}
		}
	}
	return min;
}

int part2(int map[SIZE*2][SIZE*2][3]) {
	int i, j, x, y, min = INT_MAX;
	int *m;
	for(i=0; i<SIZE*2; i++) {
		for(j=0; j<SIZE*2; j++) {
			m = map[i][j];
			if(i != SIZE && j != SIZE) {
				if(m[0] == 3) {
					x = m[1];
					y = m[2];
					min = min < x+y ? min : x+y;
				}
			}
		}
	}
	return min;
}


int main(int argc, char **argv)
{
	static int map[SIZE*2][SIZE*2][3] = { 0 };
	int pos[2] = { SIZE, SIZE };
	char c;
	int d;
	int wire = 1;
	int len = 0;

	while(scanf("%c%d,", &c, &d) != EOF) {
		if(c == '\n') {
			pos[0] = SIZE;
			pos[1] = SIZE;
			len = 0;
			wire = 2;
			continue;
		}
		walk(c, d, map, pos, wire, &len);
	}

	printf("part1: %d\n", part1(map));
	printf("part2: %d\n", part2(map));

	return 0;
}
