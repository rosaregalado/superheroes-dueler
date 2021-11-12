class Team:
  def __init__(self, name):
    ''' Initialize your team with its team name and an empty list of heroes
    '''
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
    '''Add Hero object to self.heroes.'''
    self.heroes.append(hero)

  def view_all_heroes(self):
    '''Prints out all heroes to the console.'''
    for hero in self.heroes:
      print(hero.name)
  
