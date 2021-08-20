class Employee:
    empni=0
    salary=0
    grade=''
    def __init__(self,a,b,c):
        self.empno=a
        self.salary=b
        self.grade=c
        print('constructor called')
        
    def show(self):
        print(self.empno)
        print(self.salary)
        print(self.grade)
    def __del__(self):
        print("destructor call")
        
e=Employee(139,40000,'A')
e.show()
    