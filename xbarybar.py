import matplotlib.pyplot as plt
import numpy as num

x=[1,2,3,4,5,6,7,8,9,10]
TestScore=[40,70,50,60,80,50,90,40,60,60]
sales=[2.5,6.0,4.5,5.0,4.5,2.0,5.5,3.0,4.5,3.0]
total=0
testScores=0
test_Scores=0
for i in TestScore :
    total+=i
print("Total=",total)
avg=total/len(TestScore)
print("Min=",avg)
print()

for i in sales:
 testScores+=i
avgs=testScores/len(sales)
print("Average=",avgs)
print()

dx=[]
for i in TestScore:
   dx.append(i-avg)
print("x min=",dx)   
print()

dy=[]
for i in sales:
   dy.append(i-avgs)
print("y min=",dy) 
print()

dx_dy=[]
dx__dy=0
for i in range (len(dx)):
   dx_dy.append(dx[i]*dy[i])
print("dx_dy=",dx_dy)
print()
for i in dx_dy:
   dx__dy=dx__dy+i
print("dx__dy=",dx__dy)
print()

dx_x=[]
dx__x=0
for i in range(len(dx)):
   dx_x.append(dx[i]*dx[i])
print("dx_x=",dx_x)
for i in dx_x:
   dx__x=dx__x+i
print("dx__x=",dx__x)

print()

dy_y=[]
dy__y=0
for i in range(len(dy)):
   dy_y.append(dy[i]*dy[i])
print("dx_y=",dy_y)
print()
for i in dy_y:
   dy__y=dy__y+i
print("dy__y=",dy__y)
plt.show()