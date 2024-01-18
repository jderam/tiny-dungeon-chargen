ADVENTURERS_KIT = [
    "bedroll",
    "flint and steel",
    "belt pouch",
    "rucksack",
    "lantern",
    "empty waterskin",
    "oil (3 pints)",
    "50' rope",
    "rations (7 days)",
    "torch",
    "cloak",
]

RACES = {
    "Human": {
        "hp": 6,
        # Humans get a random trait from the standard trait list
        "trait": None,
        "trait_desc": None,
    },
    "Fey": {
        "hp": 6,
        "trait": "Bow Mastery",
        "trait_desc": "You have Mastered bows and have Advantage when using them. This is in addition to the Mastered weapon chosen at Adventurer Creation.",
    },
    "Dwarf": {
        "hp": 8,
        "trait": "Dark Vision",
        "trait_desc": "You are able to see 30 feet around you in total darkness.",
    },
    "Goblin": {
        "hp": 4,
        "trait": "Goblin Agility",
        "trait_desc": "You can Test 1d6 whenever you are successfully hit by an enemy. If your Test is successful, you evade the attack and do not take damage. Declaring Evade as an Action has no additional benefit.",
    },
    "Salimar": {
        "hp": 5,
        "trait": "Pyrothermic Healing",
        "trait_desc": "Any amount damage that would be dealt to you by a source of fire instead heals you for that amount.",
    },
}

# This item is not included in the rules, but I added it for convenience
SAMPLE_WEAPONS = {
    "Light Melee": [
        "Club",
        "Dagger",
        "Mace",
        "Sword",
    ],
    "Heavy Melee": [
        "Battle Axe",
        "Glaive",
        "Two-handed Sword",
        "War Hammer",
    ],
    "Ranged": [
        "Bow",
        "Crossbow",
        "Sling",
        "Throwing Knives",
    ],
}

TRAITS = {
    "Acrobat": "You gain Advantage when Testing to do acrobatic tricks such as tumbling, long-distance jumps, climbing, and maintaining balance.",
    "Alchemist": "Provided the right reagents and recipes, you can mix potions, elixirs, and poisons. You also gain Advantage when identifying unknown liquids.",
    "Beastspeaker": "You are able to communicate with animals. This form of communication is primitive and very simplistic",
    "Berserker": "When making a melee attack, you can choose to attack at a Disadvantage. If the attack is successful, it deals 2 points of damage.",
    "Brawler": "You gain Advantage when making unarmed attacks.",
    "Diehard": "When an attack would reduce you to 0 Hit Points, it instead reduces you to 1 Hit Point. You can do this once per day.",
    "Charismatic": "You gain Advantage when attempting to convince someone of something or otherwise influence them.",
    "Dungeoneer": "You gain Advantage when attempting to find your way through a dungeon or cave system, and when attempting to identify creatures native to dungeons or caves.",
    "Educated": "You gain Advantage when checking to see if you know specific information.",
    "Eidetic Memory": "When Testing to recall information you have seen or heard previously - even in passing - you succeed on a roll of 4, 5, or 6.",
    "Familiar": "For as long as you can remember, you have never truly been alone. Another spirit has linked itself to yours, accepting you as its friend and master.",
    "Fleet of Foot": "Your speed increases from 25 feet to 30 feet",
    "Healer": "As an Action, you can Test 2d6 to heal a creature other than yourself. If the Test is successful, the target creature is healed for 2 Hit Points. This Trait can also be used to cure poison, disease, and other physical ailments that are non-magical. You must be next to the creature to heal it.",
    "Insightful": "You gain Advantage when Testing to discern whether or not someone is telling the truth or lying.",
    "Marksman": "When you Focus, your next attack with a ranged weapon is successful on a Test of 3, 4, 5, or 6.",
    "Nimble Fingers": "You gain Advantage when Testing to pick locks, pick pockets, or steal.",
    "Opportunist": "If an enemy within range fails to hit with an attack against you, you may immediately make an attack with Disadvantage against that enemy.",
    "Perceptive": "You gain Advantage when Testing to gain information about your surroundings or find things which may be hidden. You gain this even while asleep.",
    "Quick Shot": "You are able to reload a Ranged Weapon and fire it in one Action.",
    "Resolute": "You gain Advantage on all Save Tests.",
    "Shield Bearer": "While wielding a shield, Test with 2d6 on Evade or Goblin Agility Actions instead of 1d6. If you choose this Trait, your Adventurer gains a shield at Adventurer creation.",
    "Sneaky": "You gain Advantage when Testing to hide or sneak around without others noticing you.",
    "Spell Reader": "You have spent years learning the sacred language of the arcane, allowing you to read power-laced words from magic scrolls.",
    "Spell-Touched": "You were born with an arcane heritage, and while the centuries have diluted the power, you are still able to subtly influence the world around you by merely willing it to happen.",
    "Strong": "You gain Advantage when Testing to do something with brute force.",
    "Survivalist": "You gain Advantage when Testing to forage for food, find water, seek shelter, or create shelter in the wild.",
    "Tough": "You gain 1 additional Hit Point.",
    "Tracker": "You gain Advantage when Testing to track someone or an animal in the wilderness. While outside, you can also locate true north without Testing.",
    "Trapmaster": "You gain Advantage when Testing to create, locate, and disarm traps.",
    "Vigilant": "You gain Advantage on Initiative Tests.",
}

WEAPON_GROUPS = [
    "Light Melee",
    "Heavy Melee",
    "Ranged",
]
