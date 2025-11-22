# Create a Person class where we will have five attributes and five behaviors.
# Make sure that each type of function is used, and I want you to also create the print function,
# which will print all the instance variable values.

class Person:
    def __init__(self, name, age, gender, course, batch):
        self.name=name
        self.age=age
        self.course=course
        self.gender=gender
        self.batch=batch

    def get_data(self):
        print("name is ", self.name)
        print("age is ", self.age)
        print("gender is ", self.gender)
        print("course is ", self.course)
        print("batch is ", self.batch)

    def change_batch(self,batch):
        self.batch=batch
        print("Changed batch is -",self.batch)

p1=Person("john",23,"male","python","6x")
p1.get_data()
p1.change_batch("5x")




