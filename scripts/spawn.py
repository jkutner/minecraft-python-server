from mcpi.minecraft import Minecraft
import pycraft

entities = {
	"horse": 100,
	"villager": 120,
	"end_crystal": 200,
	"xp": 2,
	"area_effect_cloud": 3,
	"elder_guardian": 4,
	"wither skeleton": 5,
	"stray": 6,
	"egg": 7,
	"arrow": 10,
	"snowball": 11,
	"fireball": 12,
	"small_fireball": 13,
	"ender_pearl": 14,
	"eye_of_ender": 15,
	"bottle_of_xp": 17,
	"wither_skull": 19,
	"tnt": 20,
	"husk": 23,
	"spectral_arrow": 24,
	"shulker_bullet": 25,
	"dragon_fireball": 26,
	"zombie_villager": 27
}

def main(mc, player, entity = 2):
	type_id = 100
	try:
		type_id = entities[str(entity).lower()]
	except KeyError:
		mc.postToChat("I don't know what %s is, so here is a horse." % entity)
	pos = player.getTilePos()
	mc.spawnEntity(pos.x, pos.y, pos.z + 2, type_id)
	print(player.getEntities())

if __name__ == "__main__":
	mc = pycraft.new_minecraft()
	player = pycraft.current_player(mc)
	entity_type = input("Please enter your entity id: ")
	main(mc, player, entity_type)