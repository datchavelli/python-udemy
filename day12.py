import os
import sys

player_health = 10

def drink_potion(player_health):
    potion_strength = 2
    player_health += potion_strength
    print(f"LOCAL: {player_health}")

drink_potion(player_health)
print(f"GLOBAL: {player_health}")

