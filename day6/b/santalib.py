from collections import defaultdict

class OrbitMap:
    def __init__(self):
        self._orbits = defaultdict(set)
        
    def add_orbit(self, center, satellite):
        self._orbits[center].add(satellite)
        
    def transits_to_santa(self):
        seen = [("COM", [])]
        hist_you = None
        hist_san = None
        for center, hist in seen:
            seen.extend((sat, hist+[center]) for sat in self._orbits[center])
            if center == "YOU":
                hist_you = hist
            elif center == "SAN":
                hist_san = hist
        dist_you = len(hist_you)
        dist_san = len(hist_san)
        dist_common = -1 + sum(1 for obj1, obj2 in zip(hist_you, hist_san) if obj1 == obj2)
        dist = dist_you - 1 + dist_san - 1 - 2*dist_common
        return dist
    