from mcpi.minecraft import Minecraft
import pycraft
mc = pycraft.new_minecraft()
import time

count = 30
while count > 0:
	time.sleep(1)
	pos = mc.player.getPos()
	mc.setBlock(pos.x, pos.y, pos.z, 8)
	count -= 1