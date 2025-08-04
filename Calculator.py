class Calculator:
     def __init__(self,number1,number2):
          self.number2=number2
          self.number1=number1

     def add(self):
          answer=self.number1 +self.number2
          return answer
     def subtract(self):
          answer=self.number1 -self.number2
          return answer
     def multiply(self):
          answer=self.number1 *self.number2
          return answer
     def divide(self):
          answer=self.number1//self.number2
          return answer
