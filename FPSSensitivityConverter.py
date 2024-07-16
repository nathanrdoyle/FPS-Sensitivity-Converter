# Nathan Doyle
# Converts the sensitivity of one FPS game into sensitivities of other FPS games.

def main(): 
    
    gameList = ['Apex Legends', 'Destiny 2', 'COD: Warzone', 'CS:GO', 'VALORANT', 'Rainbow 6 Siege', 'Overwatch', 'Fortnite']
    print("")
    referenceGame = input("What is the game you are converting your sensitivty from? " + str(gameList) + ": ")
    
    while referenceGame not in gameList:
        print("")
        print("Error! Please try again!")
        print("")
        referenceGame = input("What is the game you are converting your sensitivty from? (Apex Legends, Destiny 2, COD: Warzone, CS:GO, VALORANT, Rainbow 6 Siege, Overwatch, Fortnite)")
    print("")
    referenceSensitivity = input("What is your sensitivty in " + referenceGame + "? ")

    if referenceGame in gameList:
        conversion(referenceGame, referenceSensitivity)

def conversion(referenceGame, referenceSensitivity):

    if referenceGame == "Apex Legends" or referenceGame == "CS:GO":
        apexLegendsConversions(referenceGame, referenceSensitivity)
    
    elif referenceGame == "Destiny 2" or referenceGame == "COD: Warzone" or referenceGame == "Overwatch":
        destinyConversions(referenceGame, referenceSensitivity)
    
    elif referenceGame == "VALORANT":
        valorantConversions(referenceGame, referenceSensitivity)
  
    elif referenceGame == "Fortnite":
        fortniteConversions(referenceGame, referenceSensitivity)

    elif referenceGame == "Rainbow 6 Siege":
        rainbowConversions(referenceGame, referenceSensitivity)

def apexLegendsConversions(referenceGame, referenceSensitivity):

    apexConversionFactors = {'Destiny': 3.333333, 'Warzone': 3.333333,'Valorant': 0.314286, 'Rainbow': 3.839724, 'Overwatch': 3.333333, 'Fortnite': 3.960396}

    if referenceGame == "Apex Legends":
        print("CS:GO has the same sensitivity as Apex Legends.")
    
    else:
        print("Apex Legends has the same sensitivity as CS:GO.")
    
    print("")

    apexToDestinyConversion = float(referenceSensitivity) * float(apexConversionFactors.get('Destiny'))
    apexToWarzoneConversion = float(referenceSensitivity) * float(apexConversionFactors.get('Warzone'))
    apexToValorantConversion = float(referenceSensitivity) * float(apexConversionFactors.get('Valorant'))
    apexToRainbowConversion = float(referenceSensitivity) * float(apexConversionFactors.get('Rainbow'))
    apexToOverwatchConversion = float(referenceSensitivity) * float(apexConversionFactors.get('Overwatch'))
    apexToFortniteConversion = float(referenceSensitivity) * float(apexConversionFactors.get('Fortnite'))
    
    print("Your Destiny 2 sensitivity is " + str(apexToDestinyConversion) + "!")
    print("Your COD: Warzone sensitivity is " + str(apexToWarzoneConversion) + "!")
    print("Your VALORANT sensitivity is " + str(apexToValorantConversion) + "!")
    print("Your R6S sensitivity is " + str(apexToRainbowConversion) + "!")
    print("Your Overwatch sensitivity is " + str(apexToOverwatchConversion) + "!")
    print("Your Fortnite sensitivty is " + str(apexToFortniteConversion) + "!")

def destinyConversions(referenceGame, referenceSensitivity):
                    
    destinyConversionFactors = {'Apex Legends': 0.3, 'CS': 0.3, 'Valorant': 0.094286, 'Fortnite': 1.188119, 'Rainbow': 1.151917}
                        
    if referenceGame == "Destiny 2":
        print("COD: Warzone and Overwatch have the same sensitivity as Destiny 2!")
                        
    elif referenceGame == "COD: Warzone":
        print("Your Destiny 2 and Overwatch sensitvity are the same as COD: Warzone!")
                        
    else:
        print("")

    destinyToApexConversion = float(referenceSensitivity) * float(destinyConversionFactors.get('Apex Legends'))     
    destinyToCSConversion = float(referenceSensitivity) * float(destinyConversionFactors.get('CS'))
    destinyToValorantConversion = float(referenceSensitivity) * float(destinyConversionFactors.get('Valorant'))
    destinyToFortniteConversion = float(referenceSensitivity) * float(destinyConversionFactors.get('Fortnite'))
    destinyToRainbowConversion = float(referenceSensitivity) * float(destinyConversionFactors.get('Rainbow'))
    
    print("Your Apex Legends sensitivity is " + str(destinyToApexConversion) + "!")
    print("Your CS:GO sensitivity is " + str(destinyToCSConversion) + "!")
    print("Your VALORANT sensitivity is " + str(destinyToValorantConversion) + "!")
    print("Your Fortnite sensitivty is " + str(destinyToFortniteConversion) + "!")
    print("Your R6S sensitivity is " + str(destinyToRainbowConversion) + "!")
      
