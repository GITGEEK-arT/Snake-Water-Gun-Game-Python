# project of snake, water and gun game:
import random
def SWG():
    tie_score =0
    player1_score =0
    computer_score =0
    print("welcome to the game of snake,water,gun")
    while True:
        player1 = input("Enter your choice (snake/water/gun): ").lower()
        computer_choice= random.choice(['snake', 'water', 'gun'])
        print(f"computer's choice: {computer_choice}")
        print(f"player's choice: {player1}")
        if player1 not in ['snake', 'water', 'gun']:
            print("Invalid choice ! Please choose either 'snake','water' or 'gun'")
            continue
        if player1 == computer_choice:
            print("it was a tie")
            tie_score+=1
            print(f"Score: Player1:{player1_score}, Computer:{computer_score}, Ties:{tie_score}")
        elif (player1 == 'snake' and computer_choice == 'water') or \
            (player1 == 'water' and computer_choice == 'gun') or \
            (player1 == 'gun' and computer_choice == 'snake'):
            print("player 1 wins !")
            player1_score+=1
            print(f"Score: Player1:{player1_score}, Computer:{computer_score}, Ties:{tie_score}")
        else:
            print("computer wins !")
            computer_score+=1
            print(f"Score: Player1:{player1_score}, Computer:{computer_score}, Ties:{tie_score}")
        again= input("Do you want to play again? (yes/no): ").lower()
        if again == 'yes':
            print("allright let's get started !") 
        elif again == 'no':
            print(f"Final Score are: Player1:{player1_score}, Computer:{computer_score}, Ties:{tie_score}")
            print("Thanks for playing !")
            break
SWG()

