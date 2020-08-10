class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self,firstName, lastName,id,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.scores=scores
        self.grade = ''


    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.id)
        
    def calculate(self):
        sum=0
        for i in range(len(self.scores)):
            sum +=self.scores[i]
        avg=sum//len(self.scores)
        
        if avg >= 90 and avg <= 100:
            self.grade = 'O'
        elif avg >= 80 and avg < 90:
            self.grade = 'E'
        elif avg >= 70 and avg < 80:
            self.grade = 'A'
        elif avg >= 55 and avg < 70:
            self.grade = 'P'
        elif avg >= 40 and avg < 55:
            self.grade = 'D'
        else: 
            self.grade = 'T'
        
        return self.grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())