import heartrate

heartrate.trace(browser=True)

class Employee():
    def __init__(self,fname,lname,loc):
        self.first = fname
        self.last = lname
        self.email = fname + '.' + lname + '@fifa.com'
        self.location = loc

    def fullName(self):
        return f'{self.first} {self.last}'

    def placeHolder(self,arg,pos):
        if pos.lower() == 'pre':
            return f'{arg} {self.location}'
        else:
            return f'{self.location} {arg}'


emp1 = Employee('Raj','Aryan','Barcelona')

print(emp1.email)
print(emp1.fullName())
print(emp1.placeHolder('FC','Pre'))

def employer(first,last,location = 'Barcelona'):
    return f'Hi this is {first} {last} from {location}.'

print(employer(last='Mehra',first='Rohit'))




