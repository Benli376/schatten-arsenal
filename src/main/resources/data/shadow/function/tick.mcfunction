execute as @a if items entity @s armor.head schattenarsenal:shadow_helmet if items entity @s armor.chest schattenarsenal:shadow_chestplate if items entity @s armor.legs schattenarsenal:shadow_leggings if items entity @s armor.feet schattenarsenal:shadow_boots run function shadow:armor/tick
execute as @e[tag=shadow_wither,tag=!shadow_initialized] run function shadow:init/wither
execute as @e[tag=shadow_warden,tag=!shadow_initialized] run function shadow:init/warden
execute as @e[tag=shadow_knight,tag=!shadow_initialized] run function shadow:init/knight
scoreboard players add #timer shadow_timer 1
execute if score #timer shadow_timer matches 10.. run scoreboard players set #timer shadow_timer 0
execute if score #timer shadow_timer matches 0 as @e[tag=shadow_wither] at @s run particle minecraft:witch ~ ~1 ~ 0.7 0.9 0.7 0.05 10 normal
execute if score #timer shadow_timer matches 0 as @e[tag=shadow_wither] at @s run particle minecraft:dragon_breath ~ ~1 ~ 0.4 0.5 0.4 0.02 8 normal
execute as @e[tag=shadow_wither] at @s as @a[distance=..7,gamemode=survival] run effect give @s minecraft:wither 2 0 true
execute if score #timer shadow_timer matches 0 as @e[tag=shadow_warden] at @s run particle minecraft:witch ~ ~1 ~ 0.7 0.9 0.7 0.05 10 normal
execute if score #timer shadow_timer matches 0 as @e[tag=shadow_warden] at @s run particle minecraft:dragon_breath ~ ~1 ~ 0.4 0.5 0.4 0.02 8 normal
execute as @e[tag=shadow_warden] at @s as @a[distance=..7,gamemode=survival] run effect give @s minecraft:darkness 2 0 true
execute if score #timer shadow_timer matches 0 as @e[tag=shadow_knight] at @s run particle minecraft:witch ~ ~1 ~ 0.7 0.9 0.7 0.05 10 normal
execute if score #timer shadow_timer matches 0 as @e[tag=shadow_knight] at @s run particle minecraft:dragon_breath ~ ~1 ~ 0.4 0.5 0.4 0.02 8 normal
execute as @e[tag=shadow_knight] at @s as @a[distance=..7,gamemode=survival] run effect give @s minecraft:weakness 2 0 true
