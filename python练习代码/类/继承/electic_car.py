class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印一个句子,指出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        """将里程表读表设置为给定的值"""
        if mileage >=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading+=miles


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        # 能调用父类的方法

my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
