# Redstone Development Kit Datapack
A collection of functions used for setting up probes and interfacing with the logic analyzer program.

## Installation
Currently there is only a datapack for 1.15, but other datapacks supporting other versions will be added to this folder.
Enter the folder pertaining to the version of minecraft you're using and copy the datapack into your .minecraft folder.

## Creating a Bit Probe
Stand in the location you want to place the probe, it's important that you are standing above redstone dust and not a repeater, torch, or an empty space that a block will get pushed into. Currently the probe only recognizes powered and unpowered redstone dust.
Type the command `/function probe:bit/create` in chat. A `>Summon Probe<` prompt will appear. Click it and the command 
`/summon minecraft:armor_stand ~ ~ ~ {CustomName:"\"PLACE_NAME_HERE\"",CustomNameVisible:1b,Marker:1b,NoGravity:1b,Tags:["probe","bit","primary"]}`
will appear in the chat.
Replace the PLACE_NAME_HERE placeholder with the name of the probe and hit enter. The probe will be summoned to you location.

## Destroying a Bit Probe
Type the command `/function probe:bit/destroy` in chat. A `>Kill Probe<` prompt will appear. Click it and the command `/kill @e[type=minecraft:armor_stand,name="PLACE_NAME_HERE"]` will appear in the chat.
Replace the PLACE_NAME_HERE placeholder with the name of the probe and hit enter. The probe will be destroyed.

## Creating a Word Probe
Stand in the location you want to place the least significant bit probe, it's important that you are standing above redstone dust and not a repeater, torch, or an empty space that a block will get pushed into. Currently the probe only recognizes powered and unpowered redstone dust.
Type the command `/function probe:word/create` in chat. Three prompt will appear. 

Click `>Summon LSB Probe<` and the command 
`/summon minecraft:armor_stand ~ ~ ~ {CustomName:"\"PLACE_NAME_HERE\"",CustomNameVisible:1b,Marker:1b,NoGravity:1b,Tags:["probe","word","primary"]}`
will appear in the chat.
Replace the PLACE_NAME_HERE placeholder with the name of the probe and hit enter. The least significant bit probe will be summoned to you location.

Click `>Initiate LSB Probe<` and the command
`/scoreboard players operation @e[type=minecraft:armor_stand,name="PLACE_NAME_HERE"] group = global group_total`
Will appear in the chat.
Replace the PLACE_NAME_HERE placeholder with the name of the probe and hit enter. The least significant bit probe will be initiallized and ready to pair with the subsequent probes.

Stand in the location you want the next probe to go.
Click `>Summon Secondary Probe<` and the command
`/execute as @e[type=minecraft:armor_stand,name="PLACE_NAME_HERE"] at YOUR_NAME_HERE run function probe:word/tools/create_secondary`
will appear in the chat.
Replace the PLACE_NAME_HERE placeholder with the name of the probe, replace the YOUR_NAME_HERE with your in-game name, and hit enter.
Repeat this step for all remaining bits in the bus. Number of bits must not exceed 32.

## Destroying a Word Probe
Currently unsupported, feature to be added.

## Using the Logic Analyzer
Type `/function logic_analyzer:commands/start` to begin analyzing your circuit.
During this time, all probes will report to the chat any state changes they detect.
Type `/function logic_analyzer:commands/stop` when you've finished analyzing your circuit.
It is important that you stop the logic analyzer before running the logic analyzer program, as the program looks for the start and stop command in the log to determine the bounds of the data.
