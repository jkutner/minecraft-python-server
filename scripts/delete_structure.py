from mcpi.minecraft import Minecraft
import pycraft
import os
import pickle

	
def sortPair(val1, val2):
	if val1 > val2:
		return val2, val1
	else:
		return val1, val2

def demolishStructure(x1, y1, z1, x2, y2, z2):
	x1, x2 = sortPair(x1, x2)
	y1, y2 = sortPair(y1, y2)
	z1, z2 = sortPair(z1, z2)

	width = x2 - x1
	height = y2 - y1
	length = z2 - z1

	print("Height: %s" % height)
	print("Width: %s" % width)
	print("Length: %s" % length)
	x = ""
	while x not in ["y", "n"]:
		x = input("Are you sure? (y/n) > ")
	if x == "n":
		exit()

	#Copy the structure
	for row in range(height):
		for column in range(width):
			for depth in range(length):
				mc.setBlock(x1 + column, y1 + row, z1 + depth, 0, 0)

def main(mc, player):
	mc.postToChat("This program doesn't work from the in-game chat. Please move to your Python Terminal.")

if __name__ == "__main__":
	mc = pycraft.new_minecraft()
	player = pycraft.current_player(mc)
	
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

	demolishStructure(x1, y1, z1, x2, y2, z2)
