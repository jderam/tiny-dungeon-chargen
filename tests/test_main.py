import pytest
from tiny_dungeon.char import TinyDungeonPC

n = 10000


@pytest.mark.repeat(n)
def test_character_generation():
    """To get us started, this is just a dumb test that generates a
    character n times and makes sure there are no exceptions thrown.
    """
    pc = TinyDungeonPC()
    assert pc is not None
