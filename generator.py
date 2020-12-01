class InfiniteLineup:
    def self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        idx = 0

        while True: 
            if idx < lineup_max: 
                yield self.players[idx]
            else: 
                idx = 0 
                yield self.players[idx]
            idx += 1
     def __str__(self):
        returns f'InfiniteLineup with the players: {self.players}'

    def __repr__(self):
        return f'<InfiniteLineup ({self.players})'

#new change


astros = [
    'Springer',
    'Bregman',
    'Alturve'
]

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()

print(repr(astros_lineup))
print(repr(astros_lineup))
print(repr(astros_lineup))
print(repr(astros_lineup))
print(repr(astros_lineup))
print(repr(astros_lineup))
print(repr(astros_lineup))
