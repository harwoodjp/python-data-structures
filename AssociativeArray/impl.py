class Pair(object):
	def __init__(self, key=None, value=None):
		self.key = key
		self.value = value

class AssociativeArray(object):
	def __init__(self):
		self.pairs = []

	def delete(self, key):
		if self.find(key):
			self.pairs.remove(self.find(key))

	def find(self, key): 
		for pair in self.pairs:
			if pair.key == key:
				return pair
	
	def lookup(self, key):
		if self.find(key):
			return self.find(key).value

	def print(self):
		for pair in self.pairs:
			print(str(pair.key) + " => " + str(pair.value))

	def put(self, key, value):
		if self.find(key):
			self.find(key).value = value
		else:
			self.pairs.append(Pair(key, value))