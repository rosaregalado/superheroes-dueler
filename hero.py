import random

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
    heroes = ["Wonder Woman", "Dumbledore"]

    print (f"{random.choice(heroes)} wins!")


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  hero1 = Hero("Wonder Woman", 300)
  hero2 = Hero("Dumbledore", 250)

  hero1.fight(hero2)
