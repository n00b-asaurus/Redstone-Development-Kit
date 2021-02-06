summon minecraft:armor_stand ~ ~ ~ {Marker:1b,NoGravity:1b,Tags:["probe","word","secondary","new"]}
scoreboard players operation @e[type=armor_stand,tag=probe,tag=word,tag=secondary,tag=new] group = @s group
scoreboard players add @s weight 0
scoreboard players set @s[scores={weight=0}] weight 1
scoreboard players operation @s weight += @s weight
scoreboard players operation @e[type=armor_stand,tag=probe,tag=word,tag=secondary,tag=new] weight = @s weight
tag @e[type=armor_stand,tag=probe,tag=word,tag=secondary,tag=new] remove new
