from mcpi.minecraft import Minecraft
import pycraft
import os
import pickle

	
def sortPair(val1, val2):
	if val1 > val2:
		return val2, val1
	else:
		return val1, val2

def copyStructure(x1, y1, z1, x2, y2, z2):
	x1, x2 = sortPair(x1, x2)
	y1, y2 = sortPair(y1, y2)
	z1, z2 = sortPair(z1, z2)

	width = x2 - x1
	height = y2 - y1
	length = z2 - z1

	structure = []

	print("Please wait...")

	#Copy the structure
	for row in range(height):
		structure.append([])
		for column in range(width):
			structure[row].append([])
			for depth in range(length):
				block = mc.getBlockWithData(x1 + column, y1 + row, z1 + depth)
				structure[row][column].append(block)

	return structure

def main(mc, player):
	mc.postToChat("This program doesn't work from the in-game chat. Please move to your Python Terminal.")

if __name__ == "__main__":
	mc = pycraft.new_minecraft()
	player = pycraft.current_player(mc)
	
	filename = input("What is the name of your structure? > ")
	#todo: change spaces to underscores in file name
	input("Move to the first position and press ENTER in this window")
	pos1 = player.getTilePos()

	x1 = pos1.x
	y1 = pos1.y
	z1 = pos1.z

	input("Move to the opposite corner and press ENTER in this window")
	pos2 = player.getTilePos()

	x2 = pos2.x
	y2 = pos2.y
	z2 = pos2.z

	structure = copyStructure(x1, y1, z1, x2, y2, z2)

	structurefile = open(os.path.join("data", "%s.dat" % filename), "wb")
	pickle.dump(structure, structurefile)
	