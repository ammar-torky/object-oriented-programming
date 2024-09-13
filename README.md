# Resources:
## [OOP in Arabic - #0 Introduction (youtube.com)](https://www.youtube.com/playlist?list=PLwWuxCLlF_ue7GPvoG_Ko1x43tZw5cz9v)
## [Python Object Oriented Programming - شرح للبرمجة كائنية التوجه في بايثون - YouTube](https://www.youtube.com/watch?v=A9kSngn7254&t=6633s)

<h1 align="center">
  --- Explanation ---
  <br>
</h1>

#  Constructor :
- الattributes  الخاصة بالكونستركتور بتكون داخل الكونستركتور واسمها  instance attributes اما ف نوع تاني اسمه class attributes ودي اللي بتبقي خارج الكونستركتور لو تفتكتر فال ++c كنا بنعرفها داخل الprivate access modifier 
- # Attributes:
	- instance attributes :
		- خاصة بكل أوبجكت عن التاني 
		- بتتعرف داخل الكونستركتور 
	- class attributes :
		- عامة علي اي اوبجكت يتم تعريفه من الكلاس 
		- بتتعرف خارج الكونستركتور 
#instance_attributes
```python
class human :
    def __init__(self , first_name ,last_name , age):# this is the consturctor
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person1 = human('Ammar','Yasser',21) # take object from class human with these attributes
person2 = human('mostafa','Gad',21)
```

#class_attributes
```python
class FCI_Student:
    faculity = 'FCI_MU'
    grade = "grade 3"

    def __init__(self,name,age,gen):
        self.name = name
        self.age = age
        self.gender = gen

    def full_info(self):
        print(f'faculity is : {FCI_Student.faculity}')
        print(f'Grade is : {FCI_Student.grade}')
        print(f'name is : {self.name} ')
        print(f'Age is : {self.age}')
        print(f'gender is : {self.gender}')

student1 = FCI_Student('Ammar',21,'Male')
student1.full_info()

print('-' * 40)

student2 = FCI_Student('Ahmed',21,'Male')
student2.full_info()
##############################
"""           
     output:
     
faculity is : FCI_MU
Grade is : grade 3
name is : Ammar 
Age is : 21
gender is : Male
----------------------------------------
faculity is : FCI_MU
Grade is : grade 3
name is : Ahmed
Age is : 21
gender is : Male

"""

```


---
#  define a instance method() :
#instance_method
- أول متغير هو ال self وبيشاور عالاوبجكت اللي هتنسخه من الكلاس 
```python
class human :
    def __init__(self , first_name ,last_name , age):# this is the consturctor
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def info_function(self):
	    return f'Hello,{self.first_name} {self.last_name} ...your age is {self.age}'
#self refer to to object data
person1 = human('Ammar','Yasser',21) # take object from class human with these attributes
print(person1.info_function())
##############################
##############################
#          ouput
# Hello, Ammar Yasser ...your age is 21
```

# define a class method() :
#class_method

- أول متغير بيتحط هو ال cls لانه بيشاور عالكلاس نفسه 
- بتحط قبلها decorator اسمه classmethod@ 
- python doesn’t support method overloading like c++ or java so we use class methods to create factory methods.

# define a static method() :
#static_method

- مبتحطش فيها لا cls ولا self 
- تستخدم في حالة انك عايز تعمل حاجة بسيطة فالكلاس بدون انك تأكسس الكلاس ولا instance
- بتحط قبلها decorator اسمه staticmethod@
- In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
- من الاخر كدا هي زي  اي فنكشن عادية بتنكتب برا الكلاس بس اول ما بتنكتب جو الكلاس لاستخدام بسيط مثلا  بييبقي اسمها كدا
Examples on both
```python
# class
class Third_year_Students :
    faculity = 'FCI'
    grade = 'Grade 3'

    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def info_about_person(self):
        print(f"name :{self.name} \nage : {self.age} \ngender :{self.gender}")

    @classmethod    
    def info_about_student(cls,obj):
        print(f"faculity : {cls.faculity} \ngrade : {cls.grade}")
        obj.info_about_person()

ob1 = Third_year_Students('Ammar',21,'Male')
ob2 = Third_year_Students('Mohamed',21,'Male')


ob1.info_about_person()
print()
ob1.info_about_student(ob1)
print()

print("-" * 40  , '\n')

ob2.info_about_person()
print()
ob2.info_about_student(ob2)
print()

```

