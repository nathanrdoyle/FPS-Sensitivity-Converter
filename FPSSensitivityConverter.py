# Nathan Doyle
# May 15, 2024
# Converts the sensitivity of one FPS game into sensitivities of other FPS games.

def main(): 
  referenceGame = input("What is the game you are converting your sensitivty from? (Apex Legends, Destiny 2, COD: Warzone, CS:GO, VALORANT, Rainbow 6 Siege, Overwatch, Fortnite)")
  referenceSensitivity = input("What is your sensitivty in " + referenceGame + "?")

  conversion(referenceGame, referenceSensitivity)
  
def conversion(referenceGame, referenceSensitivity):
  
  apexToDestiny = 3.333333
  apexToWarzone = 3.333333
  apexToValorant = 0.314286
  apexToRainbow = 3.839724
  apexToOverwatch = 3.333333
  apexToFortnite = 3.960396

  destinyToApex = 0.3
  destinyToCS = 0.3
  destinyToValorant = 0.094286
  destinyToFortnite = 1.188119
  destinyToRainbow = 1.151917
  

  if referenceGame == "Apex Legends" or referenceGame == "CS:GO":
    
    if referenceGame == "Apex Legends":
      print("CS:GO has the same sensitivity as Apex Legends.")
    
    else:
      print("")
    
    print("Your Destiny 2 sensitivity is " + str(float(referenceSensitivity) * float(apexToDestiny)) + "!")
    print("Your COD: Warzone sensitivity is " + str(float(referenceSensitivity) * float(apexToWarzone)) + "!")
    print("Your VALORANT sensitivity is " + str(float(referenceSensitivity) * float(apexToValorant)) + "!")
    print("Your R6S sensitivity is " + str(float(referenceSensitivity) * float(apexToRainbow)) + "!")
    print("Your Overwatch sensitivity is " + str(float(referenceSensitivity) * float(apexToOverwatch)) + "!")
    print("Your Fortnite sensitivty is " + str(float(referenceSensitivity) * float(apexToFortnite)) + "!")

  
  elif referenceGame == "Destiny 2" or referenceGame == "COD: Warzone" or referenceGame == "Overwatch":
    
    if referenceGame == "Destiny 2":
      print("COD: Warzone and Overwatch have the same sensitivity as Destiny 2!")
    
    elif referenceGame == "COD: Warzone":
      print("Your Destiny 2 and Overwatch sensitvity are the same as COD: Warzone!")
    
    else:
      print("")
    
    print("Your Apex Legends sensitivity is " + str(float(referenceSensitivity) * float(destinyToApex)) + "!")
    print("Your CS:GO sensitivity is " + str(float(referenceSensitivity) * float(destinyToCS)) + "!")
    print("Your VALORANT sensitivity is " + str(float(referenceSensitivity) * float(destinyToValorant)) + "!")
    print("Your Fortnite sensitivty is " + str(float(referenceSensitivity) * float(destinyToFortnite)) + "!")
    print("Your R6S sensitivity is " + str(float(referenceSensitivity) * float(destinyToRainbow)) + "!")

  elif referenceGame == "VALORANT":

    print("Your Apex Legends sensitivity is " + str(float(referenceSensitivity) * float(3.181818)) + "!")
    print("Your Destiny 2 sensitivity is " + str(float(referenceSensitivity) * float(10.606061)) + "!")
    print("Your COD: Warzone sensitivity is " + str(float(referenceSensitivity) * float(10.606061)) + "!")
    print("Your CS:GO sensitivity is " + str(float(referenceSensitivity) * float(3.181818)) + "!")
    print("Your R6S sensitivity is " + str(float(referenceSensitivity) * float(12.217305)) + "!")
    print("Your Overwatch sensitivity is " + str(float(referenceSensitivity) * float(10.606061)) + "!")
    print("Your Fortnite sensitivty is " + str(float(referenceSensitivity) * float(12.60126)) + "!")

  elif referenceGame == "Fortnite":
    
    print("Your Apex Legends sensitivity is " + str(float(referenceSensitivity) * float(0.2525)) + "!")
    print("Your Destiny 2 sensitivity is " + str(float(referenceSensitivity) * float(0.841667)) + "!")
    print("Your COD: Warzone sensitivity is " + str(float(referenceSensitivity) * float(0.841667)) + "!")
    print("Your CS:GO sensitivity is " + str(float(referenceSensitivity) * float(0.2525)) + "!")
    print("Your VALORANT sensitivty is " + str(float(referenceSensitivity) * float(0.079357)) + "!")
    print("Your R6S sensitivity is " + str(float(referenceSensitivity) * float(0.96953)) + "!")
    print("Your Overwatch sensitivity is " + str(float(referenceSensitivity) * float(0.841667)) + "!")

  elif referenceGame == "Rainbow 6 Siege":
    
    print("Your Apex Legends sensitivity is " + str(float(referenceSensitivity) * float(0.260435)) + "!")
    print("Your Destiny 2 sensitivity is " + str(float(referenceSensitivity) * float(0.868118)) + "!")
    print("Your COD: Warzone sensitivity is " + str(float(referenceSensitivity) * float(0.868118)) + "!")
    print("Your CS:GO sensitivity is " + str(float(referenceSensitivity) * float(0.260435)) + "!")
    print("Your VALORANT sensitivty is " + str(float(referenceSensitivity) * float(0.081851)) + "!")
    print("Your Overwatch sensitivity is " + str(float(referenceSensitivity) * float(0.868118)) + "!")
    print("Your Fortnite sensitivity is " + str(float(referenceSensitivity) * float(1.031427)) + "!")
  
  else:
    print("Error! Please try again.")

main()