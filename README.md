# Pycraft

This repo creates a Docker image for a Minecraft server that's ready to use with Python.

## Usage

You can run the published version of this image by executing the command:

```
> docker run -it -e JAVA_TOOL_OPTIONS="-Xmx2g" -p 4711:4711 -p 25566:25566 jkutner/pycraft
```

Then open Minecraft, and select "Multiplayer" and "Direct Connection". Enter the address `localhost:25566` as the "Server Address" and click "Join Server".

Then start a Python shell and run:

```
> python
Python 3.9.1 (default, Dec 10 2020, 10:36:35)
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.getBlock(0,0,0)
1
>>> exit()
```
