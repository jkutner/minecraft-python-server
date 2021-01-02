from mcpi.minecraft import Minecraft
import pycraft
mc = pycraft.new_minecraft()
for pid in mc.getPlayerEntityIds():
    name = mc.entity.getName(pid)
    mc.postToChat(f'Hello {name}!')
