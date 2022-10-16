
from random import randint
from symbol import pass_stmt
from utils import print_card_list, print_card


class SkullKingGame():
    def __init__(self, rounds, players, deck):
        self.num_players = len(players)
        self.round = 1
        self.starting_player = 0
        self.players = players
        self.total_rounds = rounds
        self.deck = deck
    
    def setup_round(self):
        bids = {}
        for player in self.players:
            player.set_hand(self.deck.deal_cards(self.round))
            print(f"Player {player.index} hand is: ", end=" ")
            print_card_list(self.deck, player.hand)
            print("")
            bids[f"Player_{player.index}"] = player.get_bid()
        
        print("All players bids are as follows: ", bids)
        return self.round % self.num_players
        

    def end_round(self):
        for player in self.players:
            player.calculate_score_and_reset()
        self.deck.reset_deck()

    def play_game(self):
        print("Playing SKULL KING")
        while self.round <= self.total_rounds:
            print(f"\n\nSTARTING ROUND {self.round}")
            # PLAY GAME
            start_player = self.setup_round()
            
            for turns in range(self.round):
                print(f"\n\nPlayer {start_player} will start this trick")
                cur_suit = None
                cards_played = {}
                for player in self.players[start_player:] + self.players[:start_player]:
                    print(f"\nPlayer {player.index} turn!")
                    card_played = player.play_card(cur_suit, list(cards_played.keys()))
                    print(f"Played {card_played}!")
                    cards_played[card_played] = player.index
                    print(f"Cards played so far: ", end=" ")
                    print_card_list(self.deck, cards_played.keys())
                    print("")
                    # Set suite for boat and magic
                    
                    if cur_suit == None:
                        cur_suit = self.deck.get_color(card_played)
                        if self.deck.get_value(card_played) == 0:
                            cur_suit == None
                    
                max_card = self.deck.determine_winner(list(cards_played.keys()), cur_suit)
                start_player = cards_played[max_card]
                print("The winning card was ", end="")
                print_card(self.deck, max_card)
                print(f"and the winning player was {start_player}")
                self.players[start_player].current_tricks_won += 1

                for player in self.players:
                    print(f"Player {player.index} bid {player.current_bid} and has won {player.current_tricks_won}") 

            self.end_round()
            self.round += 1
