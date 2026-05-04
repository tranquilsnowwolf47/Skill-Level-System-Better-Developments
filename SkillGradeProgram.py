# Filename: SkillCategoryLevelingCalculatorV1.py
# Date: 5/3/26
# Author: Aoi | shadowsnowwolf
# Processing:

# Strategtic planning:
# 1. Define the EXP requirements for each letter | Done!
# 2. Create functions that calculate to each letter | Done


# I may need OOP. I'll need to define each skill category
# Sword, Lance, Axe, Bow, Brawl, Reason, Faith, Authority, Heavy Armor, Riding, FLying
#  I'll definitely need functions that return the data so I can run it through a function again

# I might just need class methods instead of whole objects because the program should be more 
# method-heavy than object and attribute heavy

#
#
#
#
#

# x is a temproary placeholder for the dummy EXP variable
# Fix that later 

# I also may not need OOP. I could probably uses tuples and dictionaries
# For the argument, I set that to the user's EXP. Which is why returning is gonna be important 

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

# Note: 
# There's gonna be a different user EXP number for each Skill Category so keep that in mind
# Debug one first




class GradeCalculator:
    def __init__(self, skill_category):
        self.skill_category = skill_category

    # Tuple that holds all skill categories 
    skill_categories = ("Sword (Essentials)","Lance (The Arts)","Axe (Technical and Technological)","Bow (Intelligence and Education)","Brawl (Combat)",
                    "Reason (Mind and Spirit)","Faith (Piety and Spirituality)","Authority (Charisma and Leadership)","Heavy Armor (Grit and Guts)",
                    "Riding (Fitness and Extracurricular)","Flying (Organizational)")

    # Tuple that holds all letter grade categories 
    letter_grades = ("E","E+","D","D+","C","C+","B","B+","A","A+","S","S+","MAX")

    level_up = False

    # Debugged 
    # Performs calculations to E+
    def calculate_to_E_plus(x=0, E_PLUS_EXP_REQUIREMENT=40):
        # Requirement for promotion to letter: 40 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (E)
        current_letter = GradeCalculator.letter_grades[0]
        
        # Sets the upgraded letter to E+ from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[1] 

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
    def calculate_to_D(x=0, D_EXP_REQUIREMENT=60):
        # Requirement for promotion to letter: 60 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (E+)
        current_letter = GradeCalculator.letter_grades[1]
        
        # Sets the upgraded letter to D+ from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[2] 

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
    def calculate_to_D_plus(x=0, D_PLUS_EXP_REQUIREMENT=80):
        # Requirement for promotion to letter: 80 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (D)
        current_letter = GradeCalculator.letter_grades[2]
        
        # Sets the upgraded letter to D+ from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[3] 

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
    def calculate_to_C(x=0, C_EXP_REQUIREMENT=120):
        # Requirement for promotion to letter: 120 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (D+)
        current_letter = GradeCalculator.letter_grades[3]
        
        # Sets the upgraded letter to C from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[4] 

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

    # Debugged
    def calculate_to_C_plus(x=0, C_PLUS_EXP_REQUIREMENT=160):
        # Requirement for promotion to letter: 160 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current lettesr, granted the user didn't level up by default from the tuple (C)
        current_letter = GradeCalculator.letter_grades[4]
        
        # Sets the upgraded letter to C+ from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[5] 

        # Test for decision branches
        # If the user leveled up, decrement the EXP and upgrade their letter grade
        if x >= C_PLUS_EXP_REQUIREMENT:
            # Perform the calculation
            x -= C_PLUS_EXP_REQUIREMENT
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
            EXP_to_next = C_PLUS_EXP_REQUIREMENT - x

            # Let the uer know that they didn't reach the EXP requirement 
            print("You do not have enough EXP to reach the next letter.")
            print(f"Current letter: {current_letter}")
            # Let's the user know how much EXP they need from the current deduction to get to the next rank
            print(f"EXP to next: {EXP_to_next}")
            print("----------------------------------------------------------")
            print(f"\nEXP required for {new_letter}: {C_PLUS_EXP_REQUIREMENT}")

    # Debugged
    def calculate_to_B(x=0, B_EXP_REQUIREMENT=220):
        # Requirement for promotion to letter: 220 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (C+)
        current_letter = GradeCalculator.letter_grades[5]
        
        # Sets the upgraded letter to B from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[6] 

        # Test for decision branches
        # If the user leveled up, decrement the EXP and upgrade their letter grade
        if x >= B_EXP_REQUIREMENT:
            # Perform the calculation
            x -= B_EXP_REQUIREMENT
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
            EXP_to_next = B_EXP_REQUIREMENT - x

            # Let the uer know that they didn't reach the EXP requirement 
            print("You do not have enough EXP to reach the next letter.")
            print(f"Current letter: {current_letter}")
            # Let's the user know how much EXP they need from the current deduction to get to the next rank
            print(f"EXP to next: {EXP_to_next}")
            print("----------------------------------------------------------")
            print(f"\nEXP required for {new_letter}: {B_EXP_REQUIREMENT}")

    # Debugged
    def calculate_to_B_plus(x=0, B_PLUS_EXP_REQUIREMENT=280):
        # Requirement for promotion to letter: 280 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (B)
        current_letter = GradeCalculator.letter_grades[6]
        
        # Sets the upgraded letter to B+ from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[7] 

        # Test for decision branches
        # If the user leveled up, decrement the EXP and upgrade their letter grade
        if x >= B_PLUS_EXP_REQUIREMENT:
            # Perform the calculation
            x -= B_PLUS_EXP_REQUIREMENT
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
            EXP_to_next = B_PLUS_EXP_REQUIREMENT - x

            # Let the uer know that they didn't reach the EXP requirement 
            print("You do not have enough EXP to reach the next letter.")
            print(f"Current letter: {current_letter}")
            # Let's the user know how much EXP they need from the current deduction to get to the next rank
            print(f"EXP to next: {EXP_to_next}")
            print("----------------------------------------------------------")
            print(f"\nEXP required for {new_letter}: {B_PLUS_EXP_REQUIREMENT}")

    # Debugged
    def calculate_to_A(x=0, A_EXP_REQUIREMENT=360):
        # Requirement for promotion to letter: 360 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (B+)
        current_letter = GradeCalculator.letter_grades[7]
        
        # Sets the upgraded letter to A from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[8] 

        # Test for decision branches
        # If the user leveled up, decrement the EXP and upgrade their letter grade
        if x >= A_EXP_REQUIREMENT:
            # Perform the calculation
            x -= A_EXP_REQUIREMENT
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
            EXP_to_next = A_EXP_REQUIREMENT - x

            # Let the uer know that they didn't reach the EXP requirement 
            print("You do not have enough EXP to reach the next letter.")
            print(f"Current letter: {current_letter}")
            # Let's the user know how much EXP they need from the current deduction to get to the next rank
            print(f"EXP to next: {EXP_to_next}")
            print("----------------------------------------------------------")
            print(f"\nEXP required for {new_letter}: {A_EXP_REQUIREMENT}")

    # Debugged
    def calculate_to_A_plus(x=0, A_PLUS_EXP_REQUIREMENT=440):
        # Requirement for promotion to letter: 440 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (A)
        current_letter = GradeCalculator.letter_grades[8]
        
        # Sets the upgraded letter to A+ from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[9] 

        # Test for decision branches
        # If the user leveled up, decrement the EXP and upgrade their letter grade
        if x >= A_PLUS_EXP_REQUIREMENT:
            # Perform the calculation
            x -= A_PLUS_EXP_REQUIREMENT
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
            EXP_to_next = A_PLUS_EXP_REQUIREMENT - x

            # Let the uer know that they didn't reach the EXP requirement 
            print("You do not have enough EXP to reach the next letter.")
            print(f"Current letter: {current_letter}")
            # Let's the user know how much EXP they need from the current deduction to get to the next rank
            print(f"EXP to next: {EXP_to_next}")
            print("----------------------------------------------------------")
            print(f"\nEXP required for {new_letter}: {A_PLUS_EXP_REQUIREMENT}")


    # Debugged
    def calculate_to_S(x=0, S_EXP_REQUIREMENT=540):
        # Requirement for promotion to letter: 540 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (A+)
        current_letter = GradeCalculator.letter_grades[9]
        
        # Sets the upgraded letter to S from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[10] 

        # Test for decision branches
        # If the user leveled up, decrement the EXP and upgrade their letter grade
        if x >= S_EXP_REQUIREMENT:
            # Perform the calculation
            x -= S_EXP_REQUIREMENT
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
            EXP_to_next = S_EXP_REQUIREMENT - x

            # Let the uer know that they didn't reach the EXP requirement 
            print("You do not have enough EXP to reach the next letter.")
            print(f"Current letter: {current_letter}")
            # Let's the user know how much EXP they need from the current deduction to get to the next rank
            print(f"EXP to next: {EXP_to_next}")
            print("----------------------------------------------------------")
            print(f"\nEXP required for {new_letter}: {S_EXP_REQUIREMENT}")

    # Debugged
    def calculate_to_S_plus(x=0, S_PLUS_EXP_REQUIREMENT=760):
        # Requirement for promotion to letter: 760 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (S)
        current_letter = GradeCalculator.letter_grades[10]
        
        # Sets the upgraded letter to S+ from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[11] 

        # Test for decision branches
        # If the user leveled up, decrement the EXP and upgrade their letter grade
        if x >= S_PLUS_EXP_REQUIREMENT:
            # Perform the calculation
            x -= S_PLUS_EXP_REQUIREMENT
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
            EXP_to_next = S_PLUS_EXP_REQUIREMENT - x

            # Let the uer know that they didn't reach the EXP requirement 
            print("You do not have enough EXP to reach the next letter.")
            print(f"Current letter: {current_letter}")
            # Let's the user know how much EXP they need from the current deduction to get to the next rank
            print(f"EXP to next: {EXP_to_next}")
            print("----------------------------------------------------------")
            print(f"\nEXP required for {new_letter}: {S_PLUS_EXP_REQUIREMENT}")

    # Debugged
    def calculate_to_MAX(x=0, MAX_EXP_REQUIREMENT=900):
        # Requirement for promotion to letter: 900 EXP
        # Subtracts the user's total EXP points from the requirement
        # If the EXP total is greater or equal to the requirement, the user upgrades to the next letter
        
        # Sets the current letter, granted the user didn't level up by default from the tuple (S+)
        current_letter = GradeCalculator.letter_grades[11]
        
        # Sets the upgraded letter to MAX from the tuple granted the user leveled up 
        new_letter = GradeCalculator.letter_grades[12] 

        # Test for decision branches
        # If the user leveled up, decrement the EXP and upgrade their letter grade
        if x >= MAX_EXP_REQUIREMENT:
            # Perform the calculation
            x -= MAX_EXP_REQUIREMENT
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
            EXP_to_next = MAX_EXP_REQUIREMENT - x

            # Let the uer know that they didn't reach the EXP requirement 
            print("You do not have enough EXP to reach the next letter.")
            print(f"Current letter: {current_letter}")
            # Let's the user know how much EXP they need from the current deduction to get to the next rank
            print(f"EXP to next: {EXP_to_next}")
            print("----------------------------------------------------------")
            print(f"\nEXP required for {new_letter}: {MAX_EXP_REQUIREMENT}")

    # 
    def display_skill_category(self):
        print(f"{self.skill_category}")

