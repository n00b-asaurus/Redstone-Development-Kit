scoreboard players set @s state 0
function probe:tools/add_if_powered_block
scoreboard players operation @s state *= @s weight
execute as @e[type=armor_stand,tag=word,tag=primary] at @s run scoreboard players operation @s group_difference = @s group
scoreboard players operation @e[type=armor_stand,tag=word,tag=primary] group_difference -= @s group
scoreboard players operation @e[type=armor_stand,scores={group_difference=0},tag=word,tag=primary] state += @s state
