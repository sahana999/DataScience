import pymysql
#step1

d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

#step2
cur=d.cursor()
a=int(input("enter empno"))
b=input("enter name")
c=input('Enter city')
dd=int(input('enter salary'))

#step3
sql="insert into employee values(%d,'%s','%s',%d)"(a,b,c,dd);

#step4
cur.execute(sql)
print('Records saved ')
d.commit()


d.close()

'''import matplotlib.pyplot as plt
import pandas as pd
import pymysql
#step1
d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step2
cur=d.cursor()
#step3
sql="select * from employee";
#step4
cur.execute(sql)
data=cur.fetchall()
a=[]
b=[]
for res in data:
    a.append(res[0])
    b.append(res[1])
plt.bar(a,b)
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()
d.close()''''

