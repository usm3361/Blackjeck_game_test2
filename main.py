from core.game_logic import run_full_game
from core.deck import shuffle_by_suit, build_standard_deck

if __name__ == "__main__":
    deck = build_standard_deck()
    shuffle_by_suit(deck)

    player = {"hand": [ ] }
    dealer = {"hand": [ ] }

    run_full_game(deck, player, dealer)


