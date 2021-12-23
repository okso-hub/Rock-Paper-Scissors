from random import choice
from time import sleep

# Person vs Computer
pc = False
# pvp
pp = False
points1 = 0
points2 = 0

# Choice -> Person vs Computer / PvP
gameMode = int(input("1 -> 1 VS 1 \n2 -> 1 VS CPU \n"))

# PvP Modus | Names and boolean
if gameMode == 1:
     player1_name = str(input("Name of player 1: "))
     player2_name = str(input("Name of player 2: "))
     pp = True

# Person vs CPU 
elif gameMode == 2:
     pc = True

# while loop for p vs cpu
while pc:
     player = int(input("Choose your weapon! \n \n1 -> Rock \n2 -> Paper \n3 -> Scissors\n4 -> End the game\n"))
     cpu = choice(["Rock", "Paper", "Scissors"]) 

     if player == 1:
          sleep(1.5)
          if cpu == "Rock":
               print("The computer chose Rock too! \nNobody won!")
          elif cpu == "Paper":
               print("The computer chose Paper! \nThe computer won! \nNEW ROUND \n \n")
          else:
               print("The computer chose Scissors! \nYou won! \nNEW ROUND \n \n")

     elif player == 2:
          sleep(1.5)
          if cpu == "Paper":
               print("The computer chose Paper too! \nNobody won!")
          elif cpu == "Scissors":
               print("The computer chose Scissors! \nThe computer won! \nNEW ROUND \n \n")
          else:
               print("The computer chose Rock! \nYou won! \nNEW ROUND \n \n")

     elif player == 3:
          sleep(1.5)
          if cpu == "Scissors":
               sleep(1.5)
               print("The computer chose Scissors too! \nNobody won!")
          elif cpu == "Rock":
               print("The computer chose Rock! \nThe computer won! \nNEW ROUND \n \n")
          else:
               print("The computer chose Paper! \nYou won! \nNEW ROUND \n \n")
          

     if player == 4:
          print("Game ends.")
          break

# while loop for 1vs1
while pp:
     
     player1 = int(input(f"Choose your weapon, {player1_name}! \n \n1 -> Rock \n2 -> Paper \n3 -> Scissors\n4 -> End game\n"))
     player2 = int(input(f"Choose your weapon, {player2_name}! \n \n1 -> Rock \n2 -> Paper \n3 -> Scissors\n4 -> End game\n"))

     #global points1
     #global points2

     if player1 == 1:
          if player2 == player1:
               sleep(1.5)
               print("\n \nBoth of you chose Rock \nNobody won! \n \n")
               print(f"Points:\n{player1_name}: {points1}, {player2_name}: {points2}")
          elif player2 == 2:
               sleep(1.5)
               print(f"\n \n" + player1_name + ": Rock \n" + player2_name + ": Paper \n" + player2_name, " won! \n \n")
               points2 += 1
               print(f"Points:\n{player1_name}: {points1}, {player2_name}: {points2}")
          elif player2 == 3:
               sleep(1.5)
               print(f"\n \n" + player1_name, ": Rock \n" + player2_name + ": Scissors \n" + player1_name, "won! \n \n")
               points1 += 1
               print(f"Points:\n" + player1_name + ":", points1, player2_name + ":", points2)
     elif player1 == 2:
          if player2 == player1:
               sleep(1.5)
               print("\n \nBoth of you chose Paper \nNobody won! \n \n")
               print(f"Points:\n{player1_name}: {points1}, {player2_name}: {points2}")
          elif player2 == 1:
               sleep(1.5)
               print(f"\n \n" + player1_name + ": Paper \n" + player2_name + ": Rock \n" + player1_name, "won! \n \n")
               points1 += 1
               print(f"Points:\n{player1_name}: {points1}, {player2_name}: {points2}")
     elif player1 == 3:
          if player2 == player1:
               sleep(1.5)
               print("\n \nBoth of you chose Scissors \nNobody won! \n \n")
               print(f"Points:\n{player1_name}: {points1}, {player2_name}: {points2}")
          elif player2 == 1:
               sleep(1.5)
               print(f"\n \n" + player1_name + ": Scissors \n" + player2_name + ": Rock\n" + player2_name, "won! \n \n")
               points2 += 1
               print(f"Points:\n{player1_name}: {points1}, {player2_name}: {points2}")
          elif player2 == 2:
               sleep(1.5)
               print(f"\n \n" + player1_name + ": Scissors\n" + player2_name + ": Paper\n" + player1_name, "won! \n \n")
               points1 += 1
               print(f"Points:\n{player1_name}: {points1}, {player2_name}: {points2}")
     elif player1 == 4:
          print("Game ends.")
          break
