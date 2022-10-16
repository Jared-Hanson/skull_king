from termcolor import colored

def get_input(text, inputs_allowed):
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            txt = input(f"{text}: ")
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue
        if txt in inputs_allowed:
            break
        else:
            print("Sorry, I didn't understand that.")
    return txt

def get_input_int(text, inputs_allowed):
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            txt = int(input(f"{text}: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue
        if txt in inputs_allowed:
            break
        else:
            print("Sorry, I didn't understand that.")
    return txt

def print_card_list(deck, card_list):
    for card in card_list:
        print(colored(card, deck.get_formatting(card)), end=" ")

def print_card(deck, card):
    print(colored(card, deck.get_formatting(card)), end=" ")