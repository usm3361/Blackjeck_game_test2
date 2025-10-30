def build_standard_deck() -> list[dict]:
    SUITES=["H","C","D","S"]
    RANKS=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    cards = []
    for s in SUITES:
        for r in RANKS:
            card = {}
            card["rank"] = r
            card["SUITES"] = s
            cards.append(card)

    return cards

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    return[{}]


print(len(build_standard_deck()))