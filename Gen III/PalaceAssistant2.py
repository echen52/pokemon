import numpy as np
import pandas as pd

#VERSION 1.1
# added three alarm scenarios

TrainerData = pd.read_csv("trainers.csv", index_col = "Name")
MovesetData = pd.read_csv("BFpalace.csv")

# USE ONLY LEVEL 100 OR LEVEL 50 FOR NOW
Level = 50

# ADD OR REMOVE PROBLEMATIC MOVES IF YOU LIKE

Alarms1 = ['Sheer Cold', 'Horn Drill', 'Fissure', 'Guillotine']
Alarms2 = ['Swords Dance', 'Dragon Dance', 'Double Team']
Alarms3 = ['Counter', 'Mirror Coat', 'Psych Up']



#==================================#
#=== DON'T TOUCH ANYTHING BELOW ===#
#==================================#

AlarmTotal = Alarms1 + Alarms2 + Alarms3

class PokemonSet:
	def __init__(self, Name):
		self.Name = Name
		self.Entry = int(MovesetData.loc[MovesetData["Name"] == Name,"Entry"].values[0])
		self.Species = MovesetData.loc[MovesetData["Name"] == Name,"Species"].values[0]
		self.Instance = MovesetData.loc[MovesetData["Name"] == Name,"Instance"].values[0]
		self.Item = MovesetData.loc[MovesetData["Name"] == Name,"Item"].values[0]
		self.Nature = MovesetData.loc[MovesetData["Name"] == Name,"Nature"].values[0]
		self.Move1 = MovesetData.loc[MovesetData["Name"] == Name,"Move 1"].values[0]
		self.Move2 = MovesetData.loc[MovesetData["Name"] == Name,"Move 2"].values[0]
		self.Move3 = MovesetData.loc[MovesetData["Name"] == Name,"Move 3"].values[0]
		self.Move4 = MovesetData.loc[MovesetData["Name"] == Name,"Move 4"].values[0]
		self.Speed = int(MovesetData.loc[MovesetData["Name"] == Name,"Lv " + str(Level) + " Speed"].values[0])
		self.MoveList = [self.Move1, self.Move2, self.Move3, self.Move4]

		self.Attack = MovesetData.loc[MovesetData["Name"] == Name,"AI_ATK"].values[0]
		self.Defense = MovesetData.loc[MovesetData["Name"] == Name,"AI_DEF"].values[0]
		self.Support = MovesetData.loc[MovesetData["Name"] == Name,"AI_SPT"].values[0]
		self.Attack50 = MovesetData.loc[MovesetData["Name"] == Name,"AI_ATK_50"].values[0]
		self.Defense50 = MovesetData.loc[MovesetData["Name"] == Name,"AI_DEF_50"].values[0]
		self.Support50 = MovesetData.loc[MovesetData["Name"] == Name,"AI_SPT_50"].values[0]
		self.R_ATK = MovesetData.loc[MovesetData["Name"] == Name,"R_ATK"].values[0]
		self.R_DEF = MovesetData.loc[MovesetData["Name"] == Name,"R_DEF"].values[0]
		self.NOMOVE = MovesetData.loc[MovesetData["Name"] == Name,"NOMOVE"].values[0]
		self.R_ATK50 = MovesetData.loc[MovesetData["Name"] == Name,"R_ATK_50"].values[0]
		self.R_DEF50 = MovesetData.loc[MovesetData["Name"] == Name,"R_DEF_50"].values[0]
		self.NOMOVE50 = MovesetData.loc[MovesetData["Name"] == Name,"NOMOVE_50"].values[0]







		self.Move1Class = MovesetData.loc[MovesetData["Name"] == Name,"Move 1 Class"].values[0]
		self.Move2Class = MovesetData.loc[MovesetData["Name"] == Name,"Move 2 Class"].values[0]
		self.Move3Class = MovesetData.loc[MovesetData["Name"] == Name,"Move 3 Class"].values[0]
		self.Move4Class = MovesetData.loc[MovesetData["Name"] == Name,"Move 4 Class"].values[0]




		self.LocalOdds = 1
		self.GlobalOdds = 1

		self.Alarm = False
		for move in self.MoveList:
			if move in AlarmTotal:
				self.Alarm = True

	def Setprinter(self):
		msg = "!!!" if self.Alarm == True else ""
		print(f'{msg:>3}',f'{self.Name:>13}',f'{np.round(self.LocalOdds,6):>9}',f'{self.Item:>13}',f'{self.Nature:>8}',f'{self.Move1:>13}',f'{self.Move2:>13}',f'{self.Move3:>13}',f'{self.Move4:>13}',f'{self.Speed:>6}')


	#New function that adds Battle Palace Move classification and displays Nature table for selected Pokemon
	def Palaceprinter(self):
		msg = "!!!" if self.Alarm == True else ""
		print("This Pokemon's moves are classified as:")
		print('')
		print(f'{msg:>3}',f'{self.Name:>13}',f'{self.Item:>13}',f'{self.Nature:>8}',f'{self.Move1Class:>17}',f'{self.Move2Class:>17}',f'{self.Move3Class:>17}',f'{self.Move4Class:>17}')
		print("-----------------------------------------------------------------------------------------------------------------")
		print("This Pokemon's behaviors are:")
		print('')
		msg0 = ""
		msg3 = "AI_ATK"
		msg4 = "AI_DEF"
		msg5 = "AI_SPT"
		msgBreak = "|||"
		msg6 = "AI_ATK<50"
		msg7 = "AI_DEF<50"
		msg8 = "AI_SPT<50"

		msg13 = "R_ATK"
		msg14 = "R_DEF"
		msg15 = "NOMOVE"
		msg16 = "R_ATK<50"
		msg17 = "R_DEF<50"
		msg18 = "NOMOVE<50"



		filler1 ='   '
		filler2 ='          '

		print(f'{msg0:>3}',f'{msg0:>12}', f'{msg0:>9}', f'{msg0:>13}',f'{msg3:>7}', f'{msg4:>7}', f'{msg5:>7}',  f'{msgBreak:>7}',f'{msg6:>10}', f'{msg7:>10}', f'{msg8:>10}')
		print(f'{msg:>3}',f'{self.Name:>13}', f'{self.Item:>13}',f'{self.Nature:>8}', f'{self.Attack:>7}', f'{self.Defense:>7}', f'{self.Support:>7}',
		f'{msgBreak:>7}',
		f'{self.Attack50:>10}',f'{self.Defense50:>10}', f'{self.Support50:>10}')

		print(f'{msg0:>3}',f'{msg0:>12}', f'{msg0:>9}', f'{msg0:>13}',f'{msg13:>7}', f'{msg14:>7}', f'{msg15:>7}',  f'{msgBreak:>7}',f'{msg16:>10}', f'{msg17:>10}', f'{msg18:>10}')
		print(f'{msg0:>3}',f'{msg0:>12}', f'{msg0:>9}',f'{msg0:>13}', f'{self.R_ATK:>7}', f'{self.R_DEF:>7}', f'{self.NOMOVE:>7}',
		f'{msgBreak:>7}',
		f'{self.R_ATK50:>10}',f'{self.R_DEF50:>10}', f'{self.NOMOVE50:>10}')


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
	print("-----------------------------------------------------------------------------------------------------------------")

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
	if Level != 50 or Pokemon.Entry <= 850 or Pokemon.Entry>1000:
		PokemonList.append(Pokemon)
		if Pokemon.Alarm == True:
			totalalarms += 1

trainerSpecies = []
for pokemon in PokemonList:
	if [pokemon.Species,0] not in trainerSpecies:
		trainerSpecies.append([pokemon.Species,0])

# CALCULATE ALL POSSIBLE TEAMS AS A LIST OF 3-TUPLES
alarmcounter = 0
alarm1counter = 0
alarm2counter = 0
alarm3counter = 0

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
pokemon1 = PokemonSet(temp + ' ' + str(number))

pokemon1.Palaceprinter()
printline()
print("")
input("Press Enter to continue...")
printline()
print("Next Pokemon probabilities:")



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

pokemon2 = PokemonSet(temp + ' ' + str(number))

pokemon2.Palaceprinter()
printline()
print("")
input("Press Enter to continue...")
printline()
print("Next Pokemon probabilities:")

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

printline()
print("Which one was it? Enter a number.")
number = input()

if number == '':
	exit()

printline()

pokemon3 = PokemonSet(temp + ' ' + str(number))

pokemon3.Palaceprinter()
#printline()
