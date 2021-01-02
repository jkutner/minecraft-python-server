from mcpi.minecraft import Minecraft
from os.path import join, dirname
from dotenv import load_dotenv
import os
import socket
import re
import sys

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
	
if __name__ == "__main__":
	new_minecraft()