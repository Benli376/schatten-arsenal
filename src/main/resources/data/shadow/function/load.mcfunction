scoreboard objectives add shadow_timer dummy
scoreboard objectives add shadow_boss dummy
bossbar add shadow:wither {"text":"Violetter Schatten-Wither","color":"dark_purple","bold":true}
bossbar add shadow:warden {"text":"Schatten-Warden","color":"dark_purple","bold":true}
bossbar add shadow:knight {"text":"Schattenritter","color":"dark_purple","bold":true}
bossbar set shadow:wither max 1024
bossbar set shadow:warden max 1024
bossbar set shadow:knight max 1024
bossbar set shadow:wither color purple
bossbar set shadow:warden color purple
bossbar set shadow:knight color purple
scoreboard players set #timer shadow_timer 0
tellraw @a {"text":"Schatten-Arsenal ist geladen! /function shadow:give/all","color":"light_purple"}
