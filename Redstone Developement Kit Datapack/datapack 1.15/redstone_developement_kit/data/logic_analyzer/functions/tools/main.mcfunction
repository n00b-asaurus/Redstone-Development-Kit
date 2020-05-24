scoreboard players add @e[type=armor_stand,tag=probe,tag=primary] last_state 0
execute if score global run matches 1 run scoreboard players add global tick 1
execute if score global run matches 1 run execute as @e[type=armor_stand,tag=probe,tag=primary] at @s run function probe:read
execute if score global run matches 1 run execute as @e[type=armor_stand,tag=probe,tag=primary] at @s unless score @s last_state = @s state run function probe:print_logic_analyzer_info
execute if score global run matches 1 run execute as @e[type=armor_stand,tag=probe,tag=primary] at @s unless score @s last_state = @s state run scoreboard players operation @s last_state = @s state