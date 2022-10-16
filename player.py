
from utils import get_input, get_input_int, print_card_list

class Player():
    def __init__(self, deck, seat_location):
        self.deck = deck
        self.hand = None
        self.score = 0
        self.current_bid = None
        self.current_tricks_won = 0
        self.cur_hand_size = 0
        self.index = seat_location

    def _reset(self):
        self.hand = None
        self.current_bid = None
        self.current_tricks_won = 0
        self.cur_hand_size = None

    def calculate_score_and_reset(self):
        print(f"At the start of the round, the score for player {self.index} was {self.score}")
        if self.current_bid == 0:
            if self.current_tricks_won == 0:
                self.score += self.cur_hand_size * 10
            else:
                self.score -= self.cur_hand_size * 10
        elif self.current_tricks_won == self.current_bid:
            self.score += self.current_bid * 20
        else:
            self.score -= abs(self.current_tricks_won - self.current_bid) * 10
        
        self._reset()
        print(f"Now it is {self.score}")

    def set_hand(self, hand):
        self.cur_hand_size = len(hand)
        self.hand = hand.copy()
    
    def play_card(self, cur_suit, cards_played):
        print(f"Current Suit = {cur_suit}")
        if cur_suit == None or cur_suit == "M":
            playable = self.hand
            unplayable = []
        else:
            playable = []
            unplayable = []
            magic = []
            for card in self.hand:
                if self.deck.get_color(card) == "M":
                    magic.append(card)
                elif self.deck.get_color(card) == cur_suit:
                    playable.append(card)
                else:
                    unplayable.append(card)
            
            if len(playable) == 0:
                playable = unplayable.copy()
                unplayable = []
            playable.extend(magic)
            
        print(f"Unplayable Cards: ", end=" ")
        print_card_list(self.deck, unplayable)

        print(f"\nPlayable Cards: ", end=" ")
        print_card_list(self.deck, playable)
        card = get_input("\nPlease type the card chosen", playable)
        self.hand.remove(card)
        return card
    
    def get_bid(self):
        bid = get_input_int("\nPlease give the number of tricks you want to win", [i for i in range(self.cur_hand_size)])
        self.current_bid = bid
        return bid
    