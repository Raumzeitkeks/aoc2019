
class IntCode:
    class HLT(Exception):
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
        except self.HLT:
            pass
    
    def step(self):
        m, ip = self._mem, self._ip
        xop = m[ip]
        op, pms = self._decode_xop(xop)
        params = [m[v] if pm == "P" else v for v, pm in zip(m[ip+1:], pms)]
        op(*params)
    
    def _decode_xop(self, xop):
        add = lambda v1, v2, d: self._op_add(v1, v2, d)
        mul = lambda v1, v2, d: self._op_mul(v1, v2, d)
        get = lambda d: self._op_get(d)
        put = lambda v: self._op_put(v)
        jit = lambda v, ip: self._op_jit(v, ip)
        jif = lambda v, ip: self._op_jif(v, ip)
        les = lambda v1, v2, d: self._op_les(v1, v2, d)
        equ = lambda v1, v2, d: self._op_equ(v1, v2, d)
        hlt = lambda : self._op_hlt()
        hcf = lambda : self._op_hcf("Invalid xop [{}]".format(xop))
        P, I, W, J = "PIWJ"
        lut = {   1: (add, (P, P, W)),
                101: (add, (I, P, W)),
               1001: (add, (P, I, W)),
               1101: (add, (I, I, W)),
                  2: (mul, (P, P, W)),
                102: (mul, (I, P, W)),
               1002: (mul, (P, I, W)),
               1102: (mul, (I, I, W)),
                  3: (get, (W)),
                  4: (put, (P)),
                104: (put, (I)),
                  5: (jit, (P, J)),
                105: (jit, (I, J)),
                  6: (jif, (P, J)),
                106: (jif, (I, J)),
                  7: (les, (P, P, W)),
                107: (les, (I, P, W)),
               1007: (les, (P, I, W)),
               1107: (les, (I, I, W)),
                  8: (equ, (P, P, W)),
                108: (equ, (I, P, W)),
               1008: (equ, (P, I, W)),
               1108: (equ, (I, I, W)),
                 99: (hlt, ())}
        return lut.get(xop, (hcf, ()))
        
    def _op_add(self, val1, val2, dest):
        self._mem[dest] = val1 + val2
        self._ip += 4
        
    def _op_mul(self, val1, val2, dest):
        self._mem[dest] = val1 * val2
        self._ip += 4
        
    def _op_get(self, dest):
        self._mem[dest] = next(self._in)
        self._ip += 2
        
    def _op_put(self, val):
        self._out(val)
        self._ip += 2
        
    def _op_jit(self, val, ip):
        self._ip = ip if val else self._ip + 3
            
    def _op_jif(self, val, ip):
        self._ip = ip if not val else self._ip + 3
        
    def _op_les(self, val1, val2, dest):
        self._mem[dest] = 1 if val1 < val2 else 0
        self._ip += 4
        
    def _op_equ(self, val1, val2, dest):
        self._mem[dest] = 1 if val1 == val2 else 0
        self._ip += 4
        
    def _op_hlt(self, *args):
        raise self.HLT(*args)
        
    def _op_hcf(self, *args):
        raise self.HCF(*args)
        