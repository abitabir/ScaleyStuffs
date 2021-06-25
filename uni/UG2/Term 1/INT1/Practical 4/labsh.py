# Code adapted from Daniel Hernandez and Peter York's MCTS code

import numpy as np
import random

import colorama
from colorama import Fore, Back


class GameState:
    """
        A GameState represents a valid configuration of the 'state' of a game.
        For instance:
            - the position of all the active pieces on a chess board.
            - The position and velocities of all the entities in a 3D world.
        This interface presents the minimal functionality required to implement
        an MCTS-UCT algorithm for a 2 player game.
    """

    def __init__(self):
        self.playerJustMoved = 2  # Game starts with Player 1.

    def Clone(self):
        """
        :returns: deep copy of this GameState
        """
        st = GameState()
        st.playerJustMoved = self.playerJustMoved
        return st

    def DoMove(self, move):
        """
        !! This is the environment's model !!
        Changes the GameState by carrying out the param move.
        :param move: (int) action taken by an agent.
        """
        self.playerJustMoved = 3 - self.playerJustMoved

    def GetMoves(self):
        """ :returns: int array with all available moves at this state
        """
        pass

    def IsGameOver(self):
        """ :returns: whether this GameState is a terminal state
        """
        return self.GetMoves() == []

    def GetResult(self, player):
        """
        :param player: (int) player which we want to see if he / she is a winner
        :returns: winner from the perspective of the param player
        """
        pass


