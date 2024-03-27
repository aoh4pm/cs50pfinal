from tabulate import tabulate


class Menu:
    # Passes in json file from project.py main()
    def __init__(self, file):
        self.file = file

    # Creates weapon select menu
    def weapon_menu(self):
        # char = self.file                          # char json
        stats = self.file.import_stats()            # char import stats
        equipment = stats["equipment"]              # equipment dict w/weapons
        header = ["Weapon", "Hit", "Damage"]        # tabulate header
        table = []                                  # table for weap choices
        choice_list = []                            # list of weapon dicts

        # This loop will iterate over the items in the equipment dict
        # Store the weap menu text into a list for each weap
        # Store the weap info and number choice into list
        count = 0
        for item in equipment:
            # w short for weapon
            count += 1
            w = self.file.weapon_info(item)         # stores weapon_info dict in w
            w_name = w["name"]                      # stores weapon names
            w_hit = w["hit"]
            w_dice = w["dice"]
            calc_text = w["calc_text"]

            w_choice = [f"({count}) {w_name}", f"+{w_hit} ({calc_text})", f"1d{w_dice}"]
            table.append(w_choice)                  # storing menu choice info into table
            choice_list.append({count: w})          # storing choice dicts into list

        print(f"\nCombat: {stats['name'].title()}")
        print(tabulate(table, header, tablefmt="simple"))

        user_select = int(input("\nChoose your weapon: "))
        return user_select

    @staticmethod
    def attack_menu():
        # header = ["Weapon", "Hit", "Damage"]
        table = [
            ["(1) Attack"],
            ["(2) Attack with Advantage"],
            ["(3) Attack with Disadvantage"]]

        print("\nWhat kind of attack are you making?")
        print(tabulate(table, tablefmt="simple"))

        user_select = int(input("\nChoose your attack: "))
        return user_select
