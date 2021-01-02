from mcpi.minecraft import Minecraft
import pycraft
mc = pycraft.new_minecraft()


player = pycraft.new_player(mc, "DarkCarat")
block_type = input("Please enter your block id: ")
air = 0
water = 9
print(player.pid)
while True:
	pos = player.getTilePos()
	blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)

	if blockBelow != air and blockBelow != water:
		mc.setBlock(pos.x, pos.y -1, pos.z, int(block_type))
