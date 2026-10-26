attribute @s minecraft:max_health base set 1024
data merge entity @s {Health:1024.0f}
scoreboard players set #wither shadow_boss 1
tag @s add shadow_initialized
