# Redstone Development  Kit
A collection of tools used to develop, test, and troubleshoot redstone circuits

## Current Supported Minecraft Versions
Minecraft Java Edition 1.15 

## Developers Requirements
Python 3.8
JDK9 (If you're updating the Structure Generator Java Module)

## Modules
### Redstone Development Kit Datapack
A datapack containing all minecraft-end tools.
Current tools included:
* Probe - functions for adding or removing redstone probes
* Logic Analyzer - functions for controlling the logic analyzer data collection

### Redstone Logic Analyzer Tool
A python program for collecting information logic information from the games log file and turning it into an image.

### Redstone Structure Generator Tool
A python program for generating useful redstone structures.
Current structures include:
* Basic Encoder - takes a .txt file and generates a basic horizontal encoder
* Properinglish19 Decoder - takes a .txt file and generates a compact decoder, generation is kinda slow.
* Stenodyon Decoder - takes a .txt file and generates a slightly less compact decoder, generation works much faster

### Redstone Structure Generator Java Module
A java support module used to type console commands into minecraft.
Currently the only way I can reliably get commands from the structure generator program to minecraft.
Ideally, I would like to get rid of it and replace it with a python equivalent. 
