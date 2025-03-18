class Duck:
    def swim(self):
        print("Swim duck Swim Duck")

    def quack(self):
        print("Quack Quack Quack")

    def waddle(self):
        print("Waddle duck Waddle duck")


class Penguin:
    def swim(self):
        print("Swim PENGUIN Swim PENGUIN")

    def quack(self):
        print("Quack Quack Quack PENGUIN")

    def waddle(self):
        print("Waddle PENGUIN Waddle PENGUIN")


def test_duck(obj):
    obj.waddle()
    obj.swim()
    obj.quack()


if "__main__" == __name__:
    donald = Duck()
    test_duck(donald)

    penguin = Penguin()
    test_duck(penguin)
