
class IntCode:
    class Halt(Exception):
        pass
    
    class HCF(Exception):
        pass
    
    def __init__(self, intcode, input, output):
        self._mem = [int(x) for x in intcode]
        self._ip = 0
        self._in = iter(input)
        self._out = output

    def dump(self):
        return self._mem.copy()
    
    def halted(self):
        return self._mem[self._ip] == 99
        
    def run(self):
        try:
            while True:
                self.step()
        except self.Halt:
            pass
    
    def step(self):
        m, ip = self._mem, self._ip
        xop = m[ip]
        op, pms = self._decode_xop(xop)
        params = [m[v] if pm == "P" else v for v, pm in zip(m[ip+1:], pms)]
        op(*params)
    
    def _decode_xop(self, xop):
        P, I, W = "PIW"
        lut = {   1: (self._add,  (P, P, W)),
                101: (self._add,  (I, P, W)),
               1001: (self._add,  (P, I, W)),
               1101: (self._add,  (I, I, W)),
                  2: (self._mul,  (P, P, W)),
                102: (self._mul,  (I, P, W)),
               1002: (self._mul,  (P, I, W)),
               1102: (self._mul,  (I, I, W)),
                  3: (self._get,  (W)      ),
                  4: (self._put,  (P)      ),
                104: (self._put,  (I)      ),
                  5: (self._jnz,  (P, P)   ),
                105: (self._jnz,  (I, P)   ),
               1005: (self._jnz,  (P, I)   ),
               1105: (self._jnz,  (I, I)   ),
                  6: (self._jz,   (P, P)   ),
                106: (self._jz,   (I, P)   ),
               1006: (self._jz,   (P, I)   ),
               1106: (self._jz,   (I, I)   ),
                  7: (self._lt,   (P, P, W)),
                107: (self._lt,   (I, P, W)),
               1007: (self._lt,   (P, I, W)),
               1107: (self._lt,   (I, I, W)),
                  8: (self._eq,   (P, P, W)),
                108: (self._eq,   (I, P, W)),
               1008: (self._eq,   (P, I, W)),
               1108: (self._eq,   (I, I, W)),
                 99: (self._halt, ()       )}
        return lut.get(xop, (lambda: self._hcf(xop), ()))
        
    def _add(self, val1, val2, dest):
        self._mem[dest] = val1 + val2
        self._ip += 4
        
    def _mul(self, val1, val2, dest):
        self._mem[dest] = val1 * val2
        self._ip += 4
        
    def _get(self, dest):
        self._mem[dest] = next(self._in)
        self._ip += 2
        
    def _put(self, val):
        self._out(val)
        self._ip += 2
        
    def _jnz(self, val, addr):
        self._ip = addr if val != 0 else self._ip + 3
            
    def _jz(self, val, addr):
        self._ip = addr if val == 0 else self._ip + 3
        
    def _lt(self, val1, val2, dest):
        self._mem[dest] = 1 if val1 < val2 else 0
        self._ip += 4
        
    def _eq(self, val1, val2, dest):
        self._mem[dest] = 1 if val1 == val2 else 0
        self._ip += 4
        
    def _halt(self, *args):
        raise self.Halt(*args)
        
    def _hcf(self, *args):
        raise self.HCF(*args)
        