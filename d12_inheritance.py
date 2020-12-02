# Description: https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    
    def calculate(self):
        avg_score = sum(self.scores) / len(self.scores)
        if avg_score >= 90:
            return 'O'
        if avg_score >= 80:
            return 'E'
        if avg_score >= 70:
            return 'A'
        if avg_score >= 55:
            return 'P'
        if avg_score >= 40:
            return 'D'
        return 'T'


firstName, lastName, idNum  = input().split()
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())