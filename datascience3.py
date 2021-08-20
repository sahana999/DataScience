'''import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
ct=['INDIA','USA','UK']
pop=[1.35,1.80,1]
y=np.arange(len(ct))
plt.barh(y,pop)
plt.xticks(y,ct)
plt.title('pop chart')
plt.show()'''

'''import matplotlib.pyplot as plt
x=[2,4,6,8]
y=[32,65,76,90]
plt.scatter(x,y)
plt.show()
'''
'''import matplotlib.pyplot as plt
ages=[32,65,23,18,19,45,65,54,51,31]
plt.hist(ages,bins=5)
plt.show()'''

'''import matplotlib.pyplot as plt
labels=['UK','MP','DELHI','UTTARPRADESH']
lit=[25,35,45,65]

col=['green','red','yellow','blue']
e=(0,0,0,0.1)
plt.pie(lit,explode=e,labels=labels)
plt.show()'''

''' import pandas as pd
data={'year':[1971,1981,1991,2001,2011],
      'pop':[50,72,81,98,111]}
df=pd.DataFrame(data,columns=['year','pop'])
df.plot(x='year',y='pop',kind='line') '''

'''
................
import pandas as pd
data={'country':['us','uk','um'],
      'gdp':[5,9,8]}
df=pd.DataFrame(data,columns=['country','gdp'])
df.plot(x='country',y='gdp',kind='bar')
.........
'''
'''import matplotlib.pyplot as plt
sem1=[1,3,5]
m1=[34,90,65]
sem2=[2,4,6]
m2=[43,76,51]
plt.bar(sem1,m1,color='r')
plt.bar(sem1,m2,color='b')
plt.title("Bar Chart")
plt.show()
......................'''

'''import matplotlib.pyplot as plt
sem=[1,2,3]
m1=[34,90,65]
m2=[54,76,43]
m3=[78,100,89]
plt.plot(sem,m1,label='Raj')
plt.plot(sem,m2,label='Ravan')
plt.plot(sem,m3,label='Rani')
plt.legend()

plt.xlabel("sem")
plt.ylabel("marks")
plt.show()..............'''

import matplotlib.pyplot as plt
import pandas as pd
d={'empno':[121,122,123],
   'name':['priya','sana','raji'],
   'salary':[30000,70000,67777]}
df=pd.DataFrame(d)
print(d)
df['tax']=df['salary']*0.30
plt.bar(df['name'],df['salary'])





