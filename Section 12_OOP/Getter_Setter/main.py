from players import Player

zane = Player("Zane")
print(zane.__dict__)
# lives = zane._get__lives()
# print(lives)

# new_lives = zane._set__lives(100)
# print(new_lives)

print(zane)
zane.lives -= 1
print(zane)
zane.lives -= 1
print(zane)
zane.lives -= 1
print(zane)
zane.lives -= 1
print(zane)
zane.level = 4
print(zane)


player = Player("MEEM")
player.lives = 5
player.level = 3  # This should increase the score
print(player)
