class Currency:
    def __next__(self):
        n=self.counter=0
        self.counter+=1 
        if self.counter>2:
            raise StopIteration
        if n==0:
         return self.pad0(self.total)
        return self.pad0(self.total)
    def __iter__(self):
       self.counter=0
       return self
    def pad0(self,n):
       if n<10:
          return"0{0}".format(n)
       return"{0}".format(n)
    def __init__(self,n):
       if n<10:
          return "0{0}".format(n)
       return"{0}".format(n)
    def __init__(self, rs, paise):  # Constructor. Converts rs and paise to a total in paise and stores
        self.total = rs * 100 + paise

    def __str__(self):  # str function converts total to rupee and paise
        r = self.total // 100
        p = self.total % 100
        r = self.pad0(r)
        p = self.pad0(p)
        return "₹ {0}.{1}".format(r, p)

    def __add__(self, other):  # Implements the + operator
        return Currency(0, self.total + other.total)

    def __gt__(self, other):  # Implements the > operator
        return self.total > other.total

    def __le__(self, other):
        return self.total <= other.total

    def __getitem__(self, item):
        if item == 0:
            return self.pad0(self.total // 100)
        if item == 1:
            return self.pad0(self.total % 100)
        raise IndexError("list index out of range")

    def __len__(self):  # This is for a loop through sequence.We have two items rupees and paise
        return 2
c1 = Currency(1, 12)
print("C1 ", c1)
for i in c1:
    print(i)
    break
c2 = Currency(2, -90)
print("C2 ", c2)
print("0", c2[0])
print("1", c2[1])
print(c1 <= c2)