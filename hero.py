# import classes from other files
import random
from ability import Ability
from armor import Armor 
from weapon import Weapon

class Hero:
  def __init__(self, name, starting_health=100):
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.abilities = list()
    self.armors = list()
    self.deaths = 0
    self.kills = 0

  # fight method
  def fight(self, opponent):
    if len(self.abilities) == 0 and len(opponent.abilities) == 0:
      print(f"draw")
    else:
      while self.current_health > 0 or opponent.current_health > 0:
        total_damage = self.attack()
        opponent.take_damage(total_damage)

        if opponent.is_alive() == True:
          total_damage = opponent.attack()
          # hero takes the damage
          self.take_damage(total_damage)

          if self.is_alive == True:
            total_damage = self.attack()
            # opponent takes the damage
            opponent.take_damage(total_damage)
          else:
            # self is dead, opponent wins
            self.deaths+=1
            opponent.kills+=1
            return print(f'{opponent.name} won!')

        # opponent is dead, self wins
        elif opponent.is_alive() == False:
          opponent.deaths+=1
          self.kills+=1
          return print(f'{self.name} won!')


  # ability method
  def add_ability(self, ability):
    self.abilities.append(ability)

  # armor method
  def add_armor(self, armor):
    self.armors.append(armor)

  # weapon method
  def add_weapon(self, weapon):
    self.abilities.append(weapon)

  # attack method
  def attack(self):
    '''Calculate the total damage from all ability attacks.
      return: total_damage:Int'''
    # start total at 0
    total_damage = 0
    for ability in self.abilities:
      # add the damage of each attack to the total damage
      total_damage += ability.attack()
    return total_damage

  # defend method
  def defend(self):
    '''Calculate the total block amount from all armor blocks.
    return: total_block:Int'''
    total_block = 0
    # check if not dead
    if self.current_health == 0:
      total_block = 0
    else:
      for armor in self.armors:
        total_block += armor.block()
    return total_block

  # damage method
  def take_damage(self, damage):
    '''Updates self.current_health to reflect the damage minus the defense.'''
    defense = self.defend()
    new_damage = damage - defense
    if new_damage > 0:
      self.current_health -= new_damage
      return self.current_health
    else:
      return "No damage"

  # check if hero still alive
  def is_alive(self):
    '''Return True of False depending on whether the hero is alive or not.'''
    if self.current_health <= 0:
      # dead
      return False
    else:
      # alive
      return True



if __name__ == "__main__":
  # hero1 = Hero("Wonder Woman")
  # hero2 = Hero("Dumbledore")
  # ability1 = Ability("Super Speed", 300)
  # ability2 = Ability("Super Eyes", 130)
  # ability3 = Ability("Wizard Wand", 80)
  # ability4 = Ability("Wizard Beard", 20)
  # hero1.add_ability(ability1)
  # hero1.add_ability(ability2)
  # hero2.add_ability(ability3)
  # hero2.add_ability(ability4)
  # hero1.fight(hero2)

  hero = Hero("Wonder Woman")
  weapon = Weapon("Lasso of Truth", 90)
  hero.add_weapon(weapon)
  print(hero.attack())