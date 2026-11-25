class Enemy:
    def __init__(self,type_of_enemy,health_points=10,attack_damage=1) -> None:
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
    
    def talk(self):
        print(f"I'm a {self.type_of_enemy}.Be prepared to fight.")
        
    def walk(self):
        print(f"{self.type_of_enemy} moves closer to you.")
    
    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage.")
    