class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        won_points = 1
        if player_name == "player1":
            self.player1_score += won_points
        else:
            self.player2_score += won_points

    def points_equals(self):
        return self.player1_score == self.player2_score

    def game_can_end(self):
        return self.player1_score >= 4 or self.player2_score >= 4

    def game_is_on(self):
        return self.player1_score < 4 or self.player2_score < 4

    def score_when_points_equals(self):
        scores = self.player1_score
        if scores == 0:
            return "Love-All"
        elif scores == 1:
            return "Fifteen-All"
        elif scores == 2:
            return "Thirty-All"
        elif scores == 3:
            return "Forty-All"
        return "Deuce"

    def result_by_score(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        return "Forty"

    def result_by_player(self, player):
        if player == 'player1':
            return self.result_by_score(self.player1_score)
        return self.result_by_score(self.player2_score)

    def score_when_game_is_on(self):
        player1_result = self.result_by_player('player1')
        player2_result = self.result_by_player('player2')
        return f"{player1_result}-{player2_result}"

    def game_is_end(self):
        return abs(self.player1_score - self.player2_score) >= 2

    def who_is_winner(self):
        if self.player1_score > self.player2_score:
            return "Win for player1"
        return "Win for player2"

    def who_is_lead(self):
        if self.player1_score > self.player2_score:
            return "Advantage player1"
        return "Advantage player2"

    def check_end_game(self):
        if self.game_is_end():
            return self.who_is_winner()
        return self.who_is_lead()

    def get_score(self):
        if self.points_equals():
            return self.score_when_points_equals()

        if self.game_can_end():
            return self.check_end_game()

        if self.game_is_on():
            return self.score_when_game_is_on()
