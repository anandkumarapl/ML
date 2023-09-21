class Student:
    def __init__(self, rollno=None, name=None) -> None:
       if rollno is None:
           self.rollno=int(input("Roll no"))
       else:
           self.rollno=rollno

           if name is None:
               self.name=(input("Nmae"))
           else:
               self.name=name

    def __str__(self) -> str:
        return "Rollno={0}, Name={1}".format(self.rollno, self.name)
