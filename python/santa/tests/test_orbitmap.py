from santa.orbitmap import OrbitMap

def test_checksum():
    orbits = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
    uom = OrbitMap(orbits)
    assert uom.ok()
    assert uom.checksum() == 42
        
def test_transits():
    ex = [(["COM)SAN", "COM)YOU"], 0),
          (["COM)SAN", "SAN)YOU"], 1),
          (["COM)YOU", "YOU)SAN"], 1),
          (["COM)I", "I)SAN", "COM)YOU"], 1),
          (["COM)I", "I)YOU", "COM)SAN"], 1),
          (["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"], 4)]
    for orbits, transfers in ex:
        print(orbits)
        uom = OrbitMap(orbits)
        assert uom.ok()
        assert uom.transfers(uom.center("YOU"), uom.center("SAN")) == transfers
        