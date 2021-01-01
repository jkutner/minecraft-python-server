from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = 57
height = 175
levels = reversed(range(height))

pos = mc.player.getTilePos()
x, y, z = pos.x + height, pos.y, pos.z

for level in levels:
	mc.setBlocks(x - level, y, z - level, x + level, y, z + level, block)
	y += 1