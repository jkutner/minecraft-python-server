from mcpi.minecraft import Minecraft
import pycraft
mc = pycraft.new_minecraft()

def main(mc, player, block_type = 0):
	player.log()
	air = 0
	water = 9
	while player.locked():
		pos = player.getTilePos()
		blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)

		if blockBelow != air and blockBelow != water:
			mc.setBlock(pos.x, pos.y -1, pos.z, int(block_type))

if __name__ == "__main__":
	player = pycraft.current_player(mc)
	block_type = input("Please enter your block id: ")
	main(mc, player, block_type)
