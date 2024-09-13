from abc import ABC, abstractmethod
class Yasser(ABC) :
    family = "Torky"
    gender = 'Man'
    def __init__(self,name,age,field) -> None:
        self.name = name
        self.age = age
        self.field = field
    
    @abstractmethod    
    def get_Full_info(self):
        return f"Name: {self.name}, Age: {self.age}, Field: {self.field}, gender :{self.gender}"

class Nour(Yasser):
    def __init__(self, name, age, field) -> None:
        super().__init__(name, age, field)
    def get_Full_info(self):
        First = super().get_Full_info()
        return f"{First} \nsecond iam a heart doctor"


class Motaz(Yasser):
    def __init__(self, name, age, field) -> None:
        super().__init__(name, age, field)
    def get_Full_info(self):
        First = super().get_Full_info()
        return f"{First} \nsecond iam a Full Stack developer"


class Ammar(Yasser):
    def __init__(self, name, age, field) -> None:
        super().__init__(name, age, field)
    def get_Full_info(self):
        First = super().get_Full_info()
        return f"{First} \nsecond iam a Cloud Engineer"

class Lara_Lein(Nour):
    def __init__(self, name, age, field) -> None:
        super().__init__(name, age, field)
        self.gender = "Woman"  # تغيير الـgender لهذا الكائن فقط
    
    def get_Full_info(self):
        First = super().get_Full_info()
        return f"{First} \nsecond I am just a baby"

        
ob1 = Nour("Nour",28,"Medicine")
ob2 = Motaz("Motaz",28,"Full Stack")
ob3 = Ammar("Ammar",28,"Cloud Engineer")
ob4 = Lara_Lein("Lara_lein",1.5,"baby")

print(ob1.get_Full_info(),"\n",30*"-","\n")
print(ob2.get_Full_info(),"\n",30*"-","\n")
print(ob3.get_Full_info(),"\n",30*"-","\n")
print(ob4.get_Full_info(),"\n",30*"-","\n")