# Magic(Dunder) Method
#dunder #magic_method #magic

- الكود موضح كل حاجة 
```python
# magic Method
# magic Method
class Skills:
    def __init__(self,skills) -> None:
        self.skills = skills
        
    def __str__(self) -> str:
        return f"my primary skills is {self.skills}"
    
    def __repr__(self) -> str:
       return f"objct = Skills(here pass your list skills)"
   
    def __bool__(self)->bool:
        return len(self.skills) > 0
    
# add used to if you wanna add in this way ( object + "item1" ) 
    def __add__(self,item):
        new_skills = self.skills.copy()
        new_skills.append(item)
        return Skills(new_skills) # Return new ojbect 
    # هنا العملية دي علشان احافظ علي اللستة الاصلية كما هي بدون التعديل فيها 
    
    # لو عايز تعدل علي الاوبجكت بطريقة 
    # x = 5 --------------- x += 5 ------------- then x = 10 
    def __iadd__(self, item):
        self.skills.append(item)
        return self

# to make operator overloading on ( * , / , - ) you will find __mul__ , __div__ , __sub__ 
# same idea if you add "i" before name (iadd, imul , idiv , isub) then you mean x *= value and so on 

# radd used to if you wanna add in this way ("item1" + object) 
    def __radd__(self, item):
        new_skills = self.skills.copy()
        new_skills.insert(0, item)
        return Skills(new_skills)

# if you wanna print item of list of object using indexing way like this ----> print(ob[0])
    def __getitem__(self, index):
        return self.skills[index]
    
    def __setitem__(self,index,value):
        self.skills[index] = value
        


    
ob1 = Skills(['Git & GitHub','Linux','Python'])
print("my new skills is  : ",(ob1+"jenkins").skills)
print(ob1)


# Test on line 25 ----------- __iadd__ dunder method
ob1 += "Kubernetes"
print(ob1)

# Test on line 33 ----------- __radd__ dunder method
ob1 = "Docker" + ob1
print(ob1)

# Test on line 39 ----------- __getitem__ dunder method
ob1[0] = "git & gitlab"
print(ob1)




![[Pasted image 20240818082756.png#center|500 ]]
# inheritance 
```python
class Animal :
    type = "elzoahef الزواحف "
    def __init__(self,name) -> None:
        self.name = name
    def __str__(self) -> str:
        return f'name is {self.name}'

class corocodile(Animal) :
    def __init__(self,name,color,place,gender):
        super().__init__(name)
        self.color = color
        self.place = place
        self.gender = gender

    @classmethod    
    def get_all_info(self) :
        return f"type: {self.type} \nname : {self.name} \ncolor :{self.color} \nplace :{self.place} \
            \ngender :{self.gender} "

    def display_info(self):
        return f"type: {self.type} \nname : {self.name} \ncolor :{self.color} \nplace :{self.place} \

            \ngender :{self.gender} "
ob1 = corocodile("corocodile1","Green","America","Male")

print(ob1.display_info())
```

# Polymorphism 
- بكل بساطة الكلمة دي معناها اصلا تعدد الاوجه وهنا فالبايثون نقصد ان احنا هنمسك الدالة الموجودة فالكلاس الاب بنفس الاسم بس هنغير الbody بتاعها داخل الderived  class 
##  احلي مثال علي عيونك 
 ```python
 class Base:  
    def __init__(self, name ,age ) -> None:  
        self.name = name  
        self.age = age  
    def get_full_info(self):  
        return f"name is {self.name} \nage is {self.age}"  
 # here is derived class  
class Derived(Base):  
  
    def __init__(self,name,age,gender):  
        super().__init__(name,age)  
        self.gender = gender  
# here is override method man  
    def get_full_info(self):  
        old_return = super().get_ful_info()  
        return f"{old_return} \ngender is {self.gender}"
```

# Encapsulation
```python
"""  

Access Modifiers بص اصلا هو فالبايثون كدا مفيش فعليا حاجة اسمها كدا
protected , private هي بس طريقة فالكتابة بس فعليا هي مش شغالة وتقدر توصل لل 
من الخارج عادي بسهولة وهجربهالك تحت بردو 

"""  
  
