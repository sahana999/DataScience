class Employee:
    empno=0
    salary=0
    grade=''
    def get(self,a,b):
        self.empno=a
        self.salary=b
    def check(self):
        if self.salary>=30000:
            self.grade='A'
        else:
            self.grade='B'
            
    def show(self):
       self.check()
       print( self.empno)
       print(self.grade)
    
e=Employee()
e.get(103,39857878)
e.show()