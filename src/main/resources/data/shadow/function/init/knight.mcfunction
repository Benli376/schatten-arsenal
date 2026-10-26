attribute @s minecraft:max_health base set 1024
data merge entity @s {Health:1024.0f}
team join shadow_legends @s
effect give @s minecraft:glowing 999999 0 true
attribute @s minecraft:attack_damage base set 36
item replace entity @s weapon.mainhand with schattenarsenal:shadow_sword
item replace entity @s armor.head with schattenarsenal:shadow_helmet
item replace entity @s armor.chest with schattenarsenal:shadow_chestplate
item replace entity @s armor.legs with schattenarsenal:shadow_leggings
item replace entity @s armor.feet with schattenarsenal:shadow_boots
tag @s add shadow_initialized
