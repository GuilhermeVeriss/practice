# Solution day 12

class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
     
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    
    def calculate(self):
        s = 0
        for i in self.scores:
            s += i
        avar = s/len(self.scores)
        
        if avar < 40:
            return 'T'
        elif avar < 55:
            return 'D'
        elif avar < 70:
            return 'P'
        elif avar < 80:
            return 'A'
        elif avar < 90:
            return 'E'
        else:
            return 'O'

line = input().split()
