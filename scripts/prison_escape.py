from mcpi.minecraft import Minecraft
import time
import os
import pickle
import pycraft

def main(mc, player):
	mc.postToChat("Loading Prison...")
	start_position = player.getTilePos()
	load_prison(mc, player, start_position)
	mc.postToChat("Done!")
	player.setTilePos(start_position.x + 8, start_position.y + 1, start_position.z + 4)
	mc.spawnEntity(start_position.x + 8, start_position.y + 1, start_position.z + 8, 120)
	while True:
		time.sleep(1)
		pos = player.getTilePos()
		if pos.x == start_position.x + 8:
			mc.postToChat("You are 8 blocks away. Congratulations!")
		elif pos.x == start_position.x - 8:
			mc.postToChat("You are 8 blocks away. Congratulations!")
		elif pos.z == start_position.z + 8:
			mc.postToChat("You are 8 blocks away. Congratulations!")
		elif pos.z == start_position.z - 8:
			mc.postToChat("You are 8 blocks away. Congratulations!")
		else:
			mc.postToChat("You are not 8 blocks away. How rude.")

def load_prison(mc, player, pos):
	structurefile = open(os.path.join("data", "prison1.dat"), "rb")
	structure = pickle.load(structurefile)
	x = pos.x
	y = pos.y
	z = pos.z
	buildStructure(mc, x, y, z, structure)

def buildStructure(mc, x, y, z, structure):
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

if __name__ == "__main__":
	mc = pycraft.new_minecraft()
	player = pycraft.current_player(mc)
	main(mc, player)
