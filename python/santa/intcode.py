

class IntCode:
    class HLT(Exception):
        pass
    
    def __init__(self, code, input=None, output=None):
        self._mem = list(code)
        self._ip = 0
        self._rb = 0
        self._in = input
        self._out = output
    
    def __getitem__(self, key):
        try:
            return self._mem[key]
        except IndexError:
            return 0
    
    def __setitem__(self, key, value):
        try:
            self._mem[key] = value
        except IndexError:
            padding = [0] * (key - len(self._mem))
            self._mem = self._mem + padding + [value]
    
    def dump(self):
        return self._mem.copy()
    
    def halted(self):
        return self[self._ip] == 99
        
    def run(self):
        try:
            while True:
                self.step()
        except self.HLT:
            pass
    
    def step(self):
        m, ip, rb = self._mem, self._ip, self._rb
        xopc = m[ip]
        op, pmds = self._decode_xop(xopc)
        params = [self._decode_param(pmd, ip+1+i, m[ip+1+i], rb)
                  for i, pmd in enumerate(pmds)]
        op(self, *params)
    
    @staticmethod
    def _decode_xop(xopc):
        opc = xopc % 100
        lut = { 1: (IntCode._add, 3),
                2: (IntCode._mul, 3),
                3: (IntCode._get, 1),
                4: (IntCode._put, 1),
                5: (IntCode._jnz, 2),
                6: (IntCode._jz,  2),
                7: (IntCode._lt,  3),
                8: (IntCode._eq,  3),
                9: (IntCode._mrb, 1),
               99: (IntCode._hlt, 0)}
        op, n = lut[opc]
        pmds = [(xopc // 10**(i+2)) % 10 for i in range(n)]
        return op, pmds
    
    @staticmethod
    def _decode_param(pmd, paddr, v_ptr, rb):
        lut = {0: v_ptr,
               1: paddr,
               2: v_ptr + rb}
        return lut[pmd]
        
    def _add(self, v1_ptr, v2_ptr, dst_ptr):
        v1, v2 = self[v1_ptr], self[v2_ptr]
        self[dst_ptr] = v1 + v2
        self._ip += 4
        
    def _mul(self, v1_ptr, v2_ptr, dst_ptr):
        v1, v2 = self[v1_ptr], self[v2_ptr]
        self[dst_ptr] = v1 * v2
        self._ip += 4
        
    def _get(self, dst_ptr):
        self[dst_ptr] = self._in()
        self._ip += 2
        
    def _put(self, v_ptr):
        v = self[v_ptr]
        self._out(v)
        self._ip += 2
        
    def _jnz(self, v_ptr, jmp_addr_ptr):
        v, jmp_addr = self[v_ptr], self[jmp_addr_ptr]
        self._ip = jmp_addr if v != 0 else self._ip + 3
            
    def _jz(self, v_ptr, jmp_addr_ptr):
        v, jmp_addr = self[v_ptr], self[jmp_addr_ptr]
        self._ip = jmp_addr if v == 0 else self._ip + 3
        
    def _lt(self, v1_ptr, v2_ptr, dst_ptr):
        v1, v2 = self[v1_ptr], self[v2_ptr]
        self[dst_ptr] = 1 if v1 < v2 else 0
        self._ip += 4
        
    def _eq(self, v1_ptr, v2_ptr, dst_ptr):
        v1, v2 = self[v1_ptr], self[v2_ptr]
        self[dst_ptr] = 1 if v1 == v2 else 0
        self._ip += 4
        
    def _mrb(self, ofs_ptr):
        ofs = self[ofs_ptr]
        self._rb += ofs
        self._ip += 2
        
    def _hlt(self):
        raise self.HLT()


class Memory:
    def __init__(self, data=[]):
        assert all(isinstance(x, int) for x in data)
        self._data = list(data)
    
        
