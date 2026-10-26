execute as @a if items entity @s armor.head schattenarsenal:shadow_helmet if items entity @s armor.chest schattenarsenal:shadow_chestplate if items entity @s armor.legs schattenarsenal:shadow_leggings if items entity @s armor.feet schattenarsenal:shadow_boots run function shadow:armor/tick
execute as @e[tag=shadow_wither,tag=!shadow_initialized] run function shadow:init/wither
execute as @e[tag=shadow_warden,tag=!shadow_initialized] run function shadow:init/warden
execute as @e[tag=shadow_knight,tag=!shadow_initialized] run function shadow:init/knight
scoreboard players add #timer shadow_timer 1
execute if score #timer shadow_timer matches 100.. run scoreboard players set #timer shadow_timer 0
execute if entity @e[tag=shadow_wither] run bossbar set shadow:wither visible true
execute unless entity @e[tag=shadow_wither] run bossbar set shadow:wither visible false
execute if entity @e[tag=shadow_wither] run bossbar set shadow:wither players @a
execute as @e[tag=shadow_wither,limit=1] store result bossbar shadow:wither value run data get entity @s Health 1
execute at @e[tag=shadow_wither] run particle minecraft:witch ~ ~1 ~ 0.6 0.8 0.6 0.01 3 force
execute if score #timer shadow_timer matches 0 at @e[tag=shadow_wither] run particle minecraft:dragon_breath ~ ~1 ~ 0.8 0.8 0.8 0.04 35 force
execute at @e[tag=shadow_wither] as @a[distance=..7,gamemode=survival] run effect give @s minecraft:wither 2 0 true
execute unless entity @e[tag=shadow_wither] if score #wither shadow_boss matches 1 run function shadow:reward/wither
execute if entity @e[tag=shadow_warden] run bossbar set shadow:warden visible true
execute unless entity @e[tag=shadow_warden] run bossbar set shadow:warden visible false
execute if entity @e[tag=shadow_warden] run bossbar set shadow:warden players @a
execute as @e[tag=shadow_warden,limit=1] store result bossbar shadow:warden value run data get entity @s Health 1
execute at @e[tag=shadow_warden] run particle minecraft:witch ~ ~1 ~ 0.6 0.8 0.6 0.01 3 force
execute if score #timer shadow_timer matches 0 at @e[tag=shadow_warden] run particle minecraft:dragon_breath ~ ~1 ~ 0.8 0.8 0.8 0.04 35 force
execute at @e[tag=shadow_warden] as @a[distance=..7,gamemode=survival] run effect give @s minecraft:darkness 2 0 true
execute unless entity @e[tag=shadow_warden] if score #warden shadow_boss matches 1 run function shadow:reward/warden
execute if entity @e[tag=shadow_knight] run bossbar set shadow:knight visible true
execute unless entity @e[tag=shadow_knight] run bossbar set shadow:knight visible false
execute if entity @e[tag=shadow_knight] run bossbar set shadow:knight players @a
execute as @e[tag=shadow_knight,limit=1] store result bossbar shadow:knight value run data get entity @s Health 1
execute at @e[tag=shadow_knight] run particle minecraft:witch ~ ~1 ~ 0.6 0.8 0.6 0.01 3 force
execute if score #timer shadow_timer matches 0 at @e[tag=shadow_knight] run particle minecraft:dragon_breath ~ ~1 ~ 0.8 0.8 0.8 0.04 35 force
execute at @e[tag=shadow_knight] as @a[distance=..7,gamemode=survival] run effect give @s minecraft:weakness 2 0 true
execute unless entity @e[tag=shadow_knight] if score #knight shadow_boss matches 1 run function shadow:reward/knight
