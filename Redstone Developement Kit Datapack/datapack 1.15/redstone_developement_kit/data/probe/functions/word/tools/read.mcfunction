scoreboard players set @s state 0
execute as @e[type=armor_stand,tag=word,tag=secondary] at @s run scoreboard players operation @s group_difference = @s group
scoreboard players operation @e[type=armor_stand,tag=word,tag=secondary] group_difference -= @s group
execute as @e[type=armor_stand,scores={group_difference=0},tag=word,tag=secondary] at @s run function probe:word/tools/read_secondary
function probe:tools/add_if_powered_block