# for pupblic acces modifiers
"""  
تقريبا اي حاجة استخدمناها قبل كدا كانت public
"""  
  
  
# for private access modifiers   
class Base:  
    def __init__(self, name) -> None:  
        self.__name = name  
        # setters  
  
    def set_name(self, new_name):  
        self.__name = new_name  
  
    # getters  
    def get_name(self):  
        return self.__name  
  
  
# Test 1  
ob1 = Base("Ammar")  
print(ob1.get_name())  
ob1.set_name("yasser")  
print(ob1.get_name())  
  
# Test 2 ---> how to Acces private outside the class print(ob1._Base__name)  
  
  
# for Protected Acces Modifiers class Base2:  
    def __init__(self, name, age) -> None:  
        self._name = name  # prtoected    
self._age = age  # protected  مسمي فقط يصحبي   
    def set_name(self, new_name):  
        self._name = new_name  
  
    def set_age(self, new_age):  
        self._age = new_age  
  
    def get_info(self):  
        return f"name is {self._name} \nage is {self._age}"  
  
  
class derived2(Base2):  
    def __init__(self, name, age, gender):  
        super().__init__(name, age)  
        self._gender = gender  
  
    def get_info(self):  
        old_return = super().get_info()  
        return f"{old_return} \ngender is {self._gender}"  
  
  
ob3 = derived2("Ammar", 21, "Male")  
print(ob3.get_info())  
# Test 3 on Accessability : 
print(ob3._name)  # هيطبع عادي 
print(ob3._age)  # كله شغال
```



# Abstraction
- أول حاجة علشان تستخدمه لازم تعمل `from abc import ABC,abstractmethod`
- هو اسمه الكلاس المجرد ودا ممكن تتخيله مثلا بالهيكل العظمي بتاع العربية ف مثال العربيات بتاعنا
- مينفعش تعمل منه اوبجكت لانه بديهيا مينفعش اطلع الهيكل العظمي بتاع العربية علي اساس انها اوبجكت (العربية)
- بيبقي جواه حاجة اسمها abstract method ودي لازم اي كلاس تاني يعمل منه inhertance يعملها override ويستخدمها هو 
## دا مثال مجممع الدنيا شوية : 
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    family = "Animalia"
    gender = 'Unknown'

    def __init__(self, name, age, species) -> None:
        self.name = name
        self.age = age
        self.species = species

    @abstractmethod
    def get_Full_info(self):
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}, Gender: {self.gender}"


class Lion(Animal):
    def __init__(self, name, age, species) -> None:
        super().__init__(name, age, species)
    
    def get_Full_info(self):
        First = super().get_Full_info()
        return f"{First} \nsecond I am the king of the jungle"

class Dolphin(Animal):
    def __init__(self, name, age, species) -> None:
        super().__init__(name, age, species)
    
    def get_Full_info(self):
        First = super().get_Full_info()
        return f"{First} \nsecond I am a smart sea creature"

class Elephant(Animal):
    def __init__(self, name, age, species) -> None:
        super().__init__(name, age, species)
    
    def get_Full_info(self):
        First = super().get_Full_info()
        return f"{First} \nsecond I am a gentle giant"


class BabyElephant(Elephant):
    def __init__(self, name, age, species) -> None:
        super().__init__(name, age, species)
        self.gender = "Female"  # تغيير الـgender لهذا الكائن فقط
    
    def get_Full_info(self):
        First = super().get_Full_info()
        return f"{First} \nsecond I am just a baby"

ob1 = Lion("Leo", 5, "Lion")
ob2 = Dolphin("Dolly", 3, "Dolphin")
ob3 = Elephant("Ellie", 10, "Elephant")
ob4 = BabyElephant("Ella", 1, "Baby Elephant")

print(ob1.get_Full_info(), "\n", 30*"-", "\n")
print(ob2.get_Full_info(), "\n", 30*"-", "\n")
print(ob3.get_Full_info(), "\n", 30*"-", "\n")
print(ob4.get_Full_info(), "\n", 30*"-", "\n")

```
---

