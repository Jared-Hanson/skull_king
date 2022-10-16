
from utils import get_input, get_input_int, print_card_list

class CPUPlayer():
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
            self.score -= self.current_bid * 10
        
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
            

        card = self.determine_card_to_play(playable, self.deck.determine_winner(cards_played, cur_suit))
        self.hand.remove(card)
        return card
    
    def determine_card_to_play(self, playable, current_winning_card):
        if self.current_tricks_won >= self.current_bid:
            print("We want to loose")
            # Try to score low. 
            lowest_card = None
            for card in playable:
                if self.deck.get_value(card) <= self.deck.get_value(current_winning_card):
                    if lowest_card is not None:
                        if self.deck.get_value(card) > self.deck.get_value(lowest_card):
                            lowest_card = card
                    else:
                        lowest_card = card
            if lowest_card is None:
                values = [self.deck.get_value(card) for card in playable]
                if current_winning_card is None:
                    idx = values.index(min(values))
                else:
                    idx = values.index(max(values))
                lowest_card = playable[idx]
            return lowest_card

        else:
            # Try and win
            print("We want to win")
            highest_card = None
            for card in playable:
                if self.deck.get_value(card) > self.deck.get_value(current_winning_card):
                    if highest_card is not None:
                        if self.deck.get_value(card) < self.deck.get_value(highest_card):
                            highest_card = card
                    else:
                        highest_card = card
            if highest_card is None:
                values = [self.deck.get_value(card) for card in playable]
                if current_winning_card is None:
                    idx = values.index(max(values))
                else:
                    idx = values.index(min(values))
                highest_card = playable[idx]
            return highest_card

    def get_bid(self):
        bid = 0
        for card in self.hand:
            if self.deck.get_value(card) in [13, 21,22,23,24,25,26,30,35]:
                bid += 1

        self.current_bid = bid
        return bid
    