from mcpi.minecraft import Minecraft
from mcpi.minecraft import ChatEvent
import time
import pycraft
import importlib
import sys
from pycraft import Player
import threading

mc = pycraft.new_minecraft()

def run_in_background(func, *args):
	th = threading.Thread(target=func,args=args)
	th.start()

while True:
	events = mc.events.pollChatPosts()
	if len(events) > 0:
		for e in events:
			if e.type is ChatEvent.POST:
				if e.message.startswith("python "):
					player = Player(mc.conn, e.entityId)
					script = e.message.replace("python ", "")
					try:
						print("Importing %s..." % script)
						importlib.import_module(script)
						run_in_background(sys.modules[script].main, mc, player)
					except ModuleNotFoundError:
						mc.postToChat("Unknown script: %s" % script)
			else:
				print("Unknown event type: %s" % (e.type))
