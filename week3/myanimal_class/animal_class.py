class Animal:
    def __init__(self, name) -> None:
        self.name = name
        
    def eat(self,food):
        print(self.name + " eating " + str(food))

class Bird(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def Fly(self, speed):
        print("i'm " + self.name + " and my Fly speed is : " + str(speed))

class Crawler(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def Crawl(self, speed):
        print("i'm " + self.name + " and my Crawl speed is : " + str(speed))


class Walker(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def walk(self, speed):
        print("i'm " + self.name + " and my walk speed is : " + str(speed))


owl= Bird("Owl")
owl.eat("worm")
owl.Fly(25)

turtle=Crawler("turtle")
turtle.eat("grass")
turtle.Crawl(2)