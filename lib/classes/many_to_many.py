class Game:

    all = []

    def __init__(self, title):
        
        self.title = title
        Game.add_game_to_all(self)

    def __repr__(self):
        return f'Game: {self.title}'

    @classmethod
    def add_game_to_all(cls, game):
        cls.all.append(game)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, 'title') :
            self._title = value


    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        res = []
        for result in self.results():
            if result.player not in res:
                res.append(result.player)
        return res

    def average_score(self, player):
        scores = []

        for result in player.results():
            if result.game == self:
                scores.append(result.score)
        return sum(scores) / len(scores)

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.add_player_to_all(self)

    def __repr__(self):
        return f'Player {self.username}'

    @classmethod
    def add_player_to_all(cls, player):
        cls.all.append(player)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        res = []
        for result in self.results():
            if result.game not in res:
                res.append(result.game)
        return res

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        acc = 0
        for result in self.results():
            if result.game == game:
                acc += 1
        return acc

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.add_result_to_all(self)

    def __repr__(self):
        return f'{self.player} did {self.game} and scored {self.score}'
    
    @classmethod
    def add_result_to_all(cls, result):
        cls.all.append(result)
        

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not hasattr(self, 'score') and isinstance(value, int) and 1 <= value <= 5000:
            self._score = value

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        if not hasattr(self, 'player'):
            self._player = None
        if isinstance(value, Player):
            self._player = value

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, value):
        if not hasattr(self, 'game'):
            self._game = None
        if isinstance(value, Game):
            self._game = value
    
