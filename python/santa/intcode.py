from collections import deque


class IntCode:
    class Halt(Exception):
        pass
    
    class NotEnoughInput(Exception):
        pass
    
    class NotEnoughOutput(Exception):
        pass
    
    class EnoughOutput(Exception):
        pass
    
    class TooMuchOutput(Exception):
        pass
    
    def __init__(self, code, input=[]):
        self._mem = list(code)
        self._ip = 0
        self._rb = 0
        self._in = deque(input)
        self._out = deque()
    
    def copy(self):
        ic = IntCode(self._mem)
        ic._ip = self._ip
        ic._rb = self._rb
        ic._in = self._in.copy()
        ic._out = self._out.copy()
        return ic
    
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
        return self[self._ip] % 100 == 99
    
    def push(self, value):
        self._in.append(value)
    
    def pop(self, n=None):
        if n is None:
            if not self._out:
                raise self.NotEnoughOutput()
            else:
                return self._out.popleft()
        else:
            if len(self._out) < n:
                raise self.NotEnoughOutput()
            else:
                return [self._out.popleft() for _ in range(n)]
    
    def output(self):
        return list(self._out)
    
    def run(self, *_, fail=(), stop=(), ignore=(), output=None, ascii=False):
        while True:
            try:
                if output is not None:
                    if len(self._out) == output:
                        raise self.EnoughOutput()
                    elif len(self._out) > output:
                        raise self.TooMuchOutput()
                self.step()
            except self.NotEnoughInput:
                raise
            except fail:
                raise
            except stop:
                return
            except self.Halt:
                return
            except ignore:
                continue
            except self.EnoughOutput:
                return
            except self.TooMuchOutput:
                raise
    
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
        try:
            v = int(self._in.popleft())
        except IndexError:
            raise self.NotEnoughInput()
        else:
            self[dst_ptr] = v
            self._ip += 2
        
    def _put(self, v_ptr):
        v = self[v_ptr]
        self._out.append(v)
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
        raise self.Halt()
