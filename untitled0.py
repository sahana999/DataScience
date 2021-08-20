import pymysql
#step1

d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

#step2
cur=d.cursor()
a=int(input("enter empno"))
sql="select * from employee"
data=cur.fetchall()
f=0
for res in data:
   if(res[0]==a):
     print("already present")
     f=1
     break
   else:
      sql1="insert into employee values(%d)"(a)
      m=cur.execute(sql1)
      print(m)
d.close()