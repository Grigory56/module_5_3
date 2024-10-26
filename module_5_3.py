class House:
    def __init__(self,name ,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or new_floor <1:
            print('"Такого этажа не существует"')
        else:

            for i in range(new_floor):
                print (i+1)

    def __len__(self):
        s=self.number_of_floors
        return s
    def __str__(self):
        s='Название: '+ str(self.name) + ", кол-во этажей: "+str(self.number_of_floors)
        return s  # 'Название: ',self.name, ", кол-во этажей: ", self.number_of_floors

    def __eq__(self, other):

        if isinstance(other, House):
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors == other:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other, House):
            if self.number_of_floors != other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors != other:
                return True
            else:
                return False
    def __lt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors < other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors < other:
                return True
            else:
                return False
    def __le__(self, other):
        if isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors:
                return True
            else:
                return False
        #
    def __gt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors > other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors > other:
                return True
            else:
                return False
    def __ge__(self, other):
        if isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors >= other:
                return True
            else:
                return False

    def __add__(self, value):
        if isinstance(value,int):

            self.number_of_floors +=  value

        return self

    def __iadd__(self, value):
        if isinstance(value,int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value,int):
            self.number_of_floors = value + self.number_of_floors
            return self

h1= House('ЖК Эльбрус', 10)
h2= House('ЖК Акация', 20)
# print(type(h1.number_of_floors))
# print(type(h2.number_of_floors))
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__