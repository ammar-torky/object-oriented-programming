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
    
    def get_all_info(self) :
        return f"type: {self.type} \nname : {self.name} \ncolor :{self.color} \nplace :{self.place} \
            \ngender :{self.gender} "
    
    def display_info(self):
        return f"type: {self.type} \nname : {self.name} \ncolor :{self.color} \nplace :{self.place} \
            \ngender :{self.gender} "

ob1 = corocodile("corocodile1","Green","America","Male")
print(ob1.display_info())


