class Student:
	def __init__(self, name, correct, submit):
		self.name = name
		self.correct = correct
		self.submit = submit
	


	def __str__(self):
		return f"{self.name} {self.correct} {self.submit}"
	
	def __repr__(self):
		return f"{self.name} {self.correct} {self.submit}"

a = []
for nTest in range(int(input())):
	name = input()
	c, s = map(int, input().split())
	a.append(Student(name, c, s))
a.sort( key= lambda x: (-x.correct, x.submit, x.name))
for i in a:
	print(i)

