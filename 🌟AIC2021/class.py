import re

class Birthday:
	def __init__(self, name, birthday):
		self.name = name
		self.birthday = re.split('-',birthday)[0]
	def score(self):
		age = 2020 - int(self.birthday)
		print(self.name + '은' + age)