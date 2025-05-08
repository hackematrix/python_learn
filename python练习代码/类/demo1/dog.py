class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog=Dog('Willie',6)

print(f"My dog's name is {my_dog.name}")
print(f"my dog's age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()
