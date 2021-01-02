from mcpi.minecraft import Minecraft
from mcpi.minecraft import ChatEvent

import pycraft
mc = pycraft.new_minecraft()

while True:
	events = mc.events.pollChatPosts()
	if len(events) > 0:
		for e in events:
			if e.type is ChatEvent.POST:
				name = mc.entity.getName(e.entityId)
				mc.postToChat(f'hey {name}, me no understand "{e.message}"')