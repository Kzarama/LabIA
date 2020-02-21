import re
from random import sample

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():

  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self):
    #rows
    if self.board[0] == self.board[1] == self.board[2] and self.board[0] != None and self.board[1] != None and self.board[2] != None:
      self.is_game_over = True
      self.winner = self.turn
    if self.board[3] == self.board[4] == self.board[5] and self.board[3] != None and self.board[4] != None and self.board[5] != None:
      self.is_game_over = True
      self.winner = self.turn
    if self.board[6] == self.board[7] == self.board[8] and self.board[6] != None and self.board[7] != None and self.board[8] != None:
      self.is_game_over = True
      self.winner = self.turn
    #cols
    if self.board[0] == self.board[3] == self.board[6] and self.board[0] != None and self.board[3] != None and self.board[6] != None:
      self.is_game_over = True
      self.winner = self.turn
    if self.board[1] == self.board[4] == self.board[7] and self.board[1] != None and self.board[4] != None and self.board[7] != None:
      self.is_game_over = True
      self.winner = self.turn
    if self.board[2] == self.board[5] == self.board[8] and self.board[2] != None and self.board[5] != None and self.board[8] != None:
      self.is_game_over = True
      self.winner = self.turn
    #diagonals
    if self.board[0] == self.board[4] == self.board[8] and self.board[0] != None and self.board[4] != None and self.board[8] != None:
      self.is_game_over = True
      self.winner = self.turn
    if self.board[2] == self.board[4] == self.board[6] and self.board[2] != None and self.board[4] != None and self.board[6] != None:
      self.is_game_over = True
      self.winner = self.turn
    return self.is_game_over

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 1 and 9")
    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")
      return self.player_choose_cell()

    player_cell = int(player_cell) - 1

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")
      return self.player_choose_cell()

    if player_cell == 0:
      print('The number must be between 1 and 9')
      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()
    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    i = sample([x for x in range(0, 8)], 1)[0]
    if self.board[i] == None:
      self.board[i] = _MACHINE_SYMBOL
    elif self.board[i] != None:
      self.machine_turn()

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))
    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    if self.winner == _MACHINE:
      print(_PLAYER)
    elif self.winner == _PLAYER:
      print(_MACHINE)
    else:
      print('draw')
