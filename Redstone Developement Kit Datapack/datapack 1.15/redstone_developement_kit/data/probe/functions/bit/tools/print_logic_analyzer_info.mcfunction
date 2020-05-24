# bit:print_logic_analyzer_info

execute as @s at @s if score @s state matches 0 run tellraw @a ["",{"text":"time:"},{"score":{"name":"global","objective":"tick"}},{"text":",channel:"},{"selector":"@s"},{"text":",state:false"}]
execute as @s at @s if score @s state matches 1 run tellraw @a ["",{"text":"time:"},{"score":{"name":"global","objective":"tick"}},{"text":",channel:"},{"selector":"@s"},{"text":",state:true"}]