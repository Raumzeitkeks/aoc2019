from collections import defaultdict

class OrbitMap:
    def __init__(self):
        self._orbits = defaultdict(set)
        
    def add_orbit(self, center, satellite):
        self._orbits[center].add(satellite)
        
    def checksum(self):
        seen = [("COM", 0)]
        checksum = 0
        for center, dist in seen:
            seen.extend((sat, dist+1) for sat in self._orbits[center])
            checksum += dist
        return checksum
    