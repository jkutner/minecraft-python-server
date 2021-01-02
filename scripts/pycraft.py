from mcpi.minecraft import Minecraft
from os.path import join, dirname
from dotenv import load_dotenv
import os
import socket
import re
import sys
from mcpi.minecraft import CmdPositioner

def check_server(address, port):
	# Create a TCP socket
	s = socket.socket()
	print("Attempting to connect to %s on port %s" % (address, port))
	try:
		s.connect((address, port))
		print("Connected to %s on port %s" % (address, port))
		return True
	except Exception as e:
		print("Connection to %s on port %s failed: %s" % (address, port, e))
		return False
	finally:
		s.close()

def new_minecraft():
	if check_server("localhost", 4711):
		return Minecraft.create("localhost", 4711)
	elif check_server("0.0.0.0", 4711):
		return Minecraft.create("0.0.0.0", 4711)
	else:
		#todo - check that the dotenv file actually exists
		dotenv_path = join(dirname(__file__), '..', '.env')
		load_dotenv(dotenv_path)
		host = os.getenv("PYCRAFT_HOST")
		port = os.getenv("PYCRAFT_PORT")
		return Minecraft.create(host, int(port))

def new_player(mc, name):
	pid = mc.getPlayerEntityId(name)
	player = Player(mc.conn, pid)
	return player

class Player(CmdPositioner):
	"""Methods for the host (Raspberry Pi) player"""
	def __init__(self, connection, pid):
		CmdPositioner.__init__(self, connection, b"entity")
		self.conn = connection
		self.pid = pid

	def getPos(self):
		return CmdPositioner.getPos(self, self.pid)
	def setPos(self, *args):
		return CmdPositioner.setPos(self, self.pid, args)
	def getTilePos(self):
		return CmdPositioner.getTilePos(self, self.pid)
	def setTilePos(self, *args):
		return CmdPositioner.setTilePos(self, self.pid, args)
	def setDirection(self, *args):
		return CmdPositioner.setDirection(self, self.pid, args)
	def getDirection(self):
		return CmdPositioner.getDirection(self, self.pid)
	def setRotation(self, yaw):
		return CmdPositioner.setRotation(self, self.pid, yaw)
	def getRotation(self):
		return CmdPositioner.getRotation(self, self.pid)
	def setPitch(self, pitch):
		return CmdPositioner.setPitch(self, self.pid, pitch)
	def getPitch(self):
		return CmdPositioner.getPitch(self, self.pid)

	def getEntities(self, distance=10, typeId=-1):
		"""Return a list of entities near entity (distanceFromPlayerInBlocks:int, typeId:int) => [[entityId:int,entityTypeId:int,entityTypeName:str,posX:float,posY:float,posZ:float]]"""
		"""If distanceFromPlayerInBlocks:int is not specified then default 10 blocks will be used"""
		s = self.conn.sendReceive(b"player.getEntities", distance, typeId)
		entities = [e for e in s.split("|") if e]
		return [ [int(n.split(",")[0]), int(n.split(",")[1]), n.split(",")[2], float(n.split(",")[3]), float(n.split(",")[4]), float(n.split(",")[5])] for n in entities]

	def removeEntities(self, distance=10, typeId=-1):
		"""Remove entities all entities near entity (distanceFromPlayerInBlocks:int, typeId:int, ) => (removedEntitiesCount:int)"""
		"""If distanceFromPlayerInBlocks:int is not specified then default 10 blocks will be used"""
		return int(self.conn.sendReceive(b"player.removeEntities", distance, typeId))

	def pollBlockHits(self):
		"""Only triggered by sword => [BlockEvent]"""
		s = self.conn.sendReceive(b"player.events.block.hits")
		events = [e for e in s.split("|") if e]
		return [BlockEvent.Hit(*list(map(int, e.split(",")))) for e in events]

	def pollChatPosts(self):
		"""Triggered by posts to chat => [ChatEvent]"""
		s = self.conn.sendReceive(b"player.events.chat.posts")
		events = [e for e in s.split("|") if e]
		return [ChatEvent.Post(int(e[:e.find(",")]), e[e.find(",") + 1:]) for e in events]
	
	def pollProjectileHits(self):
		"""Only triggered by projectiles => [BlockEvent]"""
		s = self.conn.sendReceive(b"player.events.projectile.hits")
		events = [e for e in s.split("|") if e]
		results = []
		for e in events:
			info = e.split(",")
			results.append(ProjectileEvent.Hit(
				int(info[0]), 
				int(info[1]), 
				int(info[2]), 
				int(info[3]), 
				info[4],
				info[5]))
		return results

	def clearEvents(self):
		"""Clear the players events"""
		self.conn.send(b"player.events.clear")

	
if __name__ == "__main__":
	new_minecraft()