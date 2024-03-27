 # Dungeons and Dragons Combat Roller
    #### Video Demo: https://youtu.be/JjqkbxEAFCM?si=Jbf7jLZq7ttnLg-U
    #### Description:
    This is a program that allows a user to import their Dungeons and Dragons (DnD) player character stats
    and weapons, and automatically calculate their attack and damage rolls for that character during combat.

    In DnD combat, a player makes an attack by rolling several dice to calculate the outcome of their action.
    - 1d20 - One twenty sided dice that determines if the player's attack hits or misses
    - 1 Weapon Dice - One dice that determines how much damage a player's attack does when it hits
    The type of dice varies based on the weapon being used.
        - Example: Short Sword attacks roll 1d6 to determine damage

    There are three kinds of attacks a player can make
        - Attack
        - Attack with advantage - Roll 2d20 and take the **higher** of the two rolls
        - Attack with disadvantage - Roll 2d20 and take the **lower** of the two rolls

    Additionally there are three outcomes of a player's attack
        - Hit - Roll 1 damage dice
        - Critical hit - Roll two damage dice
        - Miss/Critical miss - Roll no damage

    A player character's abilities, such as Strength or Dexterity, are also added
    to their attack and damage rolls

    This program will take a user's character stats, convert the stats into attack and damage modifiers,
    and simulate attack and damage rolls using the ```random``` library.


    DnD Combat formulas:
    - Ability modifier = (Ability score - 10) / 2
    - Attack = 1d20 + Character Proficiency Bonus + Ability Modifier
    - Damage = Weapon Dice + Ability Modifier
    - Critical hit damage = 2 Weapon Dice + Ability Modifier

    DnD Combat reference: https://www.dndbeyond.com/sources/basic-rules/combat#ActionsinCombat

#### Files contained:

- project.py
  - Main function imports menu classes.
  - User input is passed into roll_attack() and roll_damage() functions
  - weapon_data() for pytest to verify weapon data is returned correctly for each weapon
- menus.py
  - Class that contains methods for weapon selection and attack selection
  - Weapon menu will automatically update to reflect each weapon in user's character_stats.json file
- character.py
  - Class that contains methods for character import, and calculations for abilities and weapons
  - import_stats() imports and stores character_stats.json file
  - ability_mod_calc() converts character ability scores into ability modifiers
    - Ability score is the total score of an ability (ex: Strength = 14)
    - Ability modifier is the score of an ability that is added to rolls (ex: Strength = + 2)
  - weapon_info() takes user's weapon stats and returns a dict with the weapon's combat data (i.e. type of dice, hit modifier, ability modifier)
- dice.py
  - Class that contains a method for rolling dice
  - roll() will take the number of dice and type of dice user wants to roll as inputs
  - Returns the sum of the rolls, highest roll, and lowest rolls
- test_project.py
  - Unit tests for project.py functions
- character_stats.json
  - Sample file containing character information to import
