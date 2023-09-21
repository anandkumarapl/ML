import matplotlib.pyplot as plt
import numpy as np
from resultprocessing.student import Student
from resultprocessing.subject import Subject
from resultprocessing.menu import menu

results = {}
while True:
    print("0-Exit,1-Add,2-Search,3-Plot")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        st = Student()
        physics = Subject()
        chemistry = Subject()
        results[st.rollno] = [st, physics, chemistry]
        plt.plot(st, physics, chemistry)
        print("Added")
        continue
    if option == 2:
        rollno = int(input("Roll No"))
        data = results.get(rollno)
        if data is None:
            print("not found")
            continue
        print("Student", data[0])
        print("Subject 1", data[1])
        print("Subject 2", data[2])
    if option == 3:
        x = list(range(101))
        y = [x*x for x in x]
        plt.scatter(y,x,color="pink")
        plt.plot()
        plt.show()
