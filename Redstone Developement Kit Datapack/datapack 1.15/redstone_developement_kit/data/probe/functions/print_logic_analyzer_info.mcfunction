#dispatch for the various report methods
execute as @s[tag=bit,tag=primary] at @s run function probe:bit/tools/print_logic_analyzer_info
execute as @s[tag=word,tag=primary] at @s run function probe:word/tools/print_logic_analyzer_info