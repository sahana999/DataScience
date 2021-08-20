empno=int(input('Enter empno'))
name=input('Enter name')
empno=input('Enter empno')


filename=input('enter filename')
obj=open(filename,'w')

obj.write(str(empno)+'\n')
obj.write(name)


print('Data saved')

obj.close()
