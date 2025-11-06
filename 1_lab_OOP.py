
class Car:
    def __init__(self, 
                 marka = str, 
                 model = str, 
                 yearelease = int, 
                 color = str):
        self.marka = marka
        self.model = model
        self.yeareleas = yearelease
        self.color = color


class Driver:
    def __init__(self, 
                 name = str, 
                 age = int, 
                 experience = int, 
                 kategoriy_licen = dict):
        self.name = name
        self.age = age
        self.experience = experience
        self.kategoriy_licen = kategoriy_licen

    def info(self) -> None:
        print(f"Водій: {self.name}, {self.age} років, досвід {self.experience} років.")
        print(f"Категорії прав: {self.kategoriy_licen}")



    def license(self, yearelease) -> None:
        if self.experience >= 2:
            print(f"{self.name} може керувати автомобілем {yearelease} року випуску.")
        else:
            print(f"{self.name} має замалий досвід для керування цим автомобілем.")


avto1 = Car("Toyota", "Corolla", 2020, "сірий")
vodiy1 = Driver("Олександр", 35, 10, ["B", "C"])



vodiy1.info()
vodiy1.license(avto1.yeareleas)

