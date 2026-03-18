from Character import Character

class Novice(Character):
    def basicAttack(self, character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage()}")

character1 = Novice("Your Username")
print(character1.getUsername())
print(character1.getHp())