dummy_EXP = 200

class Sword(GradeCalculator):
    pass

class Lance(GradeCalculator):
    pass

class Axe(GradeCalculator):
    pass


class Bow(GradeCalculator):
    pass


class Brawl(GradeCalculator):
    pass

class Reason(GradeCalculator):
    pass


class Faith(GradeCalculator):
    pass


class Authority(GradeCalculator):
    pass

class HeavyArmor(GradeCalculator):
    pass

class Riding(GradeCalculator):
    pass

class Flying(GradeCalculator):
    pass

# Get the user's input
# calculate based on user's input

sword = GradeCalculator(GradeCalculator.skill_categories[0])
lance = GradeCalculator(GradeCalculator.skill_categories[1])
axe  = GradeCalculator(GradeCalculator.skill_categories[2])
bow = GradeCalculator(GradeCalculator.skill_categories[3])
brawl = GradeCalculator(GradeCalculator.skill_categories[4])
reason = GradeCalculator(GradeCalculator.skill_categories[5])
faith = GradeCalculator(GradeCalculator.skill_categories[6])
authority = GradeCalculator(GradeCalculator.skill_categories[7])
heavy_armor = GradeCalculator(GradeCalculator.skill_categories[8])
riding = GradeCalculator(GradeCalculator.skill_categories[9]) 
flying = GradeCalculator(GradeCalculator.skill_categories[10])


