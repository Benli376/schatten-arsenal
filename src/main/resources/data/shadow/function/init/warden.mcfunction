attribute @s minecraft:max_health base set 1024
data merge entity @s {Health:1024.0f}
team join shadow_legends @s
effect give @s minecraft:glowing 999999 0 true
attribute @s minecraft:attack_damage base set 40
tag @s add shadow_initialized
