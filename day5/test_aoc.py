import santalib as santa 

def no_output():
    assert False, "Unexpected output"

def test_aoc_examples():
    examples = [
        ([1002,4,3,4,33], [1002,4,3,4,99], [], no_output),
        ([1101,100,-1,4,0], [1101,100,-1,4,99], [], no_output)
        ]
    for before, after, input, output in examples:
        ic = santa.IntCode(before, input, output)
        ic.run()
        assert ic.dump() == after
        