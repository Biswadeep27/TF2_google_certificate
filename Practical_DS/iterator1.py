import sys

print(sys.version_info)
print(sys.version)

num = [1,2,3]

for n in num:
	print(n)


class Employee:
	'''A simple employee class'''
	def __init__(self,first,last):
		self.first = first
		self.last = last

	def display_model(self):
		return str(self.first) + " " + str(self.last)


	def factors(self,n):
		k = 1
		while k*k < n:
			if n%k == 0:
				yield k
				yield n//k
			k += 1
			if k*k == n:
				yield k


emp_obj = Employee('Raj','Aryan')

#gen_fact = emp_obj.factors(100)

i = 1
for f in emp_obj.factors(100):
    print(f'{f} is a factor.')
    print(f'iteration in loop: {i}')
    i += 1

