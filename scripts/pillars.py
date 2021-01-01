from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def setPillar(x, y, z, height):
	stairBlock = 156
	block = 155

	#Pillar top
	mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1, block, 1)
	mc.setBlock(x - 1, y + height - 1, z, stairBlock, 12)
	mc.setBlock(x + 1, y + height - 1, z, stairBlock, 13)
	mc.setBlock(x, y + height - 1, z + 1, stairBlock, 15)
	mc.setBlock(x, y + height - 1, z - 1, stairBlock, 14)

	#Pillar base
	mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, block, 1)
	mc.setBlock(x - 1, y + 1, z, stairBlock, 0)
	mc.setBlock(x + 1, y + 1, z, stairBlock, 1)
	mc.setBlock(x, y + 1, z + 1, stairBlock, 3)
	mc.setBlock(x, y + 1, z - 1, stairBlock, 2)

	#Pillar column
	mc.setBlocks(x, y, z, x, y + height, z, block, 2)

pos = mc.player.getTilePos()
x, y, z = pos.x + 2, pos.y, pos.z


for item in range(5, 105, 5):
	setPillar(x + 5, y, z, 12)