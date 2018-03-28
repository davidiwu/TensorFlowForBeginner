import datetime
from math import log, sqrt

'''
The pass statement is a null operation; nothing happens when it executes. 
The pass is also useful in places where your code will eventually go, but has not been written yet 
(e.g., in stubs for example) 
'''

class Board(object):
    
    def start(self):
        # returns a representation of the starting state of the game
        pass

    
    def current_player(self, state):
        # takes the game state and returns the current player's number
        pass

    def next_state(self, state, play):
        # takes the game state, and the move to be applied
        # returns the new game state
        pass

    def legal_plays(self, state_history):
        # takes a sequence of game states representing the full 
        # game history, and returns the full list of moves that
        # are legal plays for the current player
        pass

    def winner(self, state_history)
        # takes a sequence of game states representing the full
        # game history. if the game is now won, return the player
        # number. if the game is still ongoing, return zero. if
        # the game is tied, return a different distinct value, e.g. -1
        pass
    

class MonteCarlo(object)

    def __init__(self, board, **kwargs):
        self.board = board
        self.states = []

        seconds = kwargs.get('time', 30)
        self.calculation_time = datetime.timedelta(seconds=seconds)

        self.max_moves = kwargs.get('max_moves', 100)

        # keep statistics of the game states that the AI hits during each run of run_simulation
        self.wins = {}
        self.plays = {}

        # C for UCB1 constant: upper confidence bound
        self.C = kwargs.get('C', 1.4)

    
    def update(self, state):
        self.states.append(state)

    
    def get_play(self):
        self.max_depth = 0
        state = self.states[-1]
        
        player = self.board.current_player(state)
        legal = self.board.legal_plays(self.states[:])

        if not legal:
            return
        if len(legal) == 1:
            return legal[0]

        games = 0
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow - begin < self.calculation_time:
            self.run_simulation()
            games += 1

        moves_states = [(p, self.board.next_state(state, p)) for p in legal]

        print games, datetime.datetime.utcnow() - begin

        # pick the move with the highest percentage of wins
        percent_wins, move = max(
            (
                self.wins.get((player, S), 0) /
                self.plays.get((player, S), 1), 
                p
            )
            for p, S in moves_states
        )

        # display the stats for each possible play
        for x in sorted (
            ((100 * self.wins.get((player, S), 0) /
                self.plays.get((player, S), 1),
                self.wins.get((player, S), 0),
                self.plays.get((player, S), 0), p)
                for p, S in moves_states),
                reverse=True
            ):
            print "{3}: {0:.2f}% ({1} / {2})".format(*x)

        print "Maximum depth searched:", self.max_depth

        return move

    def run_simulation(self):

        plays, wins = self.plays, self.wins

        visited_states = set()

        states_copy = self.states[:]
        state = states_copy[-1]

        player = self.board.current_player(state)

        expand = True

        for t in xrange(1, self.max_moves + 1):
            legal = self.board.legal_plays(states_copy)
            
            # play = choice(legal) -- choice a play based on UCB1: Upper confidence bound 1

            moves_states = [(p, self.board.next_state(state, p)) for p in legal]
            if all(plays.get((player, S)) for p, S in moves_states):
                # if we have stats on all of the legal moves here, use them.
                log_total = log(
                    sum(plays[(player, S)] for p, S in moves_states)
                )
                value, move, state = max(
                    (
                        (wins[(player, S)] / plays[(player, S)]) +
                        self.C * sqrt(log_total / plays[(player, S)]), p, S
                    )
                    for p, S in moves_states
                )
            else:
                move, state = choice(moves_states)

            #state = self.board.next_state(state, play)
            states_copy.append(state)

            # player here and below refers to the player
            # who moved into that particular state.
            if expand and (player, state) not in self.plays:
                expand = False
                self.plays[(player, state)] = 0
                self.wins[(player, state)] = 0

            visited_states.add((player, state))

            player = self.board.current_player(state)
            winner = self.board.winner(states_copy)
            if winner:
                break

        for player, state in visited_states:
            if(player, state) not in self.plays:
                continue
            self.plays[(player, state)] += 1
            if player == winner:
                self.wins[(player, state)] += 1
            

