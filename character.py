import json
import math


class Character:
    def __init__(self, file_name):
        self.file_name = file_name

    # Imports character json file
    def import_stats(self):
        with open(self.file_name, "r") as json_file:
            character_data = json.load(json_file)
        # To add.. character stat and equipment input flow
        return character_data

    # Calculates ability modifiers from char ability scores
    def ability_mod_calc(self):
        ability_scores = Character.import_stats(self)["ability_scores"]

        ability_mods = {}
        for ability in ability_scores:
            ability_mod = math.floor((ability_scores[ability] - 10) / 2)
            ability_mods[ability] = ability_mod

        return ability_mods

    def weapon_info(self, weapon):
        char_data = Character.import_stats(self)                        # full character_stats file
        ability_mods = Character.ability_mod_calc(self)                 # ability modifiers (not in json file)
        user_weap = Character.import_stats(self)["equipment"][weapon]   # user weapon choice
        prof_bonus = char_data["proficiency_bonus"]                     # proficiency bonus
        weap_ab_mod = user_weap["modifier"]                             # weapon ability mod name (dex/str/etc.)
        ability_mod = ability_mods[weap_ab_mod]                         # weapon ability mod number
        weapon_dice = user_weap["dice"]                                 # weapon damage dice
        weapon_name = user_weap["name"]
        calc_text = f"Prof bonus ({prof_bonus}) + Ability mod ({ability_mod})"

        if "fighting_style" in user_weap:
            style_mod = user_weap["fighting_style"]
            weapon_hit = prof_bonus + ability_mod + style_mod           # weapon hit modifier
        else:
            weapon_hit = prof_bonus + ability_mod                       # weapon hit modifier

        weapon_data = {
            "name": weapon_name,
            "hit": weapon_hit,
            "dice": weapon_dice,
            "ability_mod": ability_mod,
            "calc_text": calc_text
        }

        return weapon_data
