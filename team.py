import random

class Team:
  def __init__(self, name):
    self.name = name
    self.heroes = list()

  def remove_hero(self, name):
    foundHero = False
    # loop through each hero in our list
    for hero in self.heroes:
      # if we find them, remove them from the list
      if hero.name == name:
        self.heroes.remove(hero)
        # set our indicator to True
        foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
    if not foundHero:
      return 0

  def add_hero(self, hero):
    # Add Hero object to self.heroes.
    self.heroes.append(hero)

  def view_all_heroes(self):
    # Prints out all heroes to the console.
    for hero in self.heroes:
      print(hero.name)
  
  def stats(self):
    # Print team statistics
    for hero in self.heroes:
      kd = hero.kills / hero.deaths
      print(f"{hero.name} Kill/Deaths:{kd}")

  def revive_heroes(self, health=100):
    # set the hero's current_health to their starting_health
    for hero in self.heroes:
      hero.current_health = hero.starting_health


  def attack(self, other_team):
    # Battle each team against each other.
    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents)> 0:
      hero = random.choice(living_heroes)
      opponent = random.choice(living_opponents)

      # fight
      hero.fight(opponent)

      # remove dead
      if hero.is_alive():
        living_opponents.remove(opponent)
      else:
        living_heroes.remove(hero)


