class Player:
    def __init__(self, name):
        self.name = name
        self.__lives = 3
        self.__level = 1
        self.score = 0

    def _get__lives(self):
        return self.__lives

    def _set__lives(self, lives):
        if lives >= 0:
            self.__lives = lives
        else:
            print("Lives can't be negative")
            self.__lives = 0

    def _get__levels(self):
        return self.__level

    def _set__levels(self, levels):
        if levels >= 0:
            delta = levels - self.__level
            self.score += delta * 1000
            self.__level = levels
        else:
            print("Level can't be negative")

    lives = property(_get__lives, _set__lives)
    level = property(_get__levels, _set__levels)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(
            self
        )