# Hold Up!
# I should get the user input here 

skill_categories_elements = (1,2,3,4,5,6,7,8,9,10,11)
valid_total_exp_input = False
valid_skill_category_choice = False
valid_letter_grade_input = False


# Tuple that contains the methods for the calculations
calculations = (GradeCalculator.calculate_to_E_plus(), 
                GradeCalculator.calculate_to_D(), GradeCalculator.calculate_to_D_plus(),
                GradeCalculator.calculate_to_C(), GradeCalculator.calculate_to_C_plus(),
                GradeCalculator.calculate_to_B(), GradeCalculator.calculate_to_B_plus(),
                GradeCalculator.calculate_to_A(), GradeCalculator.calculate_to_A_plus(), 
                GradeCalculator.calculate_to_S_plus(), GradeCalculator.calculate_to_S(),
                GradeCalculator.calculate_to_MAX)

# Display the list of skill categories
print("List of Skill Categories: ")
print("------------------------------------------------")
for category_index, skill_category in enumerate(GradeCalculator.skill_categories,start=1):
    print(f"{category_index}. {skill_category}")

# Let the user choose what skill category they want to calculate for 
skill_category_choice = int(input("\nPlease enter a skill category to upgrade (1-11): ").strip())
if skill_category_choice in skill_categories_elements:
    valid_skill_category_choice = True
    if valid_skill_category_choice == skill_categories_elements[0]:
        current_skill_category = sword
    elif valid_skill_category_choice == skill_categories_elements[1]:
        current_skill_category == lance
    elif valid_skill_category_choice == skill_categories_elements[2]:
        current_skill_category == axe
    elif valid_skill_category_choice == skill_categories_elements[3]:
        current_skill_category == bow
    elif valid_skill_category_choice == skill_categories_elements[4]:
        current_skill_category == brawl
    elif valid_skill_category_choice == skill_categories_elements[5]:
        current_skill_category == reason
    elif valid_skill_category_choice == skill_categories_elements[6]:
        current_skill_category == faith
    elif valid_skill_category_choice == skill_categories_elements[7]:
        current_skill_category == authority
    elif valid_skill_category_choice == skill_categories_elements[8]:
        current_skill_category == heavy_armor
    elif valid_skill_category_choice == skill_categories_elements[9]:
        current_skill_category == riding
    elif valid_skill_category_choice == skill_categories_elements[9]:
        current_skill_category ==  flying
