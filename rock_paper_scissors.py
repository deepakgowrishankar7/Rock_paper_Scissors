import random

user=int(input("Type 1 for 'ROCK' 2 for 'PAPER' 3 for 'SCISSORS':"))


#computer choice
list1=["rock","paper","scissors"]
computer_choice=random.choice(list1)
print("Computer Choice:")
if computer_choice == "rock":
    print("""
    ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)
elif computer_choice == "paper":
    print("""
    PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """)
elif computer_choice== "scissors":
    print("""
    SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """)
else:
    print("Error")



#User input
print("Your Choice:")
if user == 1:
    print("""
    ROCK  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif user == 2:
    print("""
    PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
elif user == 3:
    print( """
    SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("INVALID choise")


#condition to WIN or LOSE
if user == 1:
    if computer_choice == "rock":
        print("Draw")
    elif computer_choice == "paper":
        print("Computer win")
    elif computer_choice == "scissors":
        print("You Win")
    else:
        print("Error")
elif user == 2:
    if computer_choice == "rock":
        print("You win")
    elif computer_choice == "paper":
        print("Draw")
    elif computer_choice == "scissors":
        print("Computer win")
    else:
        print("Error")
elif user == 3:
    if computer_choice == "rock":
        print("Computer win")
    elif computer_choice == "paper":
        print("You win")
    elif computer_choice == "scissors":
        print("Draw")
    else:
        print("Error")
else:
    print("Error")
