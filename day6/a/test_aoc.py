import santalib as santa 

def test_aoc_examples():
    data = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
    uom = santa.OrbitMap()
    for orbit in data:
        center, satellit = orbit.split(")")
        uom.add_orbit(center, satellit)
    assert uom.checksum() == 42
        