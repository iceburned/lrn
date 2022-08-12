from unittest import TestCase

from project.team import Team


class TestTeam(TestCase):
    TEAM_NAME = "WinWin"
    TEAM_MEMBERS = {}
    NAME_AGE = {"Teo": 22, "Zoq": 18, "Ana": 27}

    def setUp(self) -> None:
        self.team = Team(self.TEAM_NAME)

    def test_init(self):
        self.assertEqual(self.TEAM_NAME, self.team.name)
        self.assertEqual(self.TEAM_MEMBERS, self.team.members)

    def test_name_for_only_alphas(self):
        name = "99"
        with self.assertRaises(ValueError) as error:
            self.team.name = name
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_add_member_to_members_dict(self):
        self.team.members = {"Zoq": 16}
        actual = self.team.add_member(**self.NAME_AGE)
        self.assertEqual({"Teo": 22, "Zoq": 16, "Ana": 27}, self.team.members)
        expected = "Successfully added: Teo, Ana"
        self.assertEqual(expected, actual)

    def test_remove_member_if_present(self):
        self.team.members = {"Zoq": 16}
        name = "Zoq"
        member = self.team.remove_member(name)
        self.assertEqual(f"Member {name} removed", member)
        self.assertEqual({}, self.team.members)

    def test_gt_(self):
        other = Team("GOGO")
        self.team.members = self.NAME_AGE
        other.members = {"Zoq": 18, "Ana": 27}
        self.assertTrue(self.team.__gt__(other))

    def test_gt_false(self):
        other = Team("GOGO")
        self.team.members = self.NAME_AGE
        other.members = {"Zoq": 18, "Ana": 27, "a": 44, "v": 34}
        self.assertFalse(self.team.__gt__(other))

    def test_len_(self):
        self.team.members = self.NAME_AGE
        self.assertEqual(len(self.NAME_AGE), self.team.__len__())

    def test_add(self):
        other = Team("GOGO")
        other.members = {"Z": 18, "A": 27}
        new_team = self.team.__add__(other)
        self.assertEqual(f"{self.team.name}{other.name}", new_team.name)
        new_team.members.update(self.NAME_AGE)
        new_team.members.update(other.members)
        self.assertEqual({"Teo": 22, "Zoq": 18, "Ana": 27, "Z": 18, "A": 27}, new_team.members)

    def test_str__(self):
        members = {'lili': 20, "Maria": 21}
        self.team.members = members

        result = Team.__str__(self.team)
        exe = f"Team name: WinWin\nMember: Maria - 21-years old\nMember: lili - 20-years old"

        self.assertEqual(exe, result)
