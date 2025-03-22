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
ItemAlarmTotal = ['BrightPowder', 'Lax Incense', 'Focus Sash', 'Choice Scarf', 'Quick Claw']



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

		self.Alarm2 = False
		if self.Item in ItemAlarmTotal:
			self.Alarm2 = True

	def Setprinter(self):
		msg = "!!!" if self.Alarm == True or self.Alarm2 == True else ""
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
totalitemalarms = 0
for identifier in trainerSets:
	Pokemon = PokemonSet(identifier)
	if Level != 50 or Pokemon.Entry <= 1000:
		PokemonList.append(Pokemon)
		if Pokemon.Alarm == True:
			totalalarms += 1
		if Pokemon.Alarm2 == True:
			totalitemalarms += 1

trainerSpecies = []
for pokemon in PokemonList:
	if [pokemon.Species,0] not in trainerSpecies:
		trainerSpecies.append([pokemon.Species,0])

# CALCULATE ALL POSSIBLE TEAMS AS A LIST OF 3-TUPLES
alarmcounter = 0
alarm1counter = 0
alarm2counter = 0
alarm3counter = 0
itemalarmcounter = 0

TeamCombinations = []
for pokemon1 in PokemonList:
	for pokemon2 in PokemonList:
		for pokemon3 in PokemonList:
			if (    pokemon1.Species != pokemon2.Species
				and pokemon2.Species != pokemon3.Species
				and pokemon1.Species != pokemon3.Species
				and pokemon1.Item    != pokemon2.Item
				and pokemon2.Item    != pokemon3.Item
				and pokemon1.Item    != pokemon3.Item):
				TeamCombinations.append((pokemon1,pokemon2,pokemon3))
				teammoves = pokemon1.MoveList + pokemon2.MoveList + pokemon3.MoveList
				booleanalarm = 0
				booleanalarm1 = 0
				booleanalarm2 = 0
				booleanalarm3 = 0
				for move in teammoves:
					if move in AlarmTotal:
						booleanalarm = 1
					if move in Alarms1:
						booleanalarm1 = 1
					if move in Alarms2:
						booleanalarm2 = 1
					if move in Alarms3:
						booleanalarm3 = 1
				alarmcounter += booleanalarm
				alarm1counter += booleanalarm1
				alarm2counter += booleanalarm2
				alarm3counter += booleanalarm3
				teamitems = []
				teamitems.append(pokemon1.Item)
				teamitems.append(pokemon2.Item)
				teamitems.append(pokemon3.Item)
				itemcount =0
				for item in teamitems:
					if item in ItemAlarmTotal:
						itemcount = 1
				itemalarmcounter +=itemcount

print("This trainer has", len(PokemonList), "different sets, which constitute", int(len(TeamCombinations)/6), "different teams.")
print("There are", totalitemalarms, "alarming item sets, and there is a", round(itemalarmcounter/len(TeamCombinations),4), "chance of running into at least one of them.")
print("There are", totalalarms, "alarming movesets, and there is a", round(alarmcounter/len(TeamCombinations),4), "chance of running into at least one of them.")
print("There is", round(alarm1counter/len(TeamCombinations),4), "chance of finding Alarm1:", Alarms1)
print("There is", round(alarm2counter/len(TeamCombinations),4), "chance of finding Alarm2:", Alarms2)
print("There is", round(alarm3counter/len(TeamCombinations),4), "chance of finding Alarm3:", Alarms3)
print("There is", round(itemalarmcounter/len(TeamCombinations),4), "chance of finding an Alarming Item:", ItemAlarmTotal)
printline()

for pokemon in PokemonList:
	counter = 0
	for team in TeamCombinations:
		if team[0] == pokemon or team[1] == pokemon or team[2] == pokemon:
			counter += 1
	pokemon.LocalOdds = counter/(3*len(TeamCombinations))

PokemonList = sorted(PokemonList, key=lambda pokemon: pokemon.Instance)

# for pokemon in PokemonList:
# 	pokemon.Setprinter()

