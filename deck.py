import random
from dict_cards import all_cards

class SkullKingDeck():
    def __init__(self):
        self.total_cards = all_cards
        self.working_deck = self.total_cards.copy()

    def deal_cards(self, num_cards):
        hand = []
        for i in range(num_cards):
            card = random.choice(list(self.working_deck.keys()))
            hand.append(card)
            self.working_deck.pop(card)
        return hand
    
    def reset_deck(self):
        self.working_deck = self.total_cards.copy()
    
    def get_card_info(self, card):
        return self.total_cards[card]
    
    def get_formatting(self, card):
        return self.total_cards[card]["format"]

    def get_color(self, card):
        return self.total_cards[card]["color"]

    def get_value(self, card):
        if card is None:
            return 0
        return self.total_cards[card]["value"]

    def determine_winner(self, cards_played, suit):
        current_winner = None
        for card in cards_played:
            if self.get_color(card) in [suit, "M", "B"]:
                if self.get_value(current_winner) < self.get_value(card):
                    current_winner = card
        return current_winner

