from mcpi.minecraft import Minecraft
from mcpi.minecraft import ChatEvent
import time
import pycraft
import importlib
import sys
from pycraft import Player
import threading

mc = pycraft.new_minecraft()

def run_in_background(func, mc, player, kwargs):
	player.unlock()

	# TODO check if the function accepts the correct args
	default_args = {"mc": mc, "player": player}
	th = threading.Thread(target=func, kwargs={**default_args, **kwargs})

	if player.lock():
		th.start()
	else:
		print("Failed to run func: %s" % func)

def print_help(mc):
	mc.postToChat("Please provide the name of a script in addition.")

def parse_kwargs(mc, command):
	kwargs={}
	if len(command) > 2:
		args = command[2:]
		for arg in args:
			kv = arg.split("=")
			if len(kv) == 2:
				kwargs[kv[0]] = kv[1]
			else:
				mc.postToChat("Invalid arg: %s" % arg)
	return kwargs

def handle_chat_event(event):
	if e.message.startswith("python "):
		player = Player(mc.conn, e.entityId)
		command = e.message.split()
		if len(command) < 2:
			print_help(mc)
		else:
			script = command[1]
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

					kwargs = parse_kwargs(mc, command)

					print("Running function main(%s)..." % kwargs)
					run_in_background(func, mc, player, kwargs)
				except AttributeError:
					mc.postToChat("Script has no main function: %s" % script)
				except ModuleNotFoundError:
					mc.postToChat("Unknown script: %s" % script)

if __name__ == "__main__":
	while True:
		try:
			time.sleep(1)
			events = mc.events.pollChatPosts()
			if len(events) > 0:
				for e in events:
					if e.type is ChatEvent.POST:
						handle_chat_event(e)
					else:
						print("Unknown event type: %s" % (e.type))
		except:
			time.sleep(1)
			print("Recovering from error")
