from character import Character
from menus import Menu
from dice import Dice


def main():
    char = Character("character_stats.json")
    menu = Menu(char)

    while True:
        try:
            # returns an int
            while True:
                try:
                    user_weapon = menu.weapon_menu()
                    weapon_choice = weapon_selection(user_weapon)
                    break
                except ValueError:
                    print("Please select the number of the weapon you want to use")

            while True:
                try:
                    user_attack = menu.attack_menu()
                    attack_choice = attack_selection(user_attack)
                    break
                except ValueError:
                    print("Please select the number of the attack you want to use")

            weapon_stats = char.weapon_info(weapon_choice)

            # Combat
            attack_roll = roll_attack(weapon_stats, attack_choice)
            damage = roll_damage(weapon_stats, attack_roll)

            print(f"{damage}")

            restart = input("\nRoll again? (Y/N): ").lower()
            if restart == "y":
                continue
            elif restart == "n":
                return print("Thanks for playing!")
        except EOFError:
            return print("Thanks for playing!")


def weapon_selection(weapon_choice):
    match weapon_choice:
        case 1:
            return "short_sword"
        case 2:
            return "bow"
        case _:
            raise ValueError


def attack_selection(user_attack):
    match user_attack:
        case 1:
            return "Attack"
        case 2:
            return "Advantage Attack"
        case 3:
            return "Disadvantage Attack"
        case _:
            raise ValueError


def roll_attack(weapon_choice, attack_choice):
    w = weapon_choice

    print(f"\n{attack_choice} with {w['name']}")

    match attack_choice:
        case "Attack":
            roll = Dice.roll(1, 20)
            total_attack = roll["sum"] + w["hit"]

            # Check if attack crits
            if roll["sum"] == 20:
                return "crit hit"
            elif roll["sum"] == 1:
                return "crit fail"
            else:
                print(f"Attack roll ({roll['sum']}) + Weapon hit ({w['hit']})")
                print(f"\nAttack total: {total_attack}")
                return total_attack

        case "Advantage Attack":
            roll = Dice.roll(2, 20)
            total_attack = roll["highest"] + w["hit"]

            if roll["highest"] == 1 and roll["lowest"] == 1:
                return "super fail"
            elif roll["highest"] == 20 or roll["lowest"] == 20:
                return "crit hit"

            else:
                print(f"\nWith advantage you rolled: {roll['highest']}")
                print(f"Attack roll ({roll['highest']}) + Weapon hit ({w['hit']})")
                print(f"\nAttack total: {total_attack}")
                return total_attack

        case "Disadvantage Attack":
            roll = Dice.roll(2, 20)
            total_attack = roll["lowest"] + w["hit"]

            if roll["lowest"] == 20 and roll["lowest"] == 20:
                return "crit hit"
            elif roll["highest"] == 1 or roll["lowest"] == 1:
                return "crit fail"
            else:
                print(f"\nWith disadvantage you rolled: {roll['lowest']}")
                print(f"Attack roll ({roll['lowest']}) + Weapon hit ({w['hit']})")
                print(f"\nAttack total: {total_attack}")
                return total_attack
        case _:
            print("error")


def roll_damage(weapon_choice, attack_roll):
    w = weapon_choice

    match attack_roll:
        case "crit hit":
            print("\nCritical hit!")
            print("")
            damage_roll = Dice.roll(2, w["dice"])
            damage_total = damage_roll["sum"] + w["ability_mod"]
            print(f"Damage rolls ({damage_roll['sum']}) + Ability Mod ({w['ability_mod']})")

            return f"\nDamage total = {damage_total}"
        case "crit fail":
            return "\nCritical miss!"
        case "super fail":
            return "\nCritical miss!"
        case _:
            while True:
                try:
                    hit = input("\nDid your attack hit? (Y/N): ").lower()
                    print()

                    if hit == "y":
                        damage_roll = Dice.roll(1, w["dice"])
                        damage_total = damage_roll["sum"] + w["ability_mod"]
                        print(f"Damage roll ({damage_roll['sum']}) + Ability Mod ({w['ability_mod']})")
                        return f"\nDamage total = {damage_total}"
                    elif hit == "n":
                        return "Better luck next time!"
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid input")


def weapon_data(char, weapon_choice):
    w_data = char.weapon_info(weapon_choice)
    return w_data


if __name__ == "__main__":
    main()
