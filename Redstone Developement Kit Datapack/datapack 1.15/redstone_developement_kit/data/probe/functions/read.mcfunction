#dispatch for the various read methods
execute as @s[tag=bit,tag=primary] at @s run function probe:bit/tools/read
execute as @s[tag=word,tag=primary] at @s run function probe:word/tools/read
