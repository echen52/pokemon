import numpy as np
import pandas as pd

#VERSION 1.1
# added three alarm scenarios

TrainerData = pd.read_csv("subway_trainers.csv", index_col = "Name")
MovesetData = pd.read_csv("subway_pokemon.csv")

# USE ONLY LEVEL 100 OR LEVEL 50 FOR NOW
Level = 50

# ADD OR REMOVE PROBLEMATIC MOVES IF YOU LIKE

Alarms1 = ['Fake Out', 'Quick Attack', 'Mach Punch', 'Bullet Punch', 'Aqua Jet', 'Ice Shard', 'Shadow Sneak', 'Sucker Punch', 'ExtremeSpeed']
Alarms2 = ['Rain Dance', 'Hail', 'Trick Room']
Alarms3 = ['Counter', 'Mirror Coat', 'Fling']



#==================================#
#=== DON'T TOUCH ANYTHING BELOW ===#
#==================================#

AlarmTotal = Alarms1 + Alarms2 + Alarms3

class PokemonSet:
	def __init__(self, Instance):
		self.Instance = Instance
		self.Entry = int(MovesetData.loc[MovesetData["Instance"] == Instance,"Entry"].values[0])
		self.Species = MovesetData.loc[MovesetData["Instance"] == Instance,"Species"].values[0]
		self.Name = MovesetData.loc[MovesetData["Instance"] == Instance,"Name"].values[0]
		self.Item = MovesetData.loc[MovesetData["Instance"] == Instance,"Item"].values[0]
		self.Nature = MovesetData.loc[MovesetData["Instance"] == Instance,"Nature"].values[0]
		self.Species = MovesetData.loc[MovesetData["Instance"] == Instance,"Species"].values[0]
		self.Move1 = MovesetData.loc[MovesetData["Instance"] == Instance,"Move 1"].values[0]
		self.Move2 = MovesetData.loc[MovesetData["Instance"] == Instance,"Move 2"].values[0]
		self.Move3 = MovesetData.loc[MovesetData["Instance"] == Instance,"Move 3"].values[0]
		self.Move4 = MovesetData.loc[MovesetData["Instance"] == Instance,"Move 4"].values[0]
		self.Speed = MovesetData.loc[MovesetData["Instance"] == Instance,"Speed"].values[0]
		# self.Speed = int(MovesetData.loc[MovesetData["Name"] == Name,"Lv " + str(Level) + " Speed"].values[0])
		self.MoveList = [self.Move1, self.Move2, self.Move3, self.Move4]
		self.LocalOdds = 1
		self.GlobalOdds = 1

		self.Alarm = False
		for move in self.MoveList:
			if move in AlarmTotal:
				self.Alarm = True

	def Setprinter(self):
		msg = "!!!" if self.Alarm == True else ""
		print(f'{msg:>3}',f'{self.Name:>13}',f'{np.round(self.LocalOdds,6):>9}',f'{self.Item:>13}',f'{self.Nature:>8}',f'{self.Move1:>13}',f'{self.Move2:>13}',f'{self.Move3:>13}',f'{self.Move4:>13}', f'{self.Speed:>8}' )

def SpeciesListing(trainerSpecies, PokemonList):
	for species in trainerSpecies:
		species[1] = 0
		for pokemon in PokemonList:
			if pokemon.Species == species[0]:
				species[1] += pokemon.LocalOdds

	trainerSpecies = sorted(trainerSpecies, key=lambda pair: pair[1], reverse=True)

	for species in trainerSpecies:
			print(f'{species[0].upper():>15}',f'{np.round(species[1],6):>11}')

def printline():
	print("--------------------------------------------------------------------------------------------------------------------")

printline()
print("What trainer are you battling?")
Trainer = input()
if Trainer == '':
	exit()
Trainer = Trainer.upper()
printline()

# CONVERT ALL SET IDENTIFIERS TO POKEMON WITH INFORMATION FROM TABLE
trainerSets = list(TrainerData.loc[[Trainer]].values[0])
del trainerSets[0]
trainerSets = [x for x in trainerSets if x == x]
PokemonList = []
totalalarms = 0
for identifier in trainerSets:
	Pokemon = PokemonSet(identifier)
	if Level != 50 or Pokemon.Entry <= 1000:
		PokemonList.append(Pokemon)
		if Pokemon.Alarm == True:
			totalalarms += 1

