from project.hero import Hero

from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Player1', 2, 100.0, 20.0)
        self.enemy_hero = Hero('Player2', 3, 90.0, 25.0)

    def test_hero_init(self):
        self.assertEqual('Player1', self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(20.0, self.hero.damage)

    def test_hero_instance_attributes_type(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)
        self.assertIsInstance(self.hero.level, int)

    def test_hero_battle_if_enemy_hero_equals_username_raises(self):
        self.enemy_hero.username = 'Player1'

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_battle_if_health_less_or_equal_zero_raises(self):
        # Less than zero
        self.hero.health = -1

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        # Equal to zero
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero_battle_if_enemy_hero_health_less_or_equal_to_zero_raises(self):
        self.enemy_hero.health = -1

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight Player2. He needs to rest", str(ex.exception))

        self.enemy_hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight Player2. He needs to rest", str(ex.exception))

    def test_hero_battle_if_health_of_self_and_enemy_less_than_or_equal_to_zero(self):
        # Both hero and enemy hero health are below 0
        self.hero.health = 20
        self.enemy_hero.health = 30

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(-55, self.hero.health)
        self.assertEqual(-10, self.enemy_hero.health)
        self.assertEqual('Draw', result)

        # Both hero and enemy hero health are equal to zero
        self.hero.health = 75
        self.enemy_hero.health = 40

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual('Draw', result)

    def test_hero_battle_if_only_enemy_health_below_zero(self):
        # Enemy health after battle is below zero
        self.hero.health = 100
        self.enemy_hero.health = 30

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(3, self.hero.level)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual(-10, self.enemy_hero.health)
        self.assertEqual('You win', result)

    def test_hero_battle_if_only_enemy_health_is_equal_to_zero(self):
        # Enemy health after battle is equal to zero
        self.hero.health = 100
        self.enemy_hero.health = 40

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(3, self.hero.level)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual(0, self.enemy_hero.health)
        self.assertEqual('You win', result)

    def test_hero_battle_if_only_self_health_less_than_zero(self):
        self.hero.health = 60
        self.enemy_hero.health = 50

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(4, self.enemy_hero.level)
        self.assertEqual(15, self.enemy_hero.health)
        self.assertEqual(30, self.enemy_hero.damage)
        self.assertEqual(-15, self.hero.health)
        self.assertEqual('You lose', result)

    def test_hero_battle_if_only_self_health_equals_zero(self):
        self.hero.health = 75
        self.enemy_hero.health = 50

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(4, self.enemy_hero.level)
        self.assertEqual(15, self.enemy_hero.health)
        self.assertEqual(30, self.enemy_hero.damage)
        self.assertEqual(0, self.hero.health)
        self.assertEqual('You lose', result)

    def test_hero_str_method(self):
        expected = f"Hero Player1: 2 lvl\n" \
               f"Health: 100.0\n" \
               f"Damage: 20.0\n"

        result = self.hero.__str__()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
