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


