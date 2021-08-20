class A:
    def hello(self):
        print("Hello")
        print('parent')
class B():
    def sum(self,a,b):
        print('sum is..',(a+b))
class C(A,B):
    def Hi(self):
        print('hi C')
    def __str__(self):
        return "My A class"
obj=C()
print(obj)