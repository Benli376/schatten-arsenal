# Shadows v0.8: remove old globally shared bossbars from existing saves.
bossbar remove shadow:wither
bossbar remove shadow:warden
bossbar remove shadow:knight
scoreboard objectives add shadow_timer dummy
team add shadow_legends
team modify shadow_legends color dark_purple
scoreboard players set #timer shadow_timer 0
tellraw @a {"text":"Schatten-Arsenal 0.8 geladen: neue Bossleisten und Boss-Drops!","color":"light_purple"}
