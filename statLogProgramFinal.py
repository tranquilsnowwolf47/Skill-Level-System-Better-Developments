# Filename: statLogProgramFinal.py
# Date: 12/16/24 
# Author: Akira | oathkeeperthefoolxiii

# Purpose:
# Used to keep track of stat logging per day

# Psuedocode:
# Make a function for each skill category | done
# have constant ints for good, great, and perfect values
# ASk for the date | good
# Ask the user if they got an increase in <skill category name>
# if yes, ask if it was a good, great, and perfect
# Keep track of user inputs and then output the result of the logging


# Function that gets the date from the user
def getDate():
    month = int(input("Please enter the month: "))
    day = int(input("Please enter the day: "))
    year = int(input("Please enter the year: ")) 

    return month, day, year

hasIncrease = False # Global flag to determine if an increase was gained 
validResult = False # Global flag to determine if a valid choice was chosen


# Template
#def logExampleIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    #increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    #if increaseChoice == "y":
        #hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        #resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        #validChoices = ["good","great","perfect"]
        # validate input
        #if resultChoice in validChoices:
            #validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            #if resultChoice == "good":
                #print(f"Today's {skillLevelCategory} result: ")
                #print("---------------------------------------------------")
                #print(f"Skill Level Category: {skillLevelCategory}")
                #print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            #elif resultChoice == "great":
                #print(f"Today's {skillLevelCategory} result: ")
                #print("---------------------------------------------------")
                #print(f"Skill Level Category: {skillLevelCategory}")
                #print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            #elif resultChoice == "perfect":
                #print(f"Today's {skillLevelCategory} result: ")
                #print("---------------------------------------------------")
                #print(f"Skill Level Category: {skillLevelCategory}")
                #print(f"EXP obtained today: {PERFECT_EXP} ") 
            #else:
                #print("Valid result is: ",validResult) # Debugging, should be false
    #else:
        #print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        #print("-------------------------------------------------------------------------")  

    
    # Call function
    # Category name, good exp value, great exp value, perfect exp value
#logExampleIncreases("Walls",22,32,64)




# Functions
# -----------------------------------------------------------------------------------------
# Get and display results for Sword 
def logSwordIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  



# Get and display results for Lance
def logLanceIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  



# Get and display results for Axe
def logAxeIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  

    

# Get and display results for Bow
def logBowIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  



# Get and display results for Brawl 
def logBrawlIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  



# Get and display results for Reason
def logReasonIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  


    
# Get and display results for Faith
def logFaithIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  



# Get and display results for Authority    
def logAuthorityIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  

    

# Get and display results for Heavy Armor
def logHvyArmorIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  



# Get and display results for Riding
def logRidingIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")  



# Get and display results for Flying
def logFlyingIncreases(skillLevelCategory,GOOD_EXP,GREAT_EXP,PERFECT_EXP): # potential arguments: goodEXP, greatEXP, perfectEXP
    # Ask the user for if they got any skill category increases at all in the day for this category or not
    increaseChoice = str(input(f"Did you get any increases in {skillLevelCategory} today? Enter y for yes, n for no: ")).lower()
    # If the answer is y, then proceed, else, end
    if increaseChoice == "y":
        hasIncrease = True # Set the flag to true for a valid input
        # print("hasIncrease: ",hasIncrease) # For debugging 
        # Proceed with operations if an increase obtained in the day

        
        # Prompt the user if they got a good, great or perfect result
        resultChoice = input(f"Did you get a good, great, or perfect in {skillLevelCategory} today? Enter good for good, great for great, or perfect for perfect: ").lower()
        validChoices = ["good","great","perfect"]
        # validate input
        if resultChoice in validChoices:
            validResult = True 
            #print("Valid result is: ",validResult) # Debugging, should be true 
            # print("(Proceed with program here)") | # Debugging, proceed 
            
            # Ops for good
            if resultChoice == "good":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GOOD_EXP} ") 
            # Ops for great
            elif resultChoice == "great":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {GREAT_EXP} ") 
            # Ops for perfect
            elif resultChoice == "perfect":
                print(f"Today's {skillLevelCategory} result: ")
                print("---------------------------------------------------")
                print(f"Skill Level Category: {skillLevelCategory}")
                print(f"EXP obtained today: {PERFECT_EXP} ") 
            else:
                print("Valid result is: ",validResult) # Debugging, should be false
    else:
        print(f"You didn't get an increase in the {skillLevelCategory} category today. ")
        print("-------------------------------------------------------------------------")            

# Function that displays the date 
def displayDate(month, day, year):
    print()
    print(f"The date is: {month}/{day}/{year} ")


# Debug test function that calls all increase functions
#def callAllIncreases():
    #swordResult = logSwordIncreases("Sword",22,32,64)
    #print()
    #lanceResult = logLanceIncreases("Lance",22,32,64)
    #print()
    #axeResult = logAxeIncreases("Axe",22,32,64)
    #print()
    #bowResult = logBowIncreases("Bow",22,32,64)
    #print()
    #brawlResult = logBrawlIncreases("Brawl",22,32,64)
    #print()
    #reasonResult = logReasonIncreases("Reason",22,32,64)
    #print()
    #faithResult = logFaithIncreases("Faith",22,32,64)
    #print()
    #authorityResult = logAuthorityIncreases("Authority",22,32,64)
    #print()
    #hvyArmorResult = logHvyArmorIncreases("Heavy Armor",22,32,64)
    #print()
    #ridingResult = logRidingIncreases("Riding",22,32,64)
    #print()
    #flyingResult = logFlyingIncreases("Flying",22,32,64)
    #return swordResult, lanceResult, axeResult, bowResult, brawlResult, reasonResult, faithResult, authorityResult, hvyArmorResult, ridingResult, flyingResult

#callAllIncreases()



# Function that calls all functions
def allFunctions():
    month,day,year = getDate()
    swordResult = logSwordIncreases("Sword",22,32,64)
    print()
    lanceResult = logLanceIncreases("Lance",22,32,64)
    print()
    axeResult = logAxeIncreases("Axe",22,32,64)
    print()
    bowResult = logBowIncreases("Bow",22,32,64)
    print()
    brawlResult = logBrawlIncreases("Brawl",22,32,64)
    print()
    reasonResult = logReasonIncreases("Reason",22,32,64)
    print()
    faithResult = logFaithIncreases("Faith",22,32,64)
    print()
    authorityResult = logAuthorityIncreases("Authority",22,32,64)
    print()
    hvyArmorResult = logHvyArmorIncreases("Heavy Armor",22,32,64)
    print()
    ridingResult = logRidingIncreases("Riding",22,32,64)
    print()
    flyingResult = logFlyingIncreases("Flying",22,32,64)
    displayDate(month,day,year)
    return swordResult, lanceResult, axeResult, bowResult, brawlResult, reasonResult, faithResult, authorityResult, hvyArmorResult, ridingResult, flyingResult
    

# Call the function
allFunctions()


