class Enemy:
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            print(
                "{} took {} point and remaining points {}".format(
                    self.name, damage, remaining_points
                )
            )
            self.hit_points = remaining_points
        else:
            self.lives -= 1

            if self.lives <= 0:
                self.alive = False
                print("Game Over")
            else:
                print(f"{self.name} lost a life")

    def __str__(self):
        return "Name: {0.name}, Hit points: {0.hit_points}, Lives: {0.lives}".format(
            self
        )


class Troll(Enemy):
    def __init__(self, name="Troll Enemy", hit_points=0, lives=1):
        super().__init__(name, hit_points, lives)

    def grunt(self):
        print(f"{self.name} kicked {self.name}")


class Vampire(Enemy):
    def __init__(self, name="Vampire Enemy", hit_points=0, lives=1):
        super().__init__(name, hit_points, lives)
