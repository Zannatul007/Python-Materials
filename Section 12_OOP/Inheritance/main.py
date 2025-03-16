from enemy import Enemy, Troll, Vampire

# random_enemy = Enemy("Sagacious", 100, 1)
# random_enemy.take_damage(50)
# print(random_enemy)
# random_enemy.take_damage(60)
# print(random_enemy)

troll_1 = Troll()
print(troll_1)

another_troll = Troll("Ugly_another", 20, 1)
print("Another troll --> {}".format(another_troll))

troll_2 = Troll("Ugly Brother", 24)
print("The third Troll --> {}".format(troll_2))
troll_2.grunt()


vampire = Vampire("Zane", 30, 5)

while vampire.alive:
    vampire.take_damage(5)
    print(vampire)

