class Student:
    def __init__(self, name, age, id, address): 
        self.name = name
        self.age =  age
        self.student_id = id
        self.address = address  
        
obj = Student("gunasekhar", 23, 191611072, "vrk") 
print(obj.name)
print(obj.age)
print(obj.address)
