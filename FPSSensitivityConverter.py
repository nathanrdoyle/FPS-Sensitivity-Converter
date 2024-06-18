# Nathan Doyle
# Converts the sensitivity of one FPS game into sensitivities of other FPS games.

def main(): 
    
    gameList = ['Apex Legends', 'Destiny 2', 'COD: Warzone', 'CS:GO', 'VALORANT', 'Rainbow 6 Siege', 'Overwatch', 'Fortnite']
    referenceGame = input("What is the game you are converting your sensitivty from? " + str(gameList) + ": ")
    
    while referenceGame not in gameList:
        print("")
        print("Error! Please try again!")
        print("")
        referenceGame = input("What is the game you are converting your sensitivty from? (Apex Legends, Destiny 2, COD: Warzone, CS:GO, VALORANT, Rainbow 6 Siege, Overwatch, Fortnite)")
    referenceSensitivity = input("What is your sensitivty in " + referenceGame + "? ")

    if referenceGame in gameList:
        conversion(referenceGame, referenceSensitivity)

def conversion(referenceGame, referenceSensitivity):

    if referenceGame == "Apex Legends" or referenceGame == "CS:GO":
        apexLegends(referenceGame, referenceSensitivity)
  
def apexLegends(referenceGame, referenceSensitivity):

    apexConversions = {'Destiny': 3.333333, 'Warzone': 3.333333,'Valorant': 0.314286, 'Rainbow': 3.839724, 'Overwatch': 3.333333, 'Fortnite': 3.960396}

    if referenceGame == "Apex Legends":
        print("CS:GO has the same sensitivity as Apex Legends.")
    
    else:
        print("Apex Legends has the same sensitivity as CS:GO.")
    
    apexToDestiny = float(referenceSensitivity) * float(apexConversions.get('Destiny'))
    apexToWarzone = float(referenceSensitivity) * float(apexConversions.get('Warzone'))
    apexToValorant = float(referenceSensitivity) * float(apexConversions.get('Valorant'))
    apexToRainbow = float(referenceSensitivity) * float(apexConversions.get('Rainbow'))
    apexToOverwatch = float(referenceSensitivity) * float(apexConversions.get('Overwatch'))
    apexToFortnite = float(referenceSensitivity) * float(apexConversions.get('Fortnite'))
    
    print("Your Destiny 2 sensitivity is " + str(apexToDestiny) + "!")
    print("Your COD: Warzone sensitivity is " + str(apexToWarzone) + "!")
    print("Your VALORANT sensitivity is " + str(apexToValorant) + "!")
    print("Your R6S sensitivity is " + str(apexToRainbow) + "!")
    print("Your Overwatch sensitivity is " + str(apexToOverwatch) + "!")
    print("Your Fortnite sensitivty is " + str(apexToFortnite) + "!")

    # destinyToApex = 0.3
    # destinyToCS = 0.3
    # destinyToValorant = 0.094286
    # destinyToFortnite = 1.188119
    # destinyToRainbow = 1.151917

    # valorantToApex = 3.181818
    # valorantToDestiny = 10.606061
    # valorantToWarzone = 10.606061
    # valorantToCS = 3.181818
    # valorantToRainbow = 12.217305
    # valorantToOverwatch = 10.606061
    # valorantToFortnite = 12.60126

    # fortniteToApex = 0.2525
    # fortniteToDestiny = 0.841667
    # fortniteToWarzone = 0.841667
    # fortniteToCS = 0.2525
    # fortniteToValorant = 0.079357
    # fortniteToRainbow = 0.96953
    # fortniteToOverwatch = 0.841667

    # rainbowToApex = 0.260435
    # rainbowToDestiny = 0.868118
    # rainbowToWarzone = 0.868118
    # rainbowToCS = 0.260435
    # rainbowToValorant = 0.081851
    # rainbowToOverwatch = 0.868118
    # rainbowToFortnite = 1.031427

    # if referenceGame == "Apex Legends" or referenceGame == "CS:GO":
        
    #     if referenceGame == "Apex Legends":
    #     print("CS:GO has the same sensitivity as Apex Legends.")
        
    #     else:
    #     print("")
        
    #     print("Your Destiny 2 sensitivity is " + str(float(referenceSensitivity) * float(apexToDestiny)) + "!")
    #     print("Your COD: Warzone sensitivity is " + str(float(referenceSensitivity) * float(apexToWarzone)) + "!")
    #     print("Your VALORANT sensitivity is " + str(float(referenceSensitivity) * float(apexToValorant)) + "!")
    #     print("Your R6S sensitivity is " + str(float(referenceSensitivity) * float(apexToRainbow)) + "!")
    #     print("Your Overwatch sensitivity is " + str(float(referenceSensitivity) * float(apexToOverwatch)) + "!")
    #     print("Your Fortnite sensitivty is " + str(float(referenceSensitivity) * float(apexToFortnite)) + "!")

    
    # elif referenceGame == "Destiny 2" or referenceGame == "COD: Warzone" or referenceGame == "Overwatch":
        
    #     if referenceGame == "Destiny 2":
    #     print("COD: Warzone and Overwatch have the same sensitivity as Destiny 2!")
        
    #     elif referenceGame == "COD: Warzone":
    #     print("Your Destiny 2 and Overwatch sensitvity are the same as COD: Warzone!")
        
    #     else:
    #     print("")
        
    #     print("Your Apex Legends sensitivity is " + str(float(referenceSensitivity) * float(destinyToApex)) + "!")
    #     print("Your CS:GO sensitivity is " + str(float(referenceSensitivity) * float(destinyToCS)) + "!")
    #     print("Your VALORANT sensitivity is " + str(float(referenceSensitivity) * float(destinyToValorant)) + "!")
    #     print("Your Fortnite sensitivty is " + str(float(referenceSensitivity) * float(destinyToFortnite)) + "!")
    #     print("Your R6S sensitivity is " + str(float(referenceSensitivity) * float(destinyToRainbow)) + "!")

    # elif referenceGame == "VALORANT":

    #     print("Your Apex Legends sensitivity is " + str(float(referenceSensitivity) * float(valorantToApex)) + "!")
    #     print("Your Destiny 2 sensitivity is " + str(float(referenceSensitivity) * float(valorantToDestiny)) + "!")
    #     print("Your COD: Warzone sensitivity is " + str(float(referenceSensitivity) * float(valorantToWarzone)) + "!")
    #     print("Your CS:GO sensitivity is " + str(float(referenceSensitivity) * float(valorantToCS)) + "!")
    #     print("Your R6S sensitivity is " + str(float(referenceSensitivity) * float(valorantToRainbow)) + "!")
    #     print("Your Overwatch sensitivity is " + str(float(referenceSensitivity) * float(valorantToOverwatch)) + "!")
    #     print("Your Fortnite sensitivty is " + str(float(referenceSensitivity) * float(valorantToFortnite)) + "!")

    # elif referenceGame == "Fortnite":
        
    #     print("Your Apex Legends sensitivity is " + str(float(referenceSensitivity) * float(fortniteToApex)) + "!")
    #     print("Your Destiny 2 sensitivity is " + str(float(referenceSensitivity) * float(fortniteToDestiny)) + "!")
    #     print("Your COD: Warzone sensitivity is " + str(float(referenceSensitivity) * float(fortniteToWarzone)) + "!")
    #     print("Your CS:GO sensitivity is " + str(float(referenceSensitivity) * float(fortniteToCS)) + "!")
    #     print("Your VALORANT sensitivty is " + str(float(referenceSensitivity) * float(fortniteToValorant)) + "!")
    #     print("Your R6S sensitivity is " + str(float(referenceSensitivity) * float(fortniteToRainbow)) + "!")
    #     print("Your Overwatch sensitivity is " + str(float(referenceSensitivity) * float(fortniteToOverwatch)) + "!")

    # elif referenceGame == "Rainbow 6 Siege":
        
    #     print("Your Apex Legends sensitivity is " + str(float(referenceSensitivity) * float(rainbowToApex)) + "!")
    #     print("Your Destiny 2 sensitivity is " + str(float(referenceSensitivity) * float(rainbowToDestiny)) + "!")
    #     print("Your COD: Warzone sensitivity is " + str(float(referenceSensitivity) * float(rainbowToWarzone)) + "!")
    #     print("Your CS:GO sensitivity is " + str(float(referenceSensitivity) * float(rainbowToCS)) + "!")
    #     print("Your VALORANT sensitivty is " + str(float(referenceSensitivity) * float(rainbowToValorant)) + "!")
    #     print("Your Overwatch sensitivity is " + str(float(referenceSensitivity) * float(rainbowToOverwatch)) + "!")
    #     print("Your Fortnite sensitivity is " + str(float(referenceSensitivity) * float(rainbowToFortnite)) + "!")
    
    # else:
    #     print("Error! Please try again.")

main()
