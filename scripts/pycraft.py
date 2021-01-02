from mcpi.minecraft import Minecraft
from os.path import join, dirname
from dotenv import load_dotenv
import os
import socket
import re
import sys
from mcpi.minecraft import CmdEntity

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

class Player(CmdEntity):
	"""Methods for a player"""
	def __init__(self, connection, pid):
		CmdEntity.__init__(self, connection)
		self.pid = pid

	def getPos(self):
		return CmdEntity.getPos(self, self.pid)
	def setPos(self, *args):
		return CmdEntity.setPos(self, self.pid, args)
	def getTilePos(self):
		return CmdEntity.getTilePos(self, self.pid)
	def setTilePos(self, *args):
		return CmdEntity.setTilePos(self, self.pid, args)
	def setDirection(self, *args):
		return CmdEntity.setDirection(self, self.pid, args)
	def getDirection(self):
		return CmdEntity.getDirection(self, self.pid)
	def setRotation(self, yaw):
		return CmdEntity.setRotation(self, self.pid, yaw)
	def getRotation(self):
		return CmdEntity.getRotation(self, self.pid)
	def setPitch(self, pitch):
		return CmdEntity.setPitch(self, self.pid, pitch)
	def getPitch(self):
		return CmdEntity.getPitch(self, self.pid)
	def getEntities(self, distance=10, typeId=-1):
		return CmdEntity.getEntities(self. self.pid, distance=10, typeId=-1)
	def removeEntities(self, distance=10, typeId=-1):
		return CmdEntity.removeEntities(self. self.pid, distance=10, typeId=-1)

if __name__ == "__main__":
	new_minecraft()
