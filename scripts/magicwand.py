from mcpi.minecraft import Minecraft
import pycraft
mc = pycraft.new_minecraft()
player = pycraft.current_player(mc)
import time

# time.sleep(10)

# hits = mc.events.pollBlockHits()
# block = 103

# for hit in hits:
# 	print(hit)
# 	x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
# 	mc.setBlock(x, y, z, block)

while True:
	time.sleep(2)
	hits = player.pollBlockHits()
	for hit in hits:
		print(hit)