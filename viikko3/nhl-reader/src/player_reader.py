import requests
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        self.url = url


    def get_players(self):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            players.append(player)
        players.sort(key = lambda x : (x.goals + x.assists), reverse=True)
        return players
