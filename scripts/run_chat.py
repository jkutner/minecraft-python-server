from mcpi.minecraft import Minecraft
from mcpi.minecraft import ChatEvent
import time
import pycraft
import importlib
import sys
from pycraft import Player
import threading

mc = pycraft.new_minecraft()

def run_in_background(func, mc, player, *args):
	player.unlock()

	# TODO check if the function accepts the correct args
	th = threading.Thread(target=func, kwargs={"mc": mc, "player": player})

	if player.lock():
		th.start()
	else:
		print("Failed to run func: %s" % func)

if __name__ == "__main__":
	while True:
		events = mc.events.pollChatPosts()
		if len(events) > 0:
			for e in events:
				if e.type is ChatEvent.POST:
					if e.message.startswith("python "):
						player = Player(mc.conn, e.entityId)
						script = e.message.replace("python ", "")
						if script == "stop":
							player.unlock()
						elif script == "whoami":
							player.log()
							mc.postToChat(player.info())
						else:
							try:
								print("Importing %s..." % script)
								importlib.import_module(script)
								func = sys.modules[script].main
								run_in_background(func, mc, player)
							except AttributeError:
								mc.postToChat("Script has no main function: %s" % script)
							except ModuleNotFoundError:
								mc.postToChat("Unknown script: %s" % script)
				else:
					print("Unknown event type: %s" % (e.type))
