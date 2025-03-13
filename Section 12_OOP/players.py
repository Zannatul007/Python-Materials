class Player:
    def __init__(self, name):
        self.name = name
        self.__lives = 3
        self.level = 1
        self.score = 0

    def _get__lives(self):
        return self.__lives

    def _set__lives(self, lives):
        if lives >= 0:
            self.__lives = lives
        else:
            print("Lives can't be negative")

    lives = property(_get__lives, _set__lives)

    def __str__(self):
        print(
            "Name: {0.name}, Lives: {0.lives},Level: {0.level}, Score: {0.score}".format(
                self
            )
        )
