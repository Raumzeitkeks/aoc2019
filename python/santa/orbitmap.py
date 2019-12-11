from collections import defaultdict

class OrbitMap:
    def __init__(self, orbits=[]):
        self._fwd = defaultdict(set)
        self._bwd = dict()
        self.add_orbits(orbits)
        
    def add_orbit(self, orbit, *args):
        if args:
            self.add_orbit([orbit, *args])
        elif isinstance(orbit, str):
            self.add_orbit(orbit.split(")"))
        else:
            center, *satellites = orbit
            for sat in satellites:
                self._fwd[center].add(sat)
                self._bwd[sat] = center
    
    def add_orbits(self, orbits):
        for orbit in orbits:
            self.add_orbit(orbit)
            
    def objects(self):
        return set(self._fwd)
    
    def center(self, satellite):
        return self._bwd.get(satellite, None)
    
    def satellites(self, center):
        return self._fwd[center].copy()
    
    def ok(self):
        seen = set()
        todo = {"COM"}
        while todo:
            obj = todo.pop()
            if obj in seen:
                print("err:", obj)
                return False
            seen.add(obj)
            todo.update(self.satellites(obj))
        return seen == self.objects()
    
    def checksum(self):
        checksum = 0
        todo = set(["COM"])
        distance = 0
        while todo:
            checksum += distance * len(todo)
            todo_next = set()
            for obj in todo:
                todo_next.update(self.satellites(obj))
            todo = todo_next
            distance += 1
        return checksum
    
    def com_path(self, obj):
        path = [obj]
        while obj != "COM":
            obj = self.center(obj)
            path.append(obj)
        return list(reversed(path))
    
    def path(self, obj1, obj2):
        path1 = self.com_path(obj1)
        path2 = self.com_path(obj2)
        i = sum(1 for a, b in zip(path1, path2) if a == b)
        return list(reversed(path1[i:])) + path2[i-1:]
    
    def transfers(self, center1, center2):
        return len(self.path(center1, center2)) - 1
    