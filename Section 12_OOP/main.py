from players import Player

zane = Player("Zane")
print(zane.__dict__)
# lives = zane._get__lives()
# print(lives)

# new_lives = zane._set__lives(100)
# print(new_lives)

# print(zane.lives)
# zane.lives -= 1
# print(zane.lives)
# zane.lives -= 1
# print(zane.lives)
# zane.lives -= 1
# print(zane.lives)
# zane.lives -= 1
# print(zane.lives)


zane = Player("Zane")

print(zane.lives)  # ✅ Calls _get__lives() → Output: 3

zane.lives = 5  # ✅ Calls _set__lives(5)
print(zane.lives)  # ✅ Calls _get__lives() again → Output: 5

zane.lives = -10  # ❌ Invalid (prints: "Lives can't be negative")
print(zane.lives)  # ✅ Still 5 (because negative values are not allowed)
