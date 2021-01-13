from mcpi.minecraft import Minecraft
import pycraft

def main(mc, player, entity_type = 2):
	player.log()
	pos = player.getTilePos()
	mc.spawnEntity(pos.x, pos.y, pos.z + 2, int(entity_type))
	print(player.getEntities())

if __name__ == "__main__":
	mc = pycraft.new_minecraft()
	player = pycraft.current_player(mc)
	entity_type = input("Please enter your entity id: ")
	main(mc, player, entity_type)