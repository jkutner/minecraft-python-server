from mcpi.minecraft import Minecraft
from scripts import pycraft
import code
mc = pycraft.new_minecraft()

mods = dict(pycraft = pycraft, Minecraft = Minecraft, mc = mc)
code.interact(local = mods)