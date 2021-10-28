import random
import json

def play_hilo():
    """Plays the game of HiLo"""

    # Get high score
    high_score = get_high_score()
    high_score_name = high_score[0]
    high_score_num = high_score[1]

    # Display high score
    print(f"CURRENT HIGH SCORE: \n\tNAME: {high_score_name}\n\tSCORE: {high_score_num}")

    # Create cards
    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    # Create starting player score
    player_score = 300

    # Create game loop
    game_done = False
    while game_done != True or player_score > 0:

        # Deal a random card
        current_card = random.choice(cards)

        # Display player score and the dealt card
        print(f"\nPLAYER SCORE: {player_score}")
        print(f"\nThe current card is {current_card}")

        # Get the players turn
        choice = input("Is the next card going to be higher or lower (h/l)? ").lower()

        # Deal new card
        new_card = random.choice(cards)

        # Make sure the new card is different from the dealt card
        while new_card == current_card:
            new_card = new_card = random.choice(cards)

        # Distribute points
        if choice == "h":
            if new_card > current_card:
                player_score += 100
                print("Good job!")
            elif new_card < current_card:
                player_score -= 75
                print("Better luck next time!")
        elif choice == "l":
            if new_card < current_card:
                player_score += 100
                print("Good job!")
            elif new_card > current_card:
                player_score -= 75
                print("Better luck next time!")

        # Display what the new card was
        print(f"The new card was {new_card}")

        # Display the updated player score
        print(f"PLAYER SCORE: {player_score}")

        # See if the player wants to play again
        done = input("\nWould you like to play again (y/n)? ").lower()
        if done == "y":
            game_done = False
        elif done == "n":
            game_done = True

    # Check if the player score was a new high score
    if player_score > high_score_num:
            print(f"\n{player_score} is the new high score!")
            save_high_score(player_score)
    print("\n\nHave a good day!")
        

def get_high_score():
    """Gets the high score from the saved file"""

    # Open the file
    with open("high_score.json", "r") as file:
        info = json.load(file)
    
    # Return the high score
    return info

def save_high_score(player_score):
    """Save a new high score"""

    # Get the username to save
    name = input("What is the username of the player? ")

    # Open the file
    with open("high_score.json", "w") as file:
        info = name, player_score

        # Save the high score to the file
        json.dump(info, file)

def main():
    """Program driver"""
    
    play_hilo()

main()