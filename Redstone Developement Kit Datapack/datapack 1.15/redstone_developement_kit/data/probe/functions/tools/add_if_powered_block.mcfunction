#adds 1 to the probes state if powered blocks are detected

execute as @s at @s unless block ~ ~ ~ minecraft:redstone_wire[power=0] run scoreboard players add @s state 1