class Connect4State(GameState):
    """
        GameState for the Connect 4 game.
        The board is represented as a 2D array (rows and columns).
        Each entry on the array can be:
            - 0 = empty    (.)
            - 1 = player 1 (X)
            - 2 = player 2 (O)
    """

    def __init__(self, width=7, height=6, connect=4):
        self.playerJustMoved = 2
        self.winner = 0  # 0 = no winner, 1 = Player 1 wins, 2 = Player 2 wins.

        self.width = width
        self.height = height
        self.connect = connect
        self.InitializeBoard()

    def InitializeBoard(self):
        """
        Initialises the Connect 4 gameboard.
        """
        self.board = []
        for y in range(self.width):
            self.board.append([0] * self.height)

    def Clone(self):
        """
        Creates a deep copy of the game state.
        NOTE: it is _really_ important that a copy is used during simulations
              Because otherwise MCTS would be operating on the real game board.
        :returns: deep copy of this GameState
        """
        st = Connect4State(width=self.width, height=self.height)
        st.playerJustMoved = self.playerJustMoved
        st.winner = self.winner
        st.board = [self.board[col][:] for col in range(self.width)]
        return st

    def DoMove(self, movecol):
        """
        Changes this GameState by "dropping" a chip in the column
        specified by param movecol.
        :param movecol: column over which a chip will be dropped
        """  # remember, we don't specify the row like we would for noughts and crosses (Abir keeps getting game confusions)
        try:
            assert movecol >= 0 and movecol <= self.width and self.board[movecol][self.height - 1] == 0
            row = self.height - 1
            while row >= 0 and self.board[movecol][row] == 0:
                row -= 1

            row += 1

            self.playerJustMoved = 3 - self.playerJustMoved
            self.board[movecol][row] = self.playerJustMoved
            if self.DoesMoveWin(movecol, row):
                self.winner = self.playerJustMoved
        except AssertionError:
            print("Invalid Move!")

    def GetMoves(self):
        """
        :returns: array with all possible moves, index of columns which aren't full
        """
        if self.winner != 0:
            return []
        return [col for col in range(self.width) if self.board[col][self.height - 1] == 0]

    def DoesMoveWin(self, x, y):
        """
        Checks whether a newly dropped chip at position param x, param y
        wins the game.
        :param x: column index
        :param y: row index
        :returns: (boolean) True if the previous move has won the game
        """
        me = self.board[x][y]
        for (dx, dy) in [(0, +1), (+1, +1), (+1, 0), (+1, -1)]:  # all possible diagonals/verticals/horizontals (can't do winning drop from bottom tho)
            p = 1
            while self.IsOnBoard(x + p * dx, y + p * dy) and self.board[x + p * dx][y + p * dy] == me:
                p += 1
            n = 1
            while self.IsOnBoard(x - n * dx, y - n * dy) and self.board[x - n * dx][y - n * dy] == me:
                n += 1

            if p + n >= (self.connect + 1):  # want (p-1) + (n-1) + 1 >= 4, or more simply p + n >- 5
                return True

        return False

    def IsOnBoard(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def GetResult(self, player):
        """
        :param player: (int) player which we want to see if he / she is a winner
        :returns: winner from the perspective of the param player
        """
        return player == self.winner

    def __repr__(self):
        s = ""
        for x in range(self.height - 1, -1, -1):
            for y in range(self.width):
                s += [Back.WHITE + Fore.WHITE + '.', Back.BLACK + Fore.WHITE + 'X', Back.BLACK + Fore.WHITE + 'O'][
                    self.board[y][x]]
                s += Fore.RESET
                s += Back.RESET
            s += "\n"
        s += "\n\n\n"
        return s


def PrintGameResults(state):
    """
    Print match results. Function assumes match is over.
    """
    if state.winner != 0:
        if state.GetResult(state.playerJustMoved) == 1.0:
            print(str(state))
            print("Player " + str(state.playerJustMoved) + " wins!")
        else:
            print(str(state))
            print("Player " + str(3 - state.playerJustMoved) + " wins!")

    else:
        print("Nobody wins!")


def PlayGame(initialState):
    state = initialState
    while not state.IsGameOver():
        # Render
        print(str(state))
        # Capture user input
        if state.playerJustMoved == 1:
            # Player 2 turn
            move = random.choice(state.GetMoves())
        else:
            # Player 1 turn
            move = random.choice(state.GetMoves())
        # Update game state
        state.DoMove(move)

    PrintGameResults(state)


"""
Intelligent Systems 1
Week 5 Lab Sheet
Dr James Stovold
This week we are going to be playing Connect 4.
Connect 4 is a two player, zero-sum, symmetrical connection game, in which players take turns
dropping one coloured disc from the top into a seven-column, six-row grid. The pieces fall straight
down, occupying the lowest available space within the column. The objective of the game is to be
the first to form a horizontal, vertical or diagonal line of four of one's own discs.
In order to represent Connect 4 programmatically, we need to define a game state. This has been
provided for you in the form of the GameState interface. This interface is comprised of the
following functions:
• Clone(): Creates a deep copy of the a game state.
• GetMoves(): Returns a list containing all the possible moves (actions) that an agent can
execute at this state. A state with no available moves is also known as a terminal state, as
the game cannot advance from this state onwards.
• GetResult(): To query the outcome of a game upon termination.
• DoMove(): The model of the environment. Performs an action in a given state, modifying
state. This function is sometimes refered to as the Step() function.
I have also produced a piece of code which specifically implements the Connect 4 game. In
connect4.py, you will see the Connect4State class and some helper functions, such as
PrintGameResults() and PlayGame(). At the moment, the PlayGame() function plays randomly for
both players.
1. Familiarise yourself with the code provided in connect4.py, make sure you know how the
game is played by a computer (albeit randomly) before proceeding.
2. Implement a class which represents one node of a game tree.
a. This class should be able to store all its child nodes, along with which player has
just moved, the state of the game at that point, and the minimax value for that
node.
b. This class should also have functions which can update the minimax value
according to the values of its children, and a function to generate its child nodes
(i.e. the successor function). 
3. Using your class from (2), implement minimax search for Connect 4. To start with, I suggest
you stick with a small form of Connect 4, rather than the default 7x6 game. It may be useful
to use the Clone() function so that you aren’t playing directly on the game board.
a. Implement a function which builds the entire game tree when passed an instance
of Connect4State.
N.B. using a Connect 4 game which is larger than about 3x4 will likely result in a
game tree which is too big for your computer.
b. Implement a function which looks like PlayGame() but which uses the minimax
tree to determine the best move.
N.B. using numpy’s argwhere function and the random.choice function may be
useful if you want to randomly select an index from a list.
c. How well does your game work? How long does it take to generate the tree? How
long to make a move? Why?
4. Implement a heuristic function that estimates the quality of a given non-terminal game
state.
a. Does this speed up your search?
b. How does it affect play?
N.B. using a heuristic allows you to limit the lookahead of the game AI, this should
allow you to use larger game boards (I’ve found it works up to 10x10 on my laptop
before it starts to struggle).
Challenge 1: Write a version of PlayGame() which allows the user to pick which move to make for
one of the players. How well does your minimax agent play? What about your agent from (4)?
Challenge 2: Look up Monte Carlo Tree Search (MCTS) – can you extend your implementation to
work with MCTS?"""


# coding

def AccPlayGame(initialState):  # copy paste tbf
    state = initialState
    while not state.IsGameOver():
        # Render
        print(str(state))
        # Capture user input
        if state.playerJustMoved == 1:
            # Player 2 turn
            move = random.choice(state.GetMoves())
        else:
            # Player 1 turn
            move = int(input("type the column you want to put drop a chip into from 1 being the left most column onwards ~ this is connect 4")) - 1
        # Update game state
        state.DoMove(move)

    PrintGameResults(state)


class GameTreeNode:  # a node of a game tree, with a tree being a connected acyclic graph

    def __init__(self, move=None, parent=None, game_state=None):
        self.parentNode = parent  # None for the root node
        self.childNodes = []
        self.gameState = game_state.Clone()

        self.moveJustMoved = move
        if game_state is not None:
            self.playerJustMoved = game_state.playerJustMoved  # to later check if this move has caused them to win or lose
        self.minimaxValue = 0

    def propogatingChildren(self):  # a setter
        successors = dict()
        actions = self.gameState.GetMoves()
        for action in actions:
            new_game_state = self.gameState.Clone()
            new_game_state.DoMove(action)
            child_game_state_node = GameTreeNode(action, self, new_game_state)
            self.childNodes.append(child_game_state_node)
            successors[action] = child_game_state_node
        return successors

    def updatingMiniMax(self, heuristic=None):  # updates minimax value from perspective of current player
        # (thus minimising the maximum payoff of current player's opponent) - calculating values from player 1's end
        children = self.childNodes
        me = self.playerJustMoved
        if children:
            if me == 1:
                self.minimaxValue = max(child.minimaxValue for child in children)  # as player 1's fortune lies in the max (due to the notation of the values being from P1's POV) - attempting to maximise their own minimum payoff
            else:
                self.minimaxValue = min(child.minimaxValue for child in children)  # as player 2's maximum payoff lies in the minimums of the notation
        else:  # aka when children is empty i.e terminal node - so game ended
            if heuristic is not None:  # a function that predicts how good a position this is for player 1 (and thus bad for player 2 - poor 2, but that's why they look for min)
                self.minimaxValue = heuristic(self)
            else:
                # last player that made a move is the winner
                self.minimaxValue = 4 if me == 1 else -4
        return


def BuildGameTree(state_instance):
    # RecursionError: maximum recursion depth exceeded in comparison
    def _buildSubGameTree(sub_tree_root, visited=[]):
        # actual recursion goes on here - depth first searching
        if sub_tree_root.gameState.IsGameOver():
            sub_tree_root.updatingMiniMax()  # links to latter half of the update function
            return root
        successors = root.propogatingChildren()
        successors = root.childNodes
        for child in successors:
            child = _buildSubGameTree(child)  # holding new version of node
            child.updatingMiniMax()  # from the descendents, links to former half of the update function
        return root

    root = GameTreeNode(game_state=state_instance)
    root = _buildSubGameTree(root)
    return root

def AccPlayGame(initialState):
    state = initialState
    while not state.IsGameOver():
        # Render
        print(str(state))
        # Capture user input
        if state.playerJustMoved == 1:
            # Player 2 turn
            move = random.choice(state.GetMoves())
        else:
            # Player 1 turn
            move = int(input("type the column you want to put drop a chip into from 1 being the left most column onwards ~ this is connect 4")) - 1
        # Update game state
        state.DoMove(move)

    PrintGameResults(state)


def WatchGameMiniMaxStyle(initial_game_state):
    game_state = initial_game_state
    print("Building game tree...")
    game_tree_root = BuildGameTree(initial_game_state)
    print("Playing game...")
    current_game_tree_node = game_tree_root
    while not game_state.IsGameOver():
        print(str(game_state))  # render graphics
        children = current_game_tree_node.childNodes
        children_minimax_values = [child.minimaxValue for child in children]
        if game_state.player_just_moved == 1:  # therefore player 2 (min)'s turn
            # min_minimax_value = min(children_minimax_values)
            # now to find the child with the desired value, we could use:
            # children_minimax_values.index(min_minimax_value)
            # however this is limited to just giving the left most option in the list...
            # so to randomise things ~~~ we can do the following to select from any of the valid options
            random_valid_minimax_value_index = np.argwhere(np.array(children_minimax_values) == np.min(children_minimax_values)).flatten().tolist()
            # conversions needed to use handy np.argwhere() function
            random_valid_minimax_value_index = random.choice(random_valid_minimax_value_index)
        else:  # therefore player 1 (max)'s turn
            # max_minimax_value = max(children_minimax_values)
            random_valid_minimax_value_index = np.argwhere(np.array(children_minimax_values) == np.max(children_minimax_values)).flatten().tolist()
            random_valid_minimax_value_index = random.choice(random_valid_minimax_value_index)
        move = children[random_valid_minimax_value_index].moveJustMoved
        game_state.DoMove(move)
        current_game_tree_node = children[random_valid_minimax_value_index]

    PrintGameResults(game_state)


def AccPlayGameMiniMaxStyle():
    pass


def BuildGameTree_DL(initialState, depth=5):  # #NotMyCodeAtAll
    # depth limited
    root = GameTreeNode(game_state=initialState)
    # depth-first search
    root = buildSubTree_DL(root, depth)
    return root


def buildSubTree_DL(root, depth):
    if root.gameState.IsGameOver() or depth == 0:
        root.updatingMiniMax(heuristic)
        return root
    root.propogatingChildren()
    for child in root.childNodes:
        child = buildSubTree_DL(child, depth - 1)
        child.updatingMiniMax(heuristic)
    return root


def heuristic(node):  # #NotMyCodeAtAll
    # check who's move it is
    currentPlayer = 3 - node.playerJustMoved
    currentMax = 0
    # count highest number of adjacent/diag pieces
    for x in range(node.gameState.width):
        for y in range(node.gameState.height):
            me = node.gameState.board[x][y]
            if me == currentPlayer:
                for (dx, dy) in [(0, +1), (+1, +1), (+1, 0), (+1, -1)]:
                    p = 1
                    while node.gameState.IsOnBoard(x + p * dx, y + p * dy) and node.gameState.board[x + p * dx][
                        y + p * dy] == me:
                        p += 1
                    n = 1
                    while node.gameState.IsOnBoard(x - n * dx, y - n * dy) and node.gameState.board[x - n * dx][
                        y - n * dy] == me:
                        n += 1

                    if p + n > currentMax:
                        currentMax = p + n

            y += 1
        x += 1
    if currentPlayer == 1:  # max
        return currentMax
    else:
        return -currentMax


def PlayGameMinimax_heur(initialState, lookahead=4):
    state = initialState
    currentRootNode = BuildGameTree_DL(initialState, depth=lookahead)
    while not state.IsGameOver():
        # Render
        print(str(state))
        # Capture user input
        children = currentRootNode.childNodes
        vals = [child.minimaxValue for child in children]
        if state.playerJustMoved == 1:
            # Min's turn
            minval = min(vals)
            idx = np.argwhere(np.array(vals) == np.min(vals)).flatten().tolist()
            idx = random.choice(idx)
        else:
            # Max's turn
            maxval = max(vals)
            idx = np.argwhere(np.array(vals) == np.max(vals)).flatten().tolist()
            idx = random.choice(idx)

        move = children[idx].moveJustMoved
        # Update game state
        state.DoMove(move)
        currentRootNode = BuildGameTree_DL(children[idx].gameState, depth=lookahead)

    PrintGameResults(state)


colorama.init()


state_heuristiced = Connect4State(width=7, height=6)
PlayGameMinimax_heur(state_heuristiced, lookahead=4)

# env = Connect4State(width=3, height=4)
# PlayGame(env)
# AccPlayGame(env)
# WatchGameMiniMaxStyle(env)
# AccPlayGameMiniMaxStyle(env)