else:
    valid_skill_category_choice = False
    print("You did not enter the correct number")

# Get the number of EXP for that skill category
total_exp_input = int(input(f"Please enter your current number of total EXP for {current_skill_category.skill_category}: "))
if total_exp_input > 0:
    valid_total_exp_input = True
else:
    valid_total_exp_input = False

# Display the list of letter grades to the user 
print("\nList of letter grades:")
print("------------------------------------------------")
for letter in GradeCalculator.letter_grades:
    print(letter)


#for calculation in calculations:
    #result = calculation()

# Get the letter grade from the user
letter_grade_input = input("Please enter a letter grade to calculate up to (E+ - MAX): ")
if letter_grade_input in GradeCalculator.letter_grades:
    valid_letter_grade_input = True
    if letter_grade_input == GradeCalculator.letter_grades[0]:
        current_skill_category.calculate_to_E_plus(total_exp_input)
    elif letter_grade_input == GradeCalculator.letter_grades[1]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[2]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[3]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[4]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[5]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[6]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[7]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[8]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[9]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[10]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[11]:
        pass
    elif letter_grade_input == GradeCalculator.letter_grades[12]:
        pass
else:
    valid_letter_grade_input = False
    print("You did not enter a valid letter grdae.")





    

#sword_EXP = 0


