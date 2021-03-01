from random import randint

class KillerTomato:

    def __init__(self):
        self.hp = 10
        self.hp_max = 10
        self.defense = 1

    def attack(self, other_vegetable):
        damage = max(0, randint(4, 6) - other_vegetable.defense)
        other_vegetable.hp -= damage

class PuncherBroccoli:

    def __init__(self):
        self.hp = 10
        self.hp_max = 10
        self.defense = 2

    def attack(self, other_vegetable):
        damage = max(0, randint(1, 4) - other_vegetable.defense)
        if self.hp < self.hp_max/2:
            damage = max(0, randint(1, 4) * 2 - other_vegetable.defense)
        else:
            damage = max(0, randint(1, 4) - other_vegetable.defense)
        other_vegetable.hp -= damage

class BrawlerCarrot:

    def __init__(self):
        self.hp = 8
        self.hp_max = 8
        self.defense = 1

    def attack(self, other_vegetable):
        d =  randint(3, 5)
        damage = max(0, d - other_vegetable.defense)
        if d == 5 and self.hp < self.hp_max:
            self.hp += 1
            
        other_vegetable.hp -= damage
# voir correction


class Ring:

    def __init__(self, veg_1, veg_2):
        self.change_vegetables(veg_1,veg_2)

    def change_vegetables(self, veg_1, veg_2):
        self.veg_1 = veg_1
        self.veg_2 = veg_2

        self.veg_1.hp = self.veg_1.hp_max
        self.veg_2.hp = self.veg_2.hp_max
    
    def round_fight(self): #a linterieur du ring = self
        
        self.veg_1.attack(self.veg_2)
        print(f"Veg 2: {self.veg_2}")

        if self.veg_2.hp <= 0:
            return self.veg_1

        self.veg_2.attack(self.veg_1)
        print(f"Veg 1: {self.veg_1}")

        if self.veg_1.hp <= 0:
            return self.veg_2



        # while self.veg_1.hp_max <= 0 or self.veg_2.hp_max <= 0:
        #     veg_1.attack(veg_2)
        #     print(self.veg_2.hp)

        #     if self.veg_2.hp <= 0:
        #         return self.veg_1
        #     elif self.veg_1.hp <= 0:
        #         return self.veg_2
        #     else:
        #         return None