trainerSpecies = []
for pokemon in PokemonList:
	if [pokemon.Species,0] not in trainerSpecies:
		trainerSpecies.append([pokemon.Species,0])




for pokemon in PokemonList:
	counter = 0
	for pokemon2 in trainerSpecies:

		if pokemon2[0] == pokemon.Species:
			counter += 1
	pokemon.LocalOdds = counter/len(PokemonList)

PokemonList = sorted(PokemonList, key=lambda pokemon: pokemon.LocalOdds, reverse=True)



printline()
SpeciesListing(trainerSpecies, PokemonList)
printline()
print("Please enter the 1st Pokemon you have seen.")
temp = input()
if temp == '':
	exit()
temp = temp.capitalize()
printline()
print("Possible sets:")
odds = 0
for pokemon in PokemonList:
	if pokemon.Species == temp:
		odds += pokemon.LocalOdds
for pokemon in PokemonList:
	if pokemon.Species == temp:
		pokemon.LocalOdds /= odds
		pokemon.Setprinter()
printline()
print("Which one was it? Enter a number.")
number = input()
if number == '':
	exit()
printline()

pokemon1 = PokemonSet('P ' + str(number))
alarmcounter = 0
alarm1counter = 0
alarm2counter = 0
alarm3counter = 0


firstSpecies = pokemon1.Species
firstItem = pokemon1.Item


removalList =[]
for pokemon in PokemonList:

	if pokemon.Species == firstSpecies or pokemon.Item == firstItem:
		removalList.append(pokemon)



for pokemon in removalList:
	# print("Removing")
	# print(pokemon.Species)
	PokemonList.remove(pokemon)



PokemonList = sorted(PokemonList, key=lambda pokemon: pokemon.LocalOdds, reverse=True)


printline()
SpeciesListing(trainerSpecies, PokemonList)
printline()

printline()
print("Please enter the 2nd Pokemon you have seen.")
temp = input()
if temp == '':
	exit()
temp = temp.capitalize()
printline()
print("Possible sets:")
odds = 0
for pokemon in PokemonList:
	if pokemon.Species == temp:
		odds += pokemon.LocalOdds
for pokemon in PokemonList:
	if pokemon.Species == temp:
		pokemon.LocalOdds /= odds
		pokemon.Setprinter()
printline()
print("Which one was it? Enter a number.")
number = input()
if number == '':
	exit()
printline()

pokemon2 = PokemonSet('P ' + str(number))

secondSpecies = pokemon2.Species
secondItem = pokemon2.Item

removalList =[]
for pokemon in PokemonList:

	if pokemon.Species == secondSpecies or pokemon.Item == secondItem:

		removalList.append(pokemon)

for pokemon in removalList:
	PokemonList.remove(pokemon)



PokemonList = sorted(PokemonList, key=lambda pokemon: pokemon.LocalOdds, reverse=True)

printline()
SpeciesListing(trainerSpecies, PokemonList)
printline()
printline()
print("Please enter the 3rd Pokemon you have seen.")
temp = input()
if temp == '':
	exit()
temp = temp.capitalize()
printline()
print("Possible sets:")
odds = 0
for pokemon in PokemonList:
	if pokemon.Species == temp:
		odds += pokemon.LocalOdds
for pokemon in PokemonList:
	if pokemon.Species == temp:
		pokemon.LocalOdds /= odds
		pokemon.Setprinter()
printline()
print("Which one was it? Enter a number.")
number = input()
if number == '':
	exit()
printline()

pokemon3 = PokemonSet('P ' + str(number))

thirdSpecies = pokemon3.Species
thirdItem = pokemon3.Item

removalList =[]
for pokemon in PokemonList:

	if pokemon.Species == thirdSpecies or pokemon.Item == thirdItem:

		removalList.append(pokemon)

for pokemon in removalList:
	PokemonList.remove(pokemon)



PokemonList = sorted(PokemonList, key=lambda pokemon: pokemon.LocalOdds, reverse=True)





printline()
SpeciesListing(trainerSpecies, PokemonList)
printline()

printline()
print("Please enter the last Pokemon.")
temp = input()
if temp == '':
	exit()
temp = temp.capitalize()
printline()
print("Possible sets:")
odds = 0
for pokemon in PokemonList:
	if pokemon.Species == temp:
		odds += pokemon.LocalOdds
for pokemon in PokemonList:
	if pokemon.Species == temp:
		pokemon.LocalOdds /= odds
		pokemon.Setprinter()
