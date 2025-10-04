#!/usr/bin/env python3
"""
Terminal Tic-Tac-Toe (two players)

Features:
- Input validation (only accepts 1-9, unoccupied)
- Replay support and running scoreboard (X wins, O wins, Draws)
- Improved board display: when prompting it shows numbers for empty squares
- Graceful handling of KeyboardInterrupt / quit commands

Play locally with two players sharing the same terminal.

Controls:
- Enter a number 1-9 to place your mark (see the board layout below)
- Enter q or quit to exit the program
"""

from typing import List, Optional
import os
import sys


class TicTacToe:
	WIN_COMBINATIONS = [
		(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
		(0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
		(0, 4, 8), (2, 4, 6)              # diagonals
	]

	def __init__(self):
		self.board: List[Optional[str]] = [None] * 9

	def reset(self) -> None:
		self.board = [None] * 9

	def display(self, show_indices_when_empty: bool = False) -> None:
		"""Print the board. If show_indices_when_empty is True, empty cells
		are printed as 1-9 to help users choose a square.
		"""
		def cell(i: int) -> str:
			mark = self.board[i]
			if mark is not None:
				return mark
			if show_indices_when_empty:
				return str(i + 1)
			return " "

		rows = []
		for r in range(3):
			row_cells = [cell(r * 3 + c) for c in range(3)]
			rows.append(" {} | {} | {} ".format(*row_cells))
		sep = "\n---+---+---\n"
		print(sep.join(rows))

	def make_move(self, position: int, player: str) -> bool:
		"""Place player's mark at position (0-based). Return True if placed."""
		if 0 <= position < 9 and self.board[position] is None:
			self.board[position] = player
			return True
		return False

	def winner(self) -> Optional[str]:
		for a, b, c in self.WIN_COMBINATIONS:
			if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
				return self.board[a]
		if all(cell is not None for cell in self.board):
			return "Draw"
		return None


def clear_screen() -> None:
	# Attempt to clear the terminal for nicer UX; fall back to printing newlines.
	try:
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
	except Exception:
		print("\n" * 3)


def prompt_move(player: str) -> Optional[str]:
	"""Prompt the player for a move. Returns the raw input or None on EOF."""
	try:
		return input(f"Player {player}, enter square (1-9) or 'q' to quit: ").strip()
	except EOFError:
		return None


def run_game_interactive() -> None:
	scoreboard = {"X": 0, "O": 0, "Draw": 0}
	game = TicTacToe()
	current_player = "X"

	try:
		while True:
			clear_screen()
			print("Tic-Tac-Toe")
			print("-------------")
			print('\nCurrent scoreboard: X={X}  O={O}  Draws={D}\n'.format(X=scoreboard['X'], O=scoreboard['O'], D=scoreboard['Draw']))
			print("Board layout (use the numbers to choose a square):")
			game.display(show_indices_when_empty=True)

			# Prompt until valid move or quit
			while True:
				raw = prompt_move(current_player)
				if raw is None:
					# EOF (e.g., Ctrl+D) - treat as quit
					print('\nExiting...')
					raise KeyboardInterrupt
				raw_lower = raw.lower()
				if raw_lower in ("q", "quit"):
					print("Quitting the game.")
					raise KeyboardInterrupt
				if not raw.isdigit():
					print("Please enter a number 1-9 (or 'q' to quit).")
					continue
				pos = int(raw) - 1
				if pos < 0 or pos > 8:
					print("Choice out of range. Please enter 1-9.")
					continue
				if not game.make_move(pos, current_player):
					print("That square is already taken. Choose another.")
					continue
				break

			# Show updated board
			clear_screen()
			print("Tic-Tac-Toe")
			print("-------------")
			game.display(show_indices_when_empty=False)

			# Check for winner or draw
			result = game.winner()
			if result is not None:
				if result == "Draw":
					print("It's a draw!")
					scoreboard["Draw"] += 1
				else:
					print(f"Player {result} wins!")
					scoreboard[result] += 1

				print('\nScoreboard: X={X}  O={O}  Draws={D}\n'.format(X=scoreboard['X'], O=scoreboard['O'], D=scoreboard['Draw']))
				# Prompt for replay
				while True:
					again = input("Play again? (y/n): ").strip().lower()
					if again in ("y", "yes"):
						game.reset()
						current_player = "X"
						break
					if again in ("n", "no"):
						print("Thanks for playing! Final scoreboard:")
						print('X={X}  O={O}  Draws={D}'.format(X=scoreboard['X'], O=scoreboard['O'], D=scoreboard['Draw']))
						return
					print("Please answer 'y' or 'n'.")
			else:
				current_player = "O" if current_player == "X" else "X"

	except KeyboardInterrupt:
		print('\nInterrupted. Final scoreboard:')
		print('X={X}  O={O}  Draws={D}'.format(X=scoreboard['X'], O=scoreboard['O'], D=scoreboard['Draw']))


def _self_test_quick() -> None:
	"""A quick non-interactive smoke test of core logic used by automated checks.
	Not run by default from CLI; used by automated runner below.
	"""
	t = TicTacToe()
	assert t.make_move(0, 'X')
	assert t.make_move(1, 'X')  # still allowed until three-in-row
	assert not t.make_move(0, 'O')
	t.reset()
	# simulate a winning line
	t.make_move(0, 'X')
	t.make_move(1, 'X')
	t.make_move(2, 'X')
	assert t.winner() == 'X'


if __name__ == '__main__':
	# If called with --self-test, run a quick internal test and exit with code.
	if '--self-test' in sys.argv:
		try:
			_self_test_quick()
			print('Self-test OK')
			sys.exit(0)
		except AssertionError as e:
			print('Self-test FAILED:', e)
			sys.exit(2)

	run_game_interactive()

