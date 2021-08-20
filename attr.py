class Employee:
    empno=101
    salary=21000
    grade='A'
obj=Employee()
print(hasattr(obj,'empno'))
print(getattr(obj,'salary'))
delattr(obj,'empno')
print(getattr(obj,'empno'))

