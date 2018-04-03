from math import *
import random

class GameState:

    def __init__(self):
        self.playerJustMoved = 2

    def Clone(self):
        st = GameState()
        st.playerJustMoved = self.playerJustMoved
        return st

    def DoMove(self, move):
        self.playerJustMoved = 3 - self.playerJustMoved

    def GetMoves(self):
        # Get all possible moves from this state.
        pass

    def GetResult(self, playerjm):
        # Get the game result from the viewpoint of playerjm
        pass

    def __repr__(self):
        pass

class NimState:
    """ A state of the game Nim. In Nim, players alternately take 1,2 or 3 chips with the 
        winner being the player to take the last chip. 
        In Nim any initial state of the form 4n+k for k = 1,2,3 is a win for player 1
        (by choosing k) chips.
        Any initial state of the form 4n is a win for player 2.
    """
    def __init__(self, ch):
        self.playerJustMoved = 2 # At the root pretend the player just moved is p2 - p1 has the first move
        self.chips = ch
        
    def Clone(self):
        """ Create a deep clone of this game state.
        """
        st = NimState(self.chips)
        st.playerJustMoved = self.playerJustMoved
        return st

    def DoMove(self, move):
        """ Update a state by carrying out the given move.
            Must update playerJustMoved.
        """
        assert move >= 1 and move <= 3 and move == int(move)
        self.chips -= move
        self.playerJustMoved = 3 - self.playerJustMoved
        
    def GetMoves(self):
        """ Get all possible moves from this state.
        """
        return range(1,min([4, self.chips + 1]))
    
    def GetResult(self, playerjm):
        """ Get the game result from the viewpoint of playerjm. 
        """
        assert self.chips == 0
        if self.playerJustMoved == playerjm:
            return 1.0 # playerjm took the last chip and has won
        else:
            return 0.0 # playerjm's opponent took the last chip and has won

    def __repr__(self):
        s = "Chips:" + str(self.chips) + " JustPlayed:" + str(self.playerJustMoved)
        return s

class Node:
    '''
    a node in the game tree. node wins is always from the viewpoint of playerJustMoved.
    crashes if state not specified
    '''

    def __init__(self, move = None, parent = None, state = None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = list(state.GetMoves())
        self.playerJustMoved = state.playerJustMoved


    def UCTSelectChild(self):
        '''
        use the UCB1 formula to select a child node.
        '''
        s = sorted(self.childNodes, key = lambda c: c.wins/c.visits + sqrt(2 * log(self.visits)/c.visits))[-1]
        return s
    
    def AddChild(self, m, s):
        n = Node(move = m, parent = self, state = s)
        self.untriedMoves.remove(m)
        self.childNodes.append(n)
        return n

    def Update(self, result):
        self.visits += 1
        self.wins += result

    def __repr__(self):
        return '[M: ' + str(self.move) + ' W/V: ' + str(self.wins) + '/' + str(self.visits) + '=' + str(self.wins/self.visits) + ']'

    def TreeToString(self, indent):
        s = self.IndentString(indent) + str(self)
        for c in self.childNodes:
            s += c.TreeToString(indent + 1)
        return s

    def IndentString(self, indent):
        s = '\n'
        for i in range(1, indent + 1):
            s += '| '
        return s

    def ChildrenToString(self):
        s = ''
        for c in self.childNodes:
            s += str(c) + '\n'
        return s


def UCT(rootstate, itermax, verbose = False):

    rootnode = Node(state=rootstate)

    for i in range(itermax):
        node = rootnode
        state = rootstate.Clone()

        # Select
        while node.untriedMoves == [] and node.childNodes != []:
            node = node.UCTSelectChild()
            state.DoMove(node.move)

        # Expand
        if node.untriedMoves != []:
            m = random.choice(node.untriedMoves)
            state.DoMove(m)
            node = node.AddChild(m, state)

        # Rollout - this can often be made orders of magnitude quicker using
        # a state.GetRandomMove() function
        temp = state.GetMoves()
        while state.GetMoves() != []:
            temp = state.GetMoves()
            if len(temp) == 0:
                break
            state.DoMove(random.choice(temp))

        # Backpropagate
        while node != None:
            result = state.GetResult(node.playerJustMoved)
            node.Update(result)
            node = node.parentNode

    if(verbose):
        print(rootnode.TreeToString(0))
    else:
        print(rootnode.ChildrenToString())

    return sorted(rootnode.childNodes, key=lambda c: c.visits)[-1].move


def UCTPlayGame():
    state = NimState(15)

    while (state.GetMoves() != []):
        temp = state.GetMoves()
        if len(temp) == 0:
            break
        print(str(state))
        if state.playerJustMoved == 1:
            m = UCT(rootstate = state, itermax = 1000, verbose=False)
        else:
            m = UCT(rootstate= state, itermax = 100, verbose=False)
        state.DoMove(m)

    result = state.GetResult(state.playerJustMoved)
    if result == 1.0 or result == 0.0:
        print('Player ' + str(state.playerJustMoved) + ' : result ' + str(result))
    else:
        print('Nobody wins')

if __name__ == '__main__':
    UCTPlayGame()