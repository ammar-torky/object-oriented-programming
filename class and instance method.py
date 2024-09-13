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

print("-" * 40  , '\n')
ob2.info_about_person()
print()
ob2.info_about_student(ob2)
print()
