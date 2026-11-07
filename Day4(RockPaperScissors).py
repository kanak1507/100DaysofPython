import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [rock, paper, scissors]
computer = random.randint(0,2)
print("Welcome to Rock, Paper, Scissors.")
choice = input("Enter Your choice:"
      "1:Rock"
      "2:Paper"
      "3:Scissors\n ")
if choice == "1":
    print(f"You chose:{rock}")
    print(f"Computer chose:{image[computer]}")
    if computer == 0:  # Computer chose Rock
        print("Draw!")
    elif computer == 1:  # Computer chose Paper
        print("You lose!")
    else:  # Computer chose Scissors
        print("You win!")
elif choice == "2":
    print(f"You chose:{paper}")
    print(f"Computer chose:{image[computer]}")
    if computer == 0:  # Computer chose Rock
        print("You win!")
    elif computer == 1:  # Computer chose Paper
        print("Draw!")
    else:  # Computer chose Scissors
        print("You lose!")
elif choice == "3":
    print(f"You chose: {scissors}")
    print(f"Computer chose:{image[computer]}")
    if computer == 0:  # Computer chose Rock
        print("You lose!")
    elif computer == 1:  # Computer chose Paper
        print("You win!")
    else:  # Computer chose Scissors
        print("Draw!")

