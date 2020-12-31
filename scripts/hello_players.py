from mcpi.minecraft import Minecraft

mc = Minecraft.create()

for pid in mc.getPlayerEntityIds():
    name = mc.entity.getName(pid)
    mc.postToChat(f'Hello {name}!')
