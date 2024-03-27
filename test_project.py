import pytest
from character import Character
from project import roll_damage
from project import weapon_selection
from project import attack_selection
from project import weapon_data


def test_weapon_selection():
    with pytest.raises(ValueError):
        weapon_selection(3)

    with pytest.raises(ValueError):
        weapon_selection("cat")


def test_attack_selection():
    with pytest.raises(ValueError):
        attack_selection(4)

    with pytest.raises(ValueError):
        attack_selection("cat")

    assert attack_selection(1) == "Attack"
    assert attack_selection(2) == "Advantage Attack"
    assert attack_selection(3) == "Disadvantage Attack"


def test_weapon_data():
    char = Character("character_stats.json")
    assert weapon_data(char, "short_sword") == {'name': 'Short Sword', 'hit': 7, 'dice': 6, 'ability_mod': 3, 'calc_text': 'Prof bonus (4) + Ability mod (3)'}
    assert weapon_data(char, "bow") == {'name': 'Bow', 'hit': 9, 'dice': 8, 'ability_mod': 3, 'calc_text': 'Prof bonus (4) + Ability mod (3)'}


def test_roll_damage():
    weapon_choice = {'name': 'Short Sword', 'hit': 7, 'dice': 6, 'ability_mod': 3, 'calc_text': 'Prof bonus (4) + Ability mod (3)'}
    assert roll_damage(weapon_choice, "crit fail") == "\nCritical miss!"
    assert roll_damage(weapon_choice, "super fail") == "\nCritical miss!"