def valorantConversions(referenceGame, referenceSensitivity):
    
    valorantConversionFactors = {'Apex Legends': 3.181818, 'Destiny': 10.606061, 'Warzone': 10.606061, 'CS': 3.181818, 'Rainbow': 12.217305, 'Overwatch': 10.606061, 'Fortnite': 12.60126}

    valorantToApexConversion = float(referenceSensitivity) * float(valorantConversionFactors.get('Apex Legends'))
    valorantToDestinyConversion = float(referenceSensitivity) * float(valorantConversionFactors.get('Destiny'))
    valorantToWarzoneConversion = float(referenceSensitivity) * float(valorantConversionFactors.get('Warzone'))
    valorantToCSConversion = float(referenceSensitivity) * float(valorantConversionFactors.get('CS'))
    valorantToRainbowConversion = float(referenceSensitivity) * float(valorantConversionFactors.get('Rainbow'))
    valorantToOverwatchConversion = float(referenceSensitivity) * float(valorantConversionFactors.get('Overwatch'))
    valorantToFortniteConversion = float(referenceSensitivity) * float(valorantConversionFactors.get('Fortnite'))

    print("Your Apex Legends sensitivity is " + str(valorantToApexConversion) + "!")
    print("Your Destiny 2 sensitivity is " + str(valorantToDestinyConversion) + "!")
    print("Your COD: Warzone sensitivity is " + str(valorantToWarzoneConversion) + "!")
    print("Your CS:GO sensitivity is " + str(valorantToCSConversion) + "!")
    print("Your R6S sensitivity is " + str(valorantToRainbowConversion) + "!")
    print("Your Overwatch sensitivity is " + str(valorantToOverwatchConversion) + "!")
    print("Your Fortnite sensitivty is " + str(valorantToFortniteConversion) + "!")

def fortniteConversions(referenceGame, referenceSensitivity):
    
    fortniteConversionFactors = {'Apex Legends': 0.2525, 'Destiny': 0.841667, 'Warzone': 0.841667, 'CS': 0.2525, 'Valorant': 0.079357, 'Rainbow': 0.96953, 'Overwatch': 0.841667}    
    
    fortniteToApexConversion = float(referenceSensitivity) * float(fortniteConversionFactors.get('Apex Legends'))
    fortniteToDestinyConversion = float(referenceSensitivity) * float(fortniteConversionFactors.get('Destiny'))
    fortniteToWarzoneConversion = float(referenceSensitivity) * float(fortniteConversionFactors.get('Warzone'))
    fortniteToCSConversion = float(referenceSensitivity) * float(fortniteConversionFactors.get('CS'))
    fortniteToValorantConversion = float(referenceSensitivity) * float(fortniteConversionFactors.get('Valorant'))
    fortniteToRainbowConversion = float(referenceSensitivity) * float(fortniteConversionFactors.get('Rainbow'))
    fortniteToOverwatchConversion = float(referenceSensitivity) * float(fortniteConversionFactors.get('Overwatch'))

    print("Your Apex Legends sensitivity is " + str(fortniteToApexConversion) + "!")
    print("Your Destiny 2 sensitivity is " + str(fortniteToDestinyConversion) + "!")
    print("Your COD: Warzone sensitivity is " + str(fortniteToWarzoneConversion) + "!")
    print("Your CS:GO sensitivity is " + str(fortniteToCSConversion) + "!")
    print("Your VALORANT sensitivty is " + str(fortniteToValorantConversion) + "!")
    print("Your R6S sensitivity is " + str(fortniteToRainbowConversion) + "!")
    print("Your Overwatch sensitivity is " + str(fortniteToOverwatchConversion) + "!")

def rainbowConversions(referenceGame, referenceSensitivity):

    rainbowConversionFactors = {'Apex Legends': 0.260435, 'Destiny': 0.868118, 'Warzone': 0.868118, 'CS': 0.260435, 'Valorant': 0.081851, 'Overwatch': 0.868118, 'Fortnite': 1.031427}

    rainbowToApexConversion = float(referenceSensitivity) * float(rainbowConversionFactors.get('Apex Legends'))
    rainbowToDestinyConversion = float(referenceSensitivity) * float(rainbowConversionFactors.get('Destiny'))
    rainbowToWarzoneConversion = float(referenceSensitivity) * float(rainbowConversionFactors.get('Warzone'))
    rainbowToCSConversion = float(referenceSensitivity) * float(rainbowConversionFactors.get('CS'))
    rainbowToValorantConversion = float(referenceSensitivity) * float(rainbowConversionFactors.get('Valorant'))
    rainbowToOverwatchConversion = float(referenceSensitivity) * float(rainbowConversionFactors.get('Overwatch'))
    rainbowToFortniteConversion = float(referenceSensitivity) * float(rainbowConversionFactors.get('Fortnite'))

    print("Your Apex Legends sensitivity is " + str(rainbowToApexConversion) + "!")
    print("Your Destiny 2 sensitivity is " + str(rainbowToDestinyConversion) + "!")
    print("Your COD: Warzone sensitivity is " + str(rainbowToWarzoneConversion) + "!")
    print("Your CS:GO sensitivity is " + str(rainbowToCSConversion) + "!")
    print("Your VALORANT sensitivty is " + str(rainbowToValorantConversion) + "!")
    print("Your Overwatch sensitivity is " + str(rainbowToOverwatchConversion) + "!")
    print("Your Fortnite sensitivity is " + str(rainbowToFortniteConversion) + "!")


main()