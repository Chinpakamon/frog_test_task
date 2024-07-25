import unittest
from unittest.mock import patch
from main import Frog, Assassin, Adventurer, Craftsman, battle


class TestFrog(unittest.TestCase):
    @patch.multiple(Frog, __abstractmethods__=set())
    def test_init(self):
        frog = Frog()
        self.assertEquals(frog.attack, 15)
        self.assertEquals(frog.health, 150)
        self.assertEquals(frog.armor, 5)

    @patch.multiple(Frog, __abstractmethods__=set())
    def test_calculate_damage(self):
        frog = Frog()
        damage = frog.calculate_damage()
        self.assertGreaterEqual(damage, 7)
        self.assertLessEqual(damage, 15)

    @patch.multiple(Frog, __abstractmethods__=set())
    def test_calculate_armor(self):
        frog = Frog()
        armor = frog.calculate_armor()
        self.assertGreaterEqual(armor, 0)
        self.assertLessEqual(armor, 5)


class TestAssassin(unittest.TestCase):
    def test_modify_params(self):
        frog = Assassin()
        frog.modify_params()
        self.assertEquals(frog.health, 187)


class TestAdventurer(unittest.TestCase):
    def test_modify_params(self):
        frog = Adventurer()
        frog.modify_params()
        self.assertEquals(frog.attack, 22)


class TestCraftsman(unittest.TestCase):
    def test_modify_params(self):
        frog = Craftsman()
        frog.modify_params()
        self.assertEquals(frog.armor, 10)


class TestBattle(unittest.TestCase):
    @patch('random.choice')
    @patch('asyncio.gather')
    async def test_battle(self, mock_choice, mock_gather):
        mock_choice.side_effect = [Assassin, Adventurer]
        mock_gather.return_value = [(50, 50), (50, 50)]
        results = battle()
        self.assertEqual(results, (50, 50))


if __name__ == "__main__":
    unittest.main()
