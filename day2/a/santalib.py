
class IntCode:
	class HCF(Exception):
		pass
	
	def __init__(self, intcode):
		self._ic = [int(x) for x in intcode]
		self._pc = 0
		
	def __getitem__(self, key):
		return self._ic[key]
		
	def step(self):
		op, a, b, c = self[self._pc : self._pc + 4]
		if self.halted():
			return
		elif op == 1:
			self._ic[c] = self[a] + self[b]
			self._pc += 4
		elif op == 2:
			self._ic[c] = self[a] * self[b]
			self._pc += 4
		else:
			raise self.HCF
			
	def halted(self):
		return (self[self._pc] == 99)
		
	def run(self):
		while not self.halted():
			self.step()