printline()
SpeciesListing(trainerSpecies, PokemonList)
printline()
print("Please enter a Pokemon you have seen.")
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
itemalarmcounter =0
TeamCombinationsAfterFirstPoke = []
for pokemon2 in PokemonList:
	for pokemon3 in PokemonList:
		if (    pokemon1.Species != pokemon2.Species
			and pokemon2.Species != pokemon3.Species
			and pokemon1.Species != pokemon3.Species
			and pokemon1.Item    != pokemon2.Item
			and pokemon2.Item    != pokemon3.Item
			and pokemon1.Item    != pokemon3.Item):
			TeamCombinationsAfterFirstPoke.append((pokemon1,pokemon2,pokemon3))
			teammoves = pokemon2.MoveList + pokemon3.MoveList
			booleanalarm = 0
			booleanalarm1 = 0
			booleanalarm2 = 0
			booleanalarm3 = 0
			for move in teammoves:
				if move in AlarmTotal:
					booleanalarm = 1
				if move in Alarms1:
					booleanalarm1 = 1
				if move in Alarms2:
					booleanalarm2 = 1
				if move in Alarms3:
					booleanalarm3 = 1
			alarmcounter += booleanalarm
			alarm1counter += booleanalarm1
			alarm2counter += booleanalarm2
			alarm3counter += booleanalarm3
			teamitems = []
			teamitems.append(pokemon2.Item)
			teamitems.append(pokemon3.Item)
			itemcount =0
			for item in teamitems:
				if item in ItemAlarmTotal:
					itemcount = 1
			itemalarmcounter +=itemcount

for pokemon in PokemonList:
	counter = 0
	for team in TeamCombinationsAfterFirstPoke:
		if team[1] == pokemon or team[2] == pokemon:
			counter += 1
	pokemon.LocalOdds = counter/(2*len(TeamCombinationsAfterFirstPoke))

PokemonList = sorted(PokemonList, key=lambda pokemon: pokemon.Instance)

# for pokemon in PokemonList:
# 		pokemon.Setprinter()

print("Updated Pokemon Probabilities")
printline()
SpeciesListing(trainerSpecies, PokemonList)
printline()
print("There is", round(alarm1counter/len(TeamCombinationsAfterFirstPoke),4), "chance of finding Alarm1:", Alarms1)
print("There is", round(alarm2counter/len(TeamCombinationsAfterFirstPoke),4), "chance of finding Alarm2:", Alarms2)
print("There is", round(alarm3counter/len(TeamCombinationsAfterFirstPoke),4), "chance of finding Alarm3:", Alarms3)
print("There is", round(itemalarmcounter/len(TeamCombinationsAfterFirstPoke),4), "chance of finding an Alarming Item:", ItemAlarmTotal)
printline()
print("Please enter another Pokemon you have seen.")
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

TeamCombinationsAfterSecondPoke = []
alarmcounter = 0
alarm1counter = 0
alarm2counter = 0
alarm3counter = 0
itemalarmcounter =0
for pokemon3 in PokemonList:
	if (    pokemon1.Species != pokemon2.Species
		and pokemon2.Species != pokemon3.Species
		and pokemon1.Species != pokemon3.Species
		and pokemon1.Item    != pokemon2.Item
		and pokemon2.Item    != pokemon3.Item
		and pokemon1.Item    != pokemon3.Item):
		TeamCombinationsAfterSecondPoke.append((pokemon1,pokemon2,pokemon3))
		teammoves = pokemon3.MoveList
		booleanalarm = 0
		booleanalarm1 = 0
		booleanalarm2 = 0
		booleanalarm3 = 0
		for move in teammoves:
			if move in AlarmTotal:
				booleanalarm = 1
			if move in Alarms1:
				booleanalarm1 = 1
			if move in Alarms2:
				booleanalarm2 = 1
			if move in Alarms3:
				booleanalarm3 = 1
		alarmcounter += booleanalarm
		alarm1counter += booleanalarm1
		alarm2counter += booleanalarm2
		alarm3counter += booleanalarm3
		teamitems = []
		teamitems.append(pokemon3.Item)
		itemcount =0
		for item in teamitems:
			if item in ItemAlarmTotal:
				itemcount = 1
		itemalarmcounter +=itemcount

for pokemon in PokemonList:
	counter = 0
	for team in TeamCombinationsAfterSecondPoke:
		if team[2] == pokemon:
			counter += 1
	pokemon.LocalOdds = counter/len(TeamCombinationsAfterSecondPoke)

PokemonList = sorted(PokemonList, key=lambda pokemon: pokemon.Instance)

# for pokemon in PokemonList:
# 		pokemon.Setprinter()

print("Updated Pokemon Probabilities")
printline()
SpeciesListing(trainerSpecies, PokemonList)
printline()
print("There is", round(alarm1counter/len(TeamCombinationsAfterSecondPoke),4), "chance of finding Alarm1:", Alarms1)
print("There is", round(alarm2counter/len(TeamCombinationsAfterSecondPoke),4), "chance of finding Alarm2:", Alarms2)
print("There is", round(alarm3counter/len(TeamCombinationsAfterSecondPoke),4), "chance of finding Alarm3:", Alarms3)
print("There is", round(itemalarmcounter/len(TeamCombinationsAfterSecondPoke),4), "chance of finding an Alarming Item:", ItemAlarmTotal)
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
