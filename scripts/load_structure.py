from mcpi.minecraft import Minecraft
import pycraft
import os
import pickle

def buildStructure(x, y, z, structure):
	xStart = x
	zStart = z
	for row in structure:
		for column in row:
			for block in column:
				mc.setBlock(x, y, z, block.id, block.data)
				z += 1
			x += 1
			z = zStart
		y += 1
		x = xStart

def main(mc, player):
	mc.postToChat("This program doesn't work from the in-game chat. Please move to your Python Terminal.")

if __name__ == "__main__":
	mc = pycraft.new_minecraft()
	#todo: Make this a current_player function
	pycraft.load_env()
	player_name = os.getenv("PLAYER_NAME")
	player = mc.player
	if not player_name is None:
		player = pycraft.new_player(mc, player_name)
	
	filename = input("What is the name of your structure? >")
	structurefile = open(os.path.join("data", "%s.dat" % filename), "rb")
	structure = pickle.load(structurefile)
	pos = player.getTilePos()
	x = pos.x
	y = pos.y
	z = pos.z
	buildStructure(x, y, z, structure)
