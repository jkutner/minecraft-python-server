from mcpi.minecraft import Minecraft
import pycraft



if __name__ == "__main__":
	mc = pycraft.new_minecraft()
	player = pycraft.current_player(mc)
	pos = player.getTilePos()
	b = mc.getBlockWithData(-41, 1, 28)
	print(b)
	print(pos.x)
	print(pos.y)
	print(pos.z)
	print(b.data)