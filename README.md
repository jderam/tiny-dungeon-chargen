# tiny-dungeon-chargen
Python package to generate player characters for the
[Tiny Dungeon](https://www.drivethrurpg.com/product/144545/Tiny-Dungeon-Print-and-Play-Bundle)
tabletop roleplaying game (1st edition) by Brandon McFaddon.

## Installation
This package may be installed from pypi via pip:
```
python -m pip install tiny-dungeon
```

## Usage
Instantiate a character
```python
>>> from tiny_dungeon.char import TinyDungeonPC
>>>
>>> pc = TinyDungeonPC()
>>>
>>> # view as dictionary
>>> pc.as_dict()
{'race': 'Fey', 'hp': 6, 'race_trait': 'Bow Mastery', 'race_trait_desc': 'You have Mastered bows and have Advantage when using them. This is in addition to the Mastered weapon chosen at Adventurer Creation.', 'trait1': 'Acrobat', 'trait1_desc': 'You gain Advantage when Testing to do acrobatic tricks such as tumbling, long-distance jumps, climbing, and maintaining balance.', 'trait2': 'Marksman', 'trait2_desc': 'When you Focus, your next attack with a ranged weapon is successful on a Test of 3, 4, 5, or 6.', 'trait3': 'Nimble Fingers', 'trait3_desc': 'You gain Advantage when Testing to pick locks, pick pockets, or steal.', 'weapon_proficiency': 'Ranged', 'weapon': 'Throwing Knives', 'gold_pieces': 10, 'equipment': ['bedroll', 'flint and steel', 'belt pouch', 'rucksack', 'lantern', 'empty waterskin', 'oil (3 pints)', "50' rope", 'rations (7 days)', 'torch', 'cloak'], 'family_trade': ''}
>>>
>>> # print character to STDOUT
>>> pc.print_char()


NAME: _________________________________

RACE: Fey

HIT POINTS: 6

WEAPON PROFICIENCY: Ranged

WEAPON: Throwing Knives

MASTERED WEAPON: ______________________

TRAITS
------------
Bow Mastery: You have Mastered bows and have Advantage when using them. This is in addition to the Mastered weapon chosen at Adventurer Creation.
Acrobat: You gain Advantage when Testing to do acrobatic tricks such as tumbling, long-distance jumps, climbing, and maintaining balance.
Marksman: When you Focus, your next attack with a ranged weapon is successful on a Test of 3, 4, 5, or 6.
Nimble Fingers: You gain Advantage when Testing to pick locks, pick pockets, or steal.

EQUIPMENT
------------
bedroll
flint and steel
belt pouch
rucksack
lantern
empty waterskin
oil (3 pints)
50' rope
rations (7 days)
torch
cloak

GOLD PIECES: 10

```
