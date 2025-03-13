class Enemy:
    def __init__(self, name, hit_points, lives):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            print(
                "I took {} point and remaining points {}".format(
                    damage, remaining_points
                )
            )
            self.hit_points = remaining_points
        else:
            self.lives -= 1
            if self.lives <= 0:
                print("Game Over")

    def __str__(self):
        return "Name {0.name}, Hit points {0.hit_points}, Lives {0.lives}".format(self)
