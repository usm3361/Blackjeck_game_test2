def ask_player_action() -> str:
    is_valid = False
    while not is_valid:
        question = input("Would you like to play or pass to the dealer?     ")
            
        if question != "H" and question != "S":
            print()
            print("press only 'H' or 'S' - Capital letters")
        else:
            is_valid = True
                        
    return question