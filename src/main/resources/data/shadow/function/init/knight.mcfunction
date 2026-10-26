attribute @s minecraft:max_health base set 1024
data merge entity @s {Health:1024.0f}
attribute @s minecraft:attack_damage base set 40
item replace entity @s weapon.mainhand with schattenarsenal:shadow_sword[enchantments={"minecraft:sharpness":50}]
item replace entity @s armor.chest with schattenarsenal:shadow_chestplate
scoreboard players set #knight shadow_boss 1
tag @s add shadow_initialized
