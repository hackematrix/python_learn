class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_car(self):
        long_name=f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
new_car=Car('audi','a4','2024')
print(new_car.get_car()) 
