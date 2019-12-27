#include <stdio.h>
#include <limits.h>

#define SIZE 2048


typedef struct Vector
{
	int x;
	int y;
} Vector;

int abs(int a)
{
	return a<0 ? -a : a;
}

int manhattan(Vector *a)
{
	int r;
	r = abs(a->x) + abs(a->y);
	return r;
}

Vector add_vec(Vector *a, Vector *b)
{
	Vector v;
	v.x = a->x + b->x;
	v.y = a->y + b->y;
	return v;
}

Vector sub_vec(Vector *a, Vector *b)
{
	Vector v;
	v.x = a->x - b->x;
	v.y = a->y - b->y;
	return v;
}

Vector mul_vec_int(Vector *a, int b)
{
	Vector v;
	v.x = a->x * b;
	v.y = a->y * b;
	return v;
}

int mul_vec_vec(Vector *a, Vector *b)
{
	int v;
	v = a->x * b->x + a->y * b->y;
	return v;
}

// direction vectors are always orthogonal on the grid
int norm(Vector *a)
{
	if(a->x == 0) {
		return a->y;
	}
	else {
		return a->x;
	}
}

Vector normed(Vector *a)
{
	Vector v;
	v.x = a->x / norm(a);
	v.y = a->y / norm(a);
	return v;
}


typedef struct Edge
{
	Vector origin;
	Vector direction;
} Edge;

Vector intersection(Edge *a, Edge *b)
{
	Vector r;
	int v = 0, w = 0;

	Vector *ao = &(a->origin);
	Vector *bo = &(b->origin);
	Vector *ad = &(a->direction);
	Vector *bd = &(b->direction);
	Vector adn = normed(ad);
	Vector bdn = normed(bd);

	r.x = 0;
	r.y = 0;

	if (mul_vec_vec(&adn, &bdn) != 0) {
		return r;
	}

	if(adn.y == 0) {
		v = (bo->x - ao->x) / adn.x;
		w = (ao->y - bo->y) / bdn.y;
	}
	if(adn.x == 0) {
		v = (bo->y - ao->y) / adn.y;
		w = (ao->x - bo->x) / bdn.x;
	}

	if (v < 0 || w < 0 || v > norm(ad) || w > norm(bd)) {
		return r;
	}

	Vector t = mul_vec_int(&adn, v);
	Vector rr = add_vec(ao, &t);

	return norm(&rr) > 0 ? rr : r;
}



typedef struct Wire
{
	Edge edges[SIZE];
	int lengths[SIZE];
	size_t num;
	int length;
} Wire;


void walk(char c, int d, Wire *wire)
{
	size_t ind;

	ind = wire->num;
	Vector *origin = &(wire->edges[ind].origin);

	if(!ind) {
		origin->x = 0;
		origin->y = 0;
	}
	else {
		Vector *porigin = &(wire->edges[ind-1].origin);
		Vector *pdirection = &(wire->edges[ind-1].direction);
		Vector add = add_vec(porigin, pdirection);
		origin->x = add.x;
		origin->y = add.y;
	}

	Vector *direction = &(wire->edges[ind].direction);
	switch(c) {
		case 'L':
			direction->x = -d;
			direction->y = 0;
			break;
		case 'R':
			direction->x = d;
			direction->y = 0;
			break;
		case 'D':
			direction->x = 0;
			direction->y = -d;
			break;
		case 'U':
			direction->x = 0;
			direction->y = d;
			break;
	}
	wire->lengths[ind] = wire->length;
	wire->length += d;
	wire->num +=  1;
}

int part1(Wire *wires)
{
	int i, j;
	Vector inter;
	int min = INT_MAX;
	int temp;
	Wire *a = wires;
	Wire *b = wires+1;

	for(i=0; i<a->num; i++) {
		for(j=0; j<b->num; j++) {
			//printf("%d %d %d %d\n", i, a->num, a->edges[i].direction.x, a->edges[i].direction.y);
			//printf("%d %d %d %d\n", j, b->num, b->edges[j].direction.x, b->edges[j].direction.y);
			inter = intersection(&(a->edges[i]), &(b->edges[j]));
			temp = manhattan(&inter);
			//printf("temp: %d\n", temp);
			if(temp && temp < min) {
				min = temp;
			}
		}
	}
	return min;
}


int main(int argc, char **argv)
{
	static Wire wires[2];
	int d;
	char c;
	int w = 0;

	Wire *wire = wires;
	wire->length = 0;
	wire->num = 0;
	while(scanf("%c%d,", &c, &d) != EOF) {
		if(c == '\n') {
			if(w++ == 1) {
				break;
			}
			wire += 1;
			wire->length = 0;
			wire->num = 0;
			continue;
		}
		walk(c, d, wire);
	}

	printf("part1: %d\n", part1(wires));
	//printf("part2: %d\n", part2(map));

	return 0;
}
