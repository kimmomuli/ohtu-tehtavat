import unittest
from statistics import Statistics
from player import Player

#Stub
class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_correct_player(self):
        kurri = self.statistics.search('Kurri')
        self.assertEqual(kurri.team, 'EDM')
        self.assertEqual(kurri.goals, 37)
        self.assertEqual(kurri.assists, 53)


    def test_search_kissa(self):
        self.assertEqual(self.statistics.search('Kissa'), None)

    def test_team_with_correct_name(self):
        EDM_team = self.statistics.team('EDM')
        self.assertEqual(len(EDM_team), 3)
        self.assertEqual(EDM_team[0].name, 'Semenko')

    def test_team_with_kissa_name(self):
        EDM_team = self.statistics.team('kissa')
        self.assertEqual(len(EDM_team), 0)

    def test_top_scores_empty(self):
        empty_scorers = self.statistics.top_scorers(-1)
        self.assertEqual(len(empty_scorers), 0)
        
    def test_two_top_scorers(self):
        scorers = self.statistics.top_scorers(1)
        self.assertEqual(len(scorers), 2)
        self.assertEqual(scorers[0].name, 'Gretzky')
        self.assertEqual(scorers[1].name, 'Lemieux')
