import random
import json

def play_hilo():
    high_score = get_high_score()
    high_score_name = high_score[0]
    high_score_num = high_score[1]
    print(f"CURRENT HIGH SCORE: \n\tNAME: {high_score_name}\n\tSCORE: {high_score_num}")
    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    player_score = 300
    game_done = False
    while game_done != True and player_score > 0:
        current_card = random.choice(cards)
        print(f"\nPLAYER SCORE: {player_score}")
        print(f"\nThe current card is {current_card}")
        choice = input("Is the next card going to be higher or lower (h/l)? ").lower()
        new_card = random.choice(cards)
        while new_card == current_card:
            new_card = new_card = random.choice(cards)
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
        print(f"The new card was {new_card}")
        print(f"PLAYER SCORE: {player_score}")
        done = input("\nWould you like to play again (y/n)? ").lower()
        if done == "y":
            game_done = False
        elif done == "n":
            game_done = True
    if player_score > high_score_num:
            print(f"\n{player_score} is the new high score!")
            save_high_score(player_score)
    print("\n\nHave a good day!")
        

def get_high_score():
    with open("high_score.json", "r") as file:
        info = json.load(file)
    return info

def save_high_score(player_score):
    name = input("What is the username of the player? ")
    with open("high_score.json", "w") as file:
        info = name, player_score
        json.dump(info, file)

def main():
    play_hilo()

main()