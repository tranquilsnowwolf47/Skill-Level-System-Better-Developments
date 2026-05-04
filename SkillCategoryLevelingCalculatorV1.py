# Filename: SkillCategoryLevelingCalculatorV1.py
# Date: 5/3/26
# Author: Aoi | shadowsnowwolf
# Processing:

# Strategtic planning:
# 1. Define the EXP requirements for each letter | Done!
# 2. 


# I'll likely need OOP. I'll need to define each skill category
# Sword, Lance, Axe, Bow, Brawl, Reason, Faith, Authority, Heavy Armor, Riding, FLying
#  I'll definitely need functions that return the data so I can run it through a function again


# I might just need class methods instead of whole objects because the program should be more 
# method-heavy than object and attribute heavy


#
#
#
#
#


# Letter grade requirements:
# E_PLUS_EXP_REQUIREMENT = 40
# D_EXP_REQUIREMENT = 60
# D_PLUS_EXP_REQUIREMENT = 80
# C_EXP_REQUIREMENT = 120
# C_PLUS_EXP_REQUIREMENT = 160
# B_EXP_REQUIREMENT = 220
# B_PLUS_EXP_REQUIREMENT = 280
# A_EXP_REQUIREMENT = 360
# A_PLUS_EXP_REQUIREMENT = 440
# S_EXP_REQUIREMENT = 540
# S_PLUS_EXP_REQUIREMENT = 760
# MAX_EXP_REQUIREMENT = 900

letter_grades = ("E","E+","D","D+","C","C+","B","B+","A","A+","S","S+","MAX")


# I also may not need OOP. I could probably uses tuples and dictionaries
# For the argument, I set that to the user's EXP. Which is why returning is gonna be important 

class Calculator:
    def __init__(self, exp):
        pass

    E_PLUS_EXP_REQUIREMENT = 40
    D_EXP_REQUIREMENT = 60
    C_EXP_REQUIREMENT = 120
    C_PLUS_EXP_REQUIREMENT = 160
    B_EXP_REQUIREMENT = 220
    B_PLUS_EXP_REQUIREMENT = 280
    A_EXP_REQUIREMENT = 360
    A_PLUS_EXP_REQUIREMENT = 440
    S_EXP_REQUIREMENT = 540
    S_PLUS_EXP_REQUIREMENT = 760
    MAX_EXP_REQUIREMENT = 900

# Note: 
# There's gonna be a different number for each Skill Category so keep that in mind
# Debug one first


dummy_EXP = 200
level_up = False

# x is a temproary placeholder for the dummy EXP variable
# Fix that later 



# Debugged 
def calculate_E_plus(x, E_PLUS_EXP_REQUIREMENT=40):
    # Requirement for promotion to letter: 40 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E)
    current_letter = letter_grades[0]
    
    # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
    new_letter = letter_grades[1] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= E_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= E_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = E_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {E_PLUS_EXP_REQUIREMENT}")

# Debugged  
def calculate_D(x, D_EXP_REQUIREMENT=60):
    # Requirement for promotion to letter: 60 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E+)
    current_letter = letter_grades[1]
    
    # Sets the upgraded letter to D+ from the tuple granted the user leveled up 
    new_letter = letter_grades[2] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= D_EXP_REQUIREMENT:
        # Perform the calculation
        x -= D_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = D_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {D_EXP_REQUIREMENT}")


# Debugged
def calculate_D_plus(x, D_PLUS_EXP_REQUIREMENT=80):
    # Requirement for promotion to letter: 80 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (D)
    current_letter = letter_grades[2]
    
    # Sets the upgraded letter to D+ from the tuple granted the user leveled up 
    new_letter = letter_grades[3] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= D_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= D_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = D_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter..")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {D_PLUS_EXP_REQUIREMENT}")


# Debugged
def calculate_C(x, C_EXP_REQUIREMENT=120):
    # Requirement for promotion to letter: 120 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (D+)
    current_letter = letter_grades[3]
    
    # Sets the upgraded letter to C from the tuple granted the user leveled up 
    new_letter = letter_grades[4] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= C_EXP_REQUIREMENT:
        # Perform the calculation
        x -= C_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = C_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {C_EXP_REQUIREMENT}")

# Current
def calculate_C_plus(x, C_PLUS_EXP_REQUIREMENT=160):
    # Requirement for promotion to letter: 160 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E)
    current_letter = letter_grades[0]
    
    # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
    new_letter = letter_grades[1] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= E_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= E_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = E_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {E_PLUS_EXP_REQUIREMENT}")

def calculate_B(x, B_EXP_REQUIREMENT=220):
    # Requirement for promotion to letter: 220 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E)
    current_letter = letter_grades[0]
    
    # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
    new_letter = letter_grades[1] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= E_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= E_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = E_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {E_PLUS_EXP_REQUIREMENT}")

def calculate_B_plus(x, B_PLUS_EXP_REQUIREMENT=280):
    # Requirement for promotion to letter: 280 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E)
    current_letter = letter_grades[0]
    
    # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
    new_letter = letter_grades[1] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= E_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= E_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = E_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {E_PLUS_EXP_REQUIREMENT}")

def calculate_A(x, A_EXP_REQUIREMENT=360):
    # Requirement for promotion to letter: 360 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E)
    current_letter = letter_grades[0]
    
    # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
    new_letter = letter_grades[1] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= E_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= E_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = E_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {E_PLUS_EXP_REQUIREMENT}")

def calculate_A_plus(x, A_PLUS_EXP_REQUIREMENT=440):
    # Requirement for promotion to letter: 440 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E)
    current_letter = letter_grades[0]
    
    # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
    new_letter = letter_grades[1] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= E_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= E_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = E_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {E_PLUS_EXP_REQUIREMENT}")

def calculate_S(x, S_EXP_REQUIREMENT=540):
    # Requirement for promotion to letter: 540 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E)
    current_letter = letter_grades[0]
    
    # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
    new_letter = letter_grades[1] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= E_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= E_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = E_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {E_PLUS_EXP_REQUIREMENT}")

def calculate_S_plus(x, S_PLUS_EXP_REQUIREMENT=760):
    # Requirement for promotion to letter: 760 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E)
    current_letter = letter_grades[0]
    
    # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
    new_letter = letter_grades[1] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= E_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= E_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = E_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {E_PLUS_EXP_REQUIREMENT}")

def calculate_MAX(x, MAX_EXP_REQUIREMENT=900):
    # Requirement for promotion to letter: 900 EXP
    # Subtracts the user's total EXP points from the requirement
    # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
    
    # Sets the current letter, granted the user didn't level up by default from the tuple (E)
    current_letter = letter_grades[0]
    
    # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
    new_letter = letter_grades[1] 

    # Test for decision branches
    # If the user leveled up, decrement the EXP and upgrade their letter grade
    if x >= E_PLUS_EXP_REQUIREMENT:
        # Perform the calculation
        x -= E_PLUS_EXP_REQUIREMENT
        level_up = True

        # Output the new info to them  
        print("You leveled up!")
        print(f"New letter: {new_letter}")
        print(f"Remainder EXP: {x}")

        # Return the new letter and the remainder EXP to modify later
        return new_letter, x
    
    # If the user doesn't level up, just enter the EXP to next subtracted from their input
    else:
        # Calculates the deduction requirement for the next letter desired
        EXP_to_next = E_PLUS_EXP_REQUIREMENT - x

        # Let the uer know that they didn't reach the EXP requirement 
        print("You do not have enough EXP to reach the next letter.")
        print(f"Current letter: {current_letter}")
        # Let's the user know how much EXP they need from the current deduction to get to the next rank
        print(f"EXP to next: {EXP_to_next}")
        print("----------------------------------------------------------")
        print(f"\nEXP required for {new_letter}: {E_PLUS_EXP_REQUIREMENT}")


# Get the user's input
# calculate based on user's input

calculations = ()
for calculation in calculations:
    pass




class Sword(Calculator):
    def __init__(self,exp,dog):
        pass




#sword_EXP = 0
