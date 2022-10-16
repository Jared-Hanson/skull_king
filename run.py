from deck import SkullKingDeck
from game import SkullKingGame
from player import Player
from cpu_player import CPUPlayer
from termcolor import colored

deck = SkullKingDeck()

players = [Player(deck, 0), CPUPlayer(deck, 1), CPUPlayer(deck, 2), CPUPlayer(deck, 3)]

game = SkullKingGame(6, players, deck)
game.play_game()