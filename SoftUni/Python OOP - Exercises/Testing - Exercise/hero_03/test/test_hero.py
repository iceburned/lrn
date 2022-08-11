from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    HERO_USERNAME = "ATTACKER"
    HERO_LEVEL = 10
    HERO_HEALTH = 100
    HERO_DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self):
        self.attacker = Hero(self.HERO_USERNAME, self.HERO_LEVEL, self.HERO_HEALTH, self.HERO_DAMAGE)

    def test_init(self):
        self.assertEqual(self.HERO_USERNAME, self.attacker.username)
        self.assertEqual(self.HERO_LEVEL, self.attacker.level)
        self.assertEqual(self.HERO_HEALTH, self.attacker.health)
        self.assertEqual(self.HERO_DAMAGE, self.attacker.damage)

    def test_battle_raises_when_attackers_with_same_name(self):
        enemy = Hero(self.HERO_USERNAME, 5, 25, 30)
        with self.assertRaises(Exception) as error:
            self.attacker.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle_raises_when_attackers_is_dead(self):
        self.attacker.health = 0
        enemy = Hero("Pesho", 5, 25, 30)
        with self.assertRaises(ValueError) as error:
            self.attacker.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle_raises_when_enemy_is_dead(self):
        enemy = Hero("Pesho", 5, 0, 30)
        with self.assertRaises(ValueError) as error:
            self.attacker.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(error.exception))

    def test_when_both_heroes_died(self):
        enemy = Hero("Pesho", self.HERO_LEVEL, self.HERO_HEALTH, self.HERO_DAMAGE)
        result = self.attacker.battle(enemy)
        expected_health = self.HERO_HEALTH - self.HERO_LEVEL * self.HERO_DAMAGE
        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, self.attacker.health)
        self.assertEqual(expected_health, enemy.health)

    def test_battle_return_win_when_enemy_dies(self):
        enemy_level, enemy_health, enemy_damage = 5, 100, 10
        enemy = Hero("Pesho", 5, 100, 10)
        result = self.attacker.battle(enemy)
        enemy_expected_health = enemy_health - (self.HERO_LEVEL * self.HERO_DAMAGE)
        enemy_expected_level = self.HERO_LEVEL + self.BATTLE_LEVEL_INCREMENT
        enemy_expected_damage = self.HERO_DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        attacked_expected_health = self.HERO_HEALTH - (enemy_level * enemy_damage) + self.BATTLE_DAMAGE_INCREMENT

        self.assertEqual("You win", result)
        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(enemy_expected_level, self.attacker.level)
        self.assertEqual(enemy_expected_damage, self.attacker.damage)
        self.assertEqual(attacked_expected_health, self.attacker.health)

    def test_battle_return_defeat_when_attacker_dies(self):
        attacker_level, attacker_health, attacker_damage = 5, 100, 10
        attacker = Hero(" attacker", attacker_level, attacker_health, attacker_damage)
        enemy = Hero("Enemy", self.HERO_LEVEL, self.HERO_HEALTH, self.HERO_DAMAGE)
        result = attacker.battle(enemy)
        attacker_expected_health = attacker_health - (self.HERO_LEVEL * self.HERO_DAMAGE)
        enemy_expected_level = self.HERO_LEVEL + self.BATTLE_LEVEL_INCREMENT
        enemy_expected_damage = self.HERO_DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        enemy_expected_health = self.HERO_HEALTH - (attacker_level * attacker_damage) + self.BATTLE_DAMAGE_INCREMENT

        self.assertEqual("You lose", result)
        self.assertEqual(attacker_expected_health, attacker.health)
        self.assertEqual(enemy_expected_level, enemy.level)
        self.assertEqual(enemy_expected_damage, enemy.damage)
        self.assertEqual(enemy_expected_health, enemy.health)

    def test_hero_str_return_proper_message(self):
        actual_result = str(self.attacker)
        expected_result = f"Hero {self.HERO_USERNAME}: {self.HERO_LEVEL} lvl\n" \
                          f"Health: {self.HERO_HEALTH}\n" \
                          f"Damage: {self.HERO_DAMAGE}\n"
        self.assertEqual(expected_result, actual_result)


if __name__ == "name":
    main()
