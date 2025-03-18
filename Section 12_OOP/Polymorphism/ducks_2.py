class Wing:
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if (self.ratio) > 1:
            print("Weee...I can fly")
        elif (self.ratio) == 1:
            print("It's hard to fly but i can manage")
        else:
            print("Alas!! I can't fly")


class Duck:
    def __init__(self):
        self._wing = Wing(1.8)

    def swim(self):
        print("Swim duck Swim Duck")

    def quack(self):
        print("Quack Quack Quack")

    def waddle(self):
        print("Waddle duck Waddle duck")

    def wing_fly(self):
        self._wing.fly()


def test_duck(duck):
    duck.swim()
    duck.waddle()
    duck.quack()
    duck.wing_fly()


if "__main__" == __name__:
    donald = Duck()
    test_duck(donald)
