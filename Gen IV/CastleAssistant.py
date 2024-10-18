import numpy as np
import pandas as pd

#VERSION 1.1
# added three alarm scenarios

#TrainerData = pd.read_csv("trainers_HGSS.csv", index_col = "Name")
MovesetData = pd.read_csv("pokemon_HGSS.csv")

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
		self.Species = MovesetData.loc[MovesetData["Name"] == Name,"Species"].values[0]
		self.Move1 = MovesetData.loc[MovesetData["Name"] == Name,"Move1"].values[0]
		self.Move2 = MovesetData.loc[MovesetData["Name"] == Name,"Move2"].values[0]
		self.Move3 = MovesetData.loc[MovesetData["Name"] == Name,"Move3"].values[0]
		self.Move4 = MovesetData.loc[MovesetData["Name"] == Name,"Move4"].values[0]
		self.Speed = MovesetData.loc[MovesetData["Name"] == Name,"Speed"].values[0]
		self.HP = MovesetData.loc[MovesetData["Name"] == Name,"HP"].values[0]
		self.Ability1 = MovesetData.loc[MovesetData["Name"] == Name,"Ability1"].values[0]
		self.Ability2 = MovesetData.loc[MovesetData["Name"] == Name,"Ability2"].values[0]
		self.MoveList = [self.Move1, self.Move2, self.Move3, self.Move4]
		self.LocalOdds = 1
		self.GlobalOdds = 1

		self.Alarm = False
		for move in self.MoveList:
			if move in AlarmTotal:
				self.Alarm = True

	def Setprinter(self):
		msg = "!!!" if self.Alarm == True else ""
		print(f'{msg:>3}',f'{self.Name:>13}',f'{np.round(self.LocalOdds,6):>9}',f'{self.Item:>13}',f'{self.Nature:>8}',f'{self.Move1:>13}',f'{self.Move2:>13}',f'{self.Move3:>13}',f'{self.Move4:>13}',f'{self.Speed:>6}')

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


#print("Adding Pokemon")

PokemonList = []
totalalarms = 0
for row in MovesetData["Name"]:

	Pokemon = PokemonSet(row)
	if Pokemon.Entry <= 1000:
		PokemonList.append(Pokemon)
		if Pokemon.Alarm == True:
			totalalarms += 1



#print("All Pokemon added")
printline()


printline()
print("First Pokemon")
print("What is the Pokemon's Ability?")
pokemon1_ability = input()
if pokemon1_ability == '':
	exit()
pokemon1_ability = pokemon1_ability.title()


print("What is the Pokemon's Nature?")
pokemon1_nature = input()
if pokemon1_nature == '':
	exit()
pokemon1_nature = pokemon1_nature.title()

print("What is the Pokemon's Item?")
pokemon1_item = input()
if pokemon1_nature == '':
	exit()
pokemon1_item = pokemon1_item.title()

if pokemon1_item == "King'S Rock":
	newitem = "King's Rock"
	pokemon1_item = newitem


printline()

pokemon1_List =[]

for pokemon in PokemonList:
	if (pokemon1_ability == pokemon.Ability1 or pokemon1_ability == pokemon.Ability2) and pokemon1_item == pokemon.Item and pokemon1_nature ==pokemon.Nature:
		pokemon1_List.append(pokemon)





printline()
print("Second Pokemon")
print("What is the Pokemon's Ability?")
pokemon2_ability = input()
if pokemon2_ability == '':
	exit()
pokemon2_ability = pokemon2_ability.title()


print("What is the Pokemon's Nature?")
pokemon2_nature = input()
if pokemon2_nature == '':
	exit()
pokemon2_nature = pokemon2_nature.title()

print("What is the Pokemon's Item?")
pokemon2_item = input()
if pokemon2_item == '':
	exit()
pokemon2_item = pokemon2_item.title()

if pokemon2_item == "King'S Rock":
	newitem = "King's Rock"
	pokemon2_item = newitem

printline()

pokemon2_List =[]

for pokemon in PokemonList:
	if (pokemon2_ability == pokemon.Ability1 or pokemon2_ability == pokemon.Ability2) and pokemon2_item == pokemon.Item and pokemon2_nature ==pokemon.Nature:
		pokemon2_List.append(pokemon)


printline()

print("Last Pokemon")
print("What is the Pokemon's Ability?")
pokemon3_ability = input()
if pokemon3_ability == '':
	exit()
pokemon3_ability = pokemon3_ability.title()


print("What is the Pokemon's Nature?")
pokemon3_nature = input()
if pokemon3_nature == '':
	exit()
pokemon3_nature = pokemon3_nature.title()

print("What is the Pokemon's Item?")
pokemon3_item = input()
if pokemon3_item == '':
	exit()
pokemon3_item = pokemon3_item.title()

if pokemon3_item == "King'S Rock":
	newitem = "King's Rock"
	pokemon3_item = newitem

printline()

pokemon3_List =[]
for pokemon in PokemonList:
	if (pokemon3_ability == pokemon.Ability1 or pokemon3_ability == pokemon.Ability2) and pokemon3_item == pokemon.Item and pokemon3_nature ==pokemon.Nature:
		pokemon3_List.append(pokemon)



printline()
print("List of candidate Pokemon: \n\n")



allPokemon = pokemon1_List  + pokemon2_List + pokemon3_List

for pokemon in allPokemon:
	pokemon.Setprinter()
