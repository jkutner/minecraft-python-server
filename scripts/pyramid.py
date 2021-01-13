from mcpi.minecraft import Minecraft
import pycraft

def main(mc, player, block = 46, height = 10):		
	levels = reversed(range(height))

	pos = mc.player.getTilePos()
	x, y, z = pos.x + height, pos.y, pos.z

	for level in levels:
		mc.setBlocks(x - level, y, z - level, x + level, y, z + level, int(block))
		y += 1

if __name__ == "__main__":
	mc = pycraft.new_minecraft()
	player = pycraft.current_player(mc)
	block_type = input("Please enter your block id: ")
	main(mc, player, block_type)