#!/usr/bin/env python3

import fileinput


class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __add__(self, other):
        return self.add(other)
    
    def sub(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __sub__(self, other):
        return self.sub(other)
    
    def eq(self, other):
        return self.x == other.x and self.y == other.y
    
    def magnitude(self):
        return int(round((self.x**2 + self.y**2)**0.5))
    
    def normed(self):
        return Vector(self.x // self.magnitude(), self.y // self.magnitude())
    
    def __eq__(self, other):
        return self.eq(other)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def scalar(self, other):
        return self.x * other.x + self.y * other.y
    
    def __matmul__(self, other):
        return self.scalar(other)
    
    def mul(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        return Vector(self.x * other, self.y * other)
    
    def __mul__(self, other):
        return self.mul(other)
    
    def manhattan(self):
        return abs(self.x) + abs(self.y)
        
    @classmethod
    def from_direction(cls, direction, length):
        new = cls(*{
            'L': (-length, 0),
            'R': (length, 0),
            'U': (0, length),
            'D': (0, -length)
        }[direction])
        return new     
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    

class Edge:
    
    def __init__(self, origin=Vector(), direction=Vector()):
        self.origin = origin
        self.direction = direction
        
    def intersection(self, other):
        so = self.origin
        sd = self.direction
        sdn = self.direction.normed()
        oo = other.origin
        od = other.direction
        odn = other.direction.normed()
        
        if sdn @ odn != 0 or so == oo:
            return None
        
        if sdn.y == 0: # x, y case
            v = (oo.x - so.x) // sdn.x
            w = (so.y - oo.y) // odn.y
        else: # y, x case
            v = (oo.y - so.y) // sdn.y
            w = (so.x - oo.x) // odn.x
            
        if v < 0 or w < 0 or v > sd.magnitude() or w > od.magnitude():
            return None
        else:
            return so + sdn * v

    def __str__(self):
        return f'Edge ({self.origin} + {self.direction}'

class Wire:
    
    def __init__(self):
        self.edges = []
        
    def walk(self, direction, length):
        if not self.edges:
            origin = Vector()
        else:
            origin = self.edges[-1].origin + self.edges[-1].direction
        dirvec = Vector.from_direction(direction, length)
        self.edges.append(Edge(origin, dirvec))
        
    def __str__(self):
        s = 'Wire: '
        s += ' '.join(str(x) for x in self.edges)
        return s
    
    def __iter__(self):
        return iter(self.edges)
        

def part1(wires):
    min_inter = None
    for i in wires[0]:
        for j in wires[1]:
            inter = i.intersection(j)
            if inter is not None:
                if min_inter is None:
                    min_inter = inter.manhattan()
                else:
                    min_inter = min_inter if min_inter < inter.manhattan() else inter.manhattan()
    return min_inter

def part2(wires):
    min_length = None
    i_length = 0
    for i in wires[0]:
        j_length = 0
        for j in wires[1]:
            inter = i.intersection(j)
            if inter is not None:
                new_length = i_length + j_length + (inter-i.origin).magnitude() + (inter-j.origin).magnitude()
                if min_length is None:
                    min_length = new_length
                else:
                    min_length = min_length if min_length < new_length else new_length
            j_length += j.direction.magnitude()
        i_length += i.direction.magnitude()
    return min_length
                    

def main():
    wires = []
    for line in fileinput.input():
        w = Wire()
        ls = line.split(',')
        for vec in ls:
            vec = vec.strip()
            w.walk(vec[0], int(vec[1:]))
        wires.append(w)
        
    print('part1: {}'.format(part1(wires)))
    print('part2: {}'.format(part2(wires)))
    

if __name__ == '__main__':
    main()
    
    