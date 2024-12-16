# Filename: EXPAccmulationCalculatorFinal.py
# Date: 11/20/24
# Author: Akira | oathkeeperthefoolxiii

# V2 of goodGreat calculator with implentation of arguments 


# Updates:
# The former variable good_EXPResult has been renamed to goodResult for more conciseness and simplicity
# The former variable good_EXPResult has been renamed to greatResult for more conciseness and simplicity
# The former variable total_EXPResult has been renamed to totalResult for more conciseness and simplicity


def displayIntroductionInfo():
   # Provide a detailed explanation on what the program does using print statements
   print("Welcome to the EXP Accumulation Calculator!")
   print("The purpose of this program is to calculate the amount of EXP that the user has gained and display those calculations to them for self improvement purposes! ")
   print("You will be given a series of prompts that will ask you to input certain types of data. Please comply and you'll get your final calculation!")
   print()
   print()

def getDate():
    
    month = int(input("Please enter the month (in number format): "))
    day = int(input("Please enter the day: "))
    year = int(input("Please enter the year: "))
    print()
    print()
    
    return month, day, year 

# Sword:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatSword(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)
    


# Lance:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatLance(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)



# Axe:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatAxe(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)



# Bow:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatBow(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)



# Brawl:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatBrawl(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)



# Reason:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatReason(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)



# Faith:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatFaith(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)



# Authority:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatAuthority(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)



# Hvy Armor:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatHvyArmor(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)
    


# Riding:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatRiding(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)



# Flying:
# -------------------------------------------------------------------------------------------
def calculateGoodGreatFlying(skillCategoryName, GOOD_EXP, GREAT_EXP):
    # Get the number of good results from the user
    goodInput = int(input("Please enter how many good results you got. ")) 
    
    # Get the nuber of great results from the user
    greatInput = int(input("Please enter how many great results you got. "))    

    # Calculations
    goodResult = GOOD_EXP * goodInput
    greatResult = GREAT_EXP * greatInput
    totalResult = goodResult + greatResult

    # Final output:
    print("\n")
    print(f"Skill Category: {skillCategoryName}")
    print("-------------------------------------------------------------")
    print(f"The total number of EXP accumulated for this weapon is: {totalResult}")
    print("The total amount of good EXP is:",goodResult)
    print("The total amount of great EXP is:",greatResult)
    
def displayDate(year,month,day):
    print(f"The date is: {month}/{day}/{year}.")

# Function calls
# ------------------------------------------------------------------------------------------------
def displayAllCalculations():   # Function that calls all functions
    displayIntroductionInfo()
    month,day,year = getDate()
    calculateGoodGreatSword("Sword",22,32) 
    print("\n")
    calculateGoodGreatLance("Lance",22,32)
    print("\n")
    calculateGoodGreatAxe("Axe",22,32)
    print("\n")
    calculateGoodGreatBow("Bow",22,32)
    print("\n")
    calculateGoodGreatBrawl("Brawl",22,32)
    print("\n")
    calculateGoodGreatReason("Reason",22,32)
    print("\n")
    calculateGoodGreatFaith("Faith",22,32)
    print("\n")
    calculateGoodGreatAuthority("Authority",22,32)
    print("\n")
    calculateGoodGreatHvyArmor("Hvy Armor",22,32)
    print("\n")
    calculateGoodGreatRiding("Riding",22,32)
    print("\n")
    calculateGoodGreatFlying("Flying",22,32)
    print("\n")
    displayDate(year,month,day)

displayAllCalculations()