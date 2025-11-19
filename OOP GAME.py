class Character:
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp  # Encapsulation: Private variable

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        if hp < 0:
            self.__hp = 0
        else:
            self.__hp = hp

    # Method Overloading (via default arguments)
    def heal(self, amount=10):
        self.__hp += amount
        return f"{self.name} healed for {amount} HP!"

    # Base method for Overriding
    def attack(self,target):
        return "Punch"

    def take_damage(self,damage):
        new_hp = self.__hp - damage
        self.set_hp(new_hp)
        print(f"{self.name} took {damage} damage!")

# Inheritance
class Warrior(Character):
    # Method Overriding
    def attack(self,target):
        damage = 15
        target.take_damage(damage)
        return f"{self.name} slashes {target.name} for {damage} damage!"

class Mage(Character):
    # Method Overriding
    def attack(self, target):
        damage = 15
        target.take_damage(damage)
        return f"{self.name} slashes {target.name} for {damage} damage!"

# Duck Typing (No inheritance, but has attack method)
class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self,damage):
        new_hp = self.hp - damage
        if new_hp < 0:
            self.hp = 0
        else:
            self.hp = new_hp
        print(f"{self.name} took {damage} damage!")
    def attack(self, target):
        damage = 15
        target.take_damage(damage)
        return f"{self.name} bites {target.name} for {damage} damage!"


class Paladin(Warrior):
    def attack(self, target):
        damage = 15
        target.take_damage(damage)
        return f"{self.name} slashes {target.name} for {damage} damage!"


class Potion:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    # Operator Overloading (+)
    def __add__(self, other):
        return Potion(self.type, self.value + other.value)

    # Operator Overloading (str)
    def __str__(self):
        return f"{self.type} potion: {self.value}"



# --- DRIVER CODE ---

# 1. Creating Characters
conan = Warrior("Conan", 100)
merlin = Mage("Merlin", 50)
slime = Monster("Slime", 80)
lancelot=Paladin("Lancelot",80)


# 2. Polymorphism & Duck Typing
party = [conan, merlin, slime,lancelot]

print("--- BATTLE START ---")
for member in party:
    if member != slime:
        print(member.attack(slime))

# 3. Operator Overloading
print("\n--- ALCHEMY ---")
p1 = Potion("Health", 50)
p2 = Potion("Health", 100)
p3 = p1 + p2
print(p3)

# 4. Method Overloading (Healing)
print("\n--- HEALING ---")
print(f"Conan HP before: {conan.get_hp()}")

# Calling heal() with NO arguments (uses default 10)
print(conan.heal())
print(f"Conan HP after default heal: {conan.get_hp()}")

# Calling heal(50) WITH arguments (overrides default)
print(conan.heal(50))
print(f"Conan HP after big heal: {conan.get_hp()}")