# Filename: SkillManualV1.py
# Date: 2/21/26
# Author: Aoi | shadowsnowowlf 

# Let the user choose a skill category
# Choose a letter or display all at once 
# Allow them to view the requirement 
# Skill tracker program based on letter grade (proficiency level based
#on gained experience)

# Beta prototype for the Skill Manual program

# Will import modules 

# A list that will append the unlocked skills 

# Ex: Dog (Has requiremnt)
# If user wants to print out all the skills at once . do this for each
# A function will be needed for that 
# Maybe a nested loop
#if input == A_plus:
    #for skill in A_plus:
        #print(skill)


import SwordSkills, LanceSkills, AxeSkills
import BowSkills, BrawlSkills, ReasonSkills
import FaithSkills, AuthoritySkills, HeavyArmorSkills
import RidingSkills, FlyingSkills

skill_categories = ("Sword","Lance","Axe","Bow (Intelligence and Education)","Brawl","Reason (Mind and Spirit)","Faith","Authority","Heavy Armor","Riding (Fitness and Extracurricular)","Flying (Organizational)")
skill_categories = (SwordSkills.skill_category, LanceSkills.skill_category, AxeSkills.skill_category, BowSkills.skill_category, BrawlSkills.skill_category,
ReasonSkills.skill_category, FaithSkills.skill_category, AuthoritySkills.skill_category, HeavyArmorSkills.skill_category, RidingSkills.skill_category, FlyingSkills.skill_category)

loop = True
skill_category_menu_choices = (1,2,3,4,5,6,7,8,9,10,11)
display_choices = ("All", "Letters")
letter_grades = ("E+","D","D+","C","C+","B","B+","A","A+","S","S+")
unlocked_skills = []


# Debugging 
# print(len(skill_categories)) 

def get_header_choice():
    header_choice = input("Would you like to see a header of the skill category? (Y or N): ").capitalize()
    return header_choice

while loop:
    # Display the basic info
    print("Skill Categories: ")
    for skill_index, skill_category in enumerate(skill_categories,start=1):
        print(f"\t{skill_index}. {skill_category}")
    print("---------------------------------------------------------------------")

    # Get the skill category
    skill_category_choice = int(input("Please enter a skill category to see info for (1-11): "))

    # Input validation
    # Confirm if the user entered a valid input (number)
    if skill_category_choice in skill_category_menu_choices:
        valid_menu_choice = True

        # Validate per skill category
        # Input validation for Sword 
        if skill_category_choice == skill_category_menu_choices[0]:
            # Allows the user to choose if they want to see all the skills at once, or just the skills of the correpsonding letter  
            display_choice = input("Would you like to see all skills or by individual letter? (Enter 'All' to see all skills or 'Letters' for individual letters): ").capitalize()
            if display_choice in display_choices: # Validate whether the user chose the right option choice or not 
                valid_display_choice = True
        
                # Operations for all letters
                if display_choice == display_choices[0]: # For displaying all letters
                    header_choice = input("Would you like to see a header of the skill category? (Y or N): ").capitalize()
                    if header_choice == "Y":
                        print()
                        SwordSkills.display_all_sword_skills(True) # call the function that displays all skills with the header 
                    else:
                        print()
                        SwordSkills.display_all_sword_skills() # call the function that displays all skills without the header        
                
                # Operations for indivdual letters
                elif display_choice == display_choices[1]: # Display the individual letters to the user so they know which letters they can choose
                    print(f"List of {skill_categories[0]} letter grades: ")
                    for letter in letter_grades:
                        print(letter)
                    print()

                    letter_input = input("Please enter a letter to display skills for: ") # Get the letter from the user that they want to see skills for
                    if letter_input in letter_grades: # Validate whether they entered a letter in the tuple or not 
                        valid_letter = True
                        #print("Eureka! It worked!") # Debugging 
                        
                        # For E+
                        if letter_input == letter_grades[0]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_e_plus_skills(True)
                            else:
                                SwordSkills.display_e_plus_skills() # Call the letter function without the header
                        # For D
                        elif letter_input == letter_grades[1]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_d_skills(True)
                            else:
                                SwordSkills.display_d_skills()
                        # For D+
                        elif letter_input == letter_grades[2]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_d_plus_skills(True)
                            else:
                                SwordSkills.display_d_plus_skills()
                        # For C
                        elif letter_input == letter_grades[3]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_c_skills(True)
                            else:
                                SwordSkills.display_c_skills()
                        # For C+
                        elif letter_input == letter_grades[4]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_c_plus_skills(True)
                            else:
                                SwordSkills.display_c_plus_skills()
                        # For B
                        elif letter_input == letter_grades[5]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_b_skills(True) 
                            else:
                                SwordSkills.display_b_skills()
                        # For B+
                        elif letter_input == letter_grades[6]:
                                header_choice = get_header_choice()
                                if header_choice == "Y": # Call the letter function with the header
                                    SwordSkills.display_b_plus_skills(True)
                                else:
                                    SwordSkills.display_b_plus_skills() 
                        # For A
                        elif letter_input == letter_grades[7]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_a_skills(True)
                            else:
                                SwordSkills.display_a_skills() 
                        # For A+
                        elif letter_input == letter_grades[8]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_a_plus_skills(True)
                            else:
                                SwordSkills.display_a_plus_skills() 
                        # For S
                        elif letter_input == letter_grades[9]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_s_skills(True)
                            else:
                                SwordSkills.display_s_skills() 
                        # For S+
                        elif letter_input == letter_grades[10]:
                            header_choice = get_header_choice()
                            if header_choice == "Y": # Call the letter function with the header
                                SwordSkills.display_s_plus_skills(True)
                            else:
                                SwordSkills.display_s_plus_skills() 
                    else:
                        print("Invalid letter.")
                        valid_letter = False
            else:
                valid_display_choice = False
                print("Wrong input.")
    # For Lance
    elif skill_category_choice == skill_category_menu_choices[1]: 
        pass
    # For Axe
    elif skill_category_choice == skill_category_menu_choices[2]: 
        pass
    # For Bow
    elif skill_category_choice == skill_category_menu_choices[3]: 
        pass
    # For Brawl
    elif skill_category_choice == skill_category_menu_choices[4]: 
        pass
    # For Reason
    elif skill_category_choice == skill_category_menu_choices[5]: 
        pass
    # For Faith
    elif skill_category_choice == skill_category_menu_choices[6]: 
        pass
    # For Authority
    elif skill_category_choice == skill_category_menu_choices[7]: 
        pass
    # For Heavy Armor
    elif skill_category_choice == skill_category_menu_choices[8]: 
        pass
    # For Riding
    elif skill_category_choice == skill_category_menu_choices[9]: 
        pass
    # For Flying
    elif skill_category_choice == skill_category_menu_choices[10]: 
        pass
    # Catch if the user doesn't enter the correct number corresponding to the skill category
    else:
        valid_menu_choice = False
        print("You did not enter the correct skill category.")
    
    loop_choice = input("\nWould you like to try again? (Y-N): ").upper()
    if loop_choice == "Y":
        loop
    else:
        break

