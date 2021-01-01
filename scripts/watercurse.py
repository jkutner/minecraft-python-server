from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

count = 30
while count > 0:
	time.sleep(1)
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y, pos.z, 8)
	count -= 1