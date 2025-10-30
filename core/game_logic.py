from player_io import ask_player_action
def calculate_hand_value(hand: list[dict]) -> int:
    total = 0
    value = 0
    for card in hand:
            if card["rank"] == "J":
                value = 10
                total+=value
            elif card["rank"] == "Q":
                value = 10
            elif card["rank"] == "K":
                value = 10
            elif card["rank"] == "A":
                value = 1
            else:    
                value = int(card["rank"])
            total += value
    return total

hand = [{"rank":"A", "suite":"H"}, {"rank":"K", "suite":"H"}]


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    card_player1 = deck.pop(0)
    card_player2 = deck.pop(0)
    player["hand"].append(card_player1)
    player["hand"].append(card_player2)
    card_dealer1 = deck.pop(0)
    card_dealer2 = deck.pop(0)
    player["hand"].append(card_dealer1)
    player["hand"].append(card_dealer2)
    val_hand_player = calculate_hand_value(player["hand"])
    print(val_hand_player)
    print()
    val_hand_dealer = calculate_hand_value(dealer["hand"])
    print(val_hand_dealer)
    

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    dealer_queue = True
    while dealer_queue == True:
        card = deck.pop(0)
        dealer["hand"].append(card)
        val_hand_dealer = calculate_hand_value(dealer["hand"])
        if val_hand_dealer >= 17:
            if val_hand_dealer > 21:
                print("🎉, player is won.")
                dealer_queue = False
            else:
                break
    return dealer_queue

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck)
    player_queue = True
    while player_queue:
        Players_answer = ask_player_action()
        if Players_answer == "H":
            player["hand"].append(deck.pop(0))
            val_hand_player = calculate_hand_value(player["hand"])
            if val_hand_player > 21:
                print("end game, 😒, dealer is won.")
                break
        elif Players_answer == "S":
            dealer_play(deck,dealer)
    
    end_val_pleyer = player["hand"]
    end_val_dealer = dealer["hand"]
    print(f"the val for player is: {end_val_pleyer}, the val for dealer is: {end_val_dealer}")

    if end_val_pleyer > end_val_dealer:
        print("🎉, player is won.")
    else:
        print("😒, dealer is won.")

        




        
            
                
