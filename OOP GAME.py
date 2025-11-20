from nn import NeuralNetwork, Neuron

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

    def heal(self, amount=10):
        self.hp += amount
        return f"{self.name} regenerates {amount} HP!"

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


class SmartMonster(Monster):
    def __init__(self, name, hp):
        # Initialize the basic Monster stats
        super().__init__(name, hp)

        # --- CREATE THE BRAIN ---

        # Neuron 1: The "Aggressor"
        # Positive weight (0.1): It gets excited when HP is high.
        # Bias (-5): It needs a decent amount of HP to start firing.
        neuron_attack = Neuron([0.1], -5)

        # Neuron 2: The "Survivor"
        # Negative weight (-0.1): It gets excited when HP is LOW.
        # Bias (5): It starts firing easily unless HP gets too high.
        neuron_heal = Neuron([-0.1], 5)

        # The Network holds both neurons
        self.brain = NeuralNetwork([neuron_attack, neuron_heal])

    def attack(self, target):
        # 1. Ask the brain. It expects a list of inputs, so we wrap hp in brackets.
        decisions = self.brain.feed_forward([self.hp])

        # decisions[0] is the Attack score (because we added that neuron first)
        # decisions[1] is the Heal score

        attack_score = decisions[0]
        heal_score = decisions[1]
        print(f"[{self.name} Brain] Attack: {attack_score:.2f} | Heal: {heal_score:.2f}")

        # 2. Decision Logic
        if attack_score > heal_score:
            # COPY the attack logic here directly (don't use 'def')
            damage = 20
            target.take_damage(damage)
            return f"{self.name} chooses VIOLENCE and bites {target.name}!"
        else:
            # Call the inherited heal method
            return f"{self.name} chooses SURVIVAL: " + self.heal()


# --- DRIVER CODE ---

# # 1. Creating Characters
# conan = Warrior("Conan", 100)
# merlin = Mage("Merlin", 50)
# slime = Monster("Slime", 80)
# lancelot=Paladin("Lancelot",80)
#
#
# # 2. Polymorphism & Duck Typing
# party = [conan, merlin, slime,lancelot]
#
# print("--- BATTLE START ---")
# for member in party:
#     if member != slime:
#         print(member.attack(slime))
#
# # 3. Operator Overloading
# print("\n--- ALCHEMY ---")
# p1 = Potion("Health", 50)
# p2 = Potion("Health", 100)
# p3 = p1 + p2
# print(p3)
#
# # 4. Method Overloading (Healing)
# print("\n--- HEALING ---")
# print(f"Conan HP before: {conan.get_hp()}")
#
# # Calling heal() with NO arguments (uses default 10)
# print(conan.heal())
# print(f"Conan HP after default heal: {conan.get_hp()}")
#
# # Calling heal(50) WITH arguments (overrides default)
# print(conan.heal(50))
# print(f"Conan HP after big heal: {conan.get_hp()}")

smart_beast = SmartMonster("Smart Beast", 110)
dummy_target = Warrior("Training Dummy", 500)

print(f"--- OBSERVING AI BEHAVIOR ({smart_beast.name}) ---")

# We will simulate 5 turns
for turn in range(1, 6):
    print(f"\n--- TURN {turn} (Current HP: {smart_beast.hp}) ---")

    # 1. The Monster decides what to do based on CURRENT HP
    print(smart_beast.attack(dummy_target))

    # 2. CRITICAL STEP: We hurt the monster to change the input for next time
    # We force it to take 25 damage every turn
    print(">> The Training Dummy smacks the beast!")
    smart_beast.take_damage(25)
