

class LivingThing():
	def __init__(self, name, health, spellPoints, _gold):
		self.name = name
		self.health = health
		self.spellPoints = spellPoints
		self._gold = _gold
		
	def incomeEarned(self, income):
		self._gold += income
		return self._gold
		
hero = LivingThing('Matt', 50, 80, 10)

print('the hero %s has %s gold.' %(hero.name, hero._gold))

print LivingThing.incomeEarned(hero, 1)

