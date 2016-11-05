from unittest import TestCase

from player import Player


class TestPlayer(TestCase):

    def test_name(self):
        player = Player(name="Doris", sign='O')
        self.assertEqual(player.name,"Doris")
