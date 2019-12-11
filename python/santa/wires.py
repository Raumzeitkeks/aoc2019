import itertools as itt

def norm(coord):
    return sum(abs(x) for x in coord)

class Wire:
    def __init__(self, description):
        x, y = 0, 0
        self._trace = [(0, 0)]
        for instruction in description:
            direction = instruction[0]
            distance = int(instruction[1:])
            if direction == "U":
                self._trace.extend((x, y+i+1) for i in range(distance))
                y += distance
            elif direction == "D":
                self._trace.extend((x, y-i-1) for i in range(distance))
                y -= distance
            elif direction == "L":
                self._trace.extend((x-i-1, y) for i in range(distance))
                x -= distance
            elif direction == "R":
                self._trace.extend((x+i+1, y) for i in range(distance))
                x += distance
            else:
                raise Exception("Unknown direction")
                
    def trace(self):
        return self._trace.copy()
            
    def intersect(self, other):
        return set(self.trace()).intersection(other.trace()) - {(0, 0)}

    def walk(self, coord):
        path = itt.takewhile(lambda c: c != coord, self.trace())
        return list(path) + [coord] if coord in self.trace() else None