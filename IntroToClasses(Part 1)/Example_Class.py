class Dog():
    def __init__(self):
        self.age = "11"
        self.name = "Rover"
        self.weight = "34"

    def introduce(self):
        print("My name is " + (my_dog.name))
        print("I am " + (my_dog.age) + " years old")
        print("My weight is " + (my_dog.weight) + " kg")

#Call Dog class
my_dog = Dog()
my_dog.introduce()

#Updating attibutes for the second instance of the class
my_dog.age = "13"
my_dog.name = "lassie"
my_dog.weight = "30"
my_dog_2 = Dog()

#Add white space 
print("""
      """)

#Call second instance of the class
my_dog_2.introduce()







