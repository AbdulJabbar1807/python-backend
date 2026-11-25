from enemy_class import *

zombie = Enemy('Zombie',15,3)

print(f"{zombie.type_of_enemy} has {zombie.health_points} points and can do attack damage of {zombie.attack_damage}")

zombie.talk()
zombie.walk()
zombie.attack()