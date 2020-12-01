class Lineup:
    def__init__(self, players):
        self.players = players
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < (len(self.players)) -1):
            player = self.players[self.n]
            self.n += 1
            return player
        elif self.n == (len(self.players) -1)
        player = self.players[self.n]
            self.n = 0
            return player


astros = [
    'springer',
    'tucker', 
    'bregman',
    'correa',
    'gonzalez',
]

astos_lineup = Lineup(astros)
#line 16 is istantiating it 
process = iter(astros_lineup)

print(next(process)
print(next(process))