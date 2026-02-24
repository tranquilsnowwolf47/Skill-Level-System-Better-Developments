# Filename: SkillManual.py
# Date: 2/21/26
# Author: Aoi | shadowsnowowlf 

# Let the user choose a skill category
# Choose a letter or display all at once 
# Allow them to view the requirement 
# Skill tracker program based on letter grade (proficiency level based
#on gained experience)

# Will import modules 

# A list that will append the unlocked skills 

# Ex: Dog (Has requiremnt)
# If user wants to print out all the skills at once . do this for each
# A function will be needed for that 
# Maybe a nested loop
#if input == A_plus:
    #for skill in A_plus:
        #print(skill)


import SwordSkills
import LanceSkills
import AxeSkills
import BowSkills
import BrawlSkills
import ReasonSkills
import FaithSkills
import AuthoritySkills
import HeavyArmorSkills
import RidingSkills
import FlyingSkills

skill_categories = ("Sword","Lance","Axe","Bow","Brawl","Reason","Faith","Authority","Heavy Armor","Riding","Flying")
display_choices = ("All", "Letters")
letter_grades = ("E+","D","D+","C","C+","B","B+","A","A+","S","S+")
unlocked_skills = []

# Debugging 
# print(len(skill_categories)) 

# Display the basic info
print("Skill Categories: ")
print("---------------------------------------------------------------------")
for skill_category in skill_categories:
    print(skill_category)
print()


# Get the skill category
skill_category_choice = input("Please enter a skill category to see info for: ").capitalize() 

# Input validation
if skill_category in skill_categories:
    valid_skill_category = True
    if skill_category_choice == skill_categories[0]: # 
        print("Would you like to see all skills or by individual letter?")
        display_choice = ("Enter 'All' for all skills or enter 'Letters' for individual letters: ")
        if display_choice in display_choices:
            valid_display_choice = True
            if display_choice == display_choices[0]:
                pass
            elif display_choice == display_choices[1]:
                pass
        else:
            valid_display_choice = False
            print("Wrong input.")

    elif skill_category_choice == skill_categories[1]:
        pass
    elif skill_category_choice == skill_categories[2]:
        pass
    elif skill_category_choice == skill_categories[3]:
        pass
    elif skill_category_choice == skill_categories[4]:
        pass
    elif skill_category_choice == skill_categories[5]:
        pass
    elif skill_category_choice == skill_categories[6]:
        pass
    elif skill_category_choice == skill_categories[7]:
        pass
    elif skill_category_choice == skill_categories[8]:
        pass
    elif skill_category_choice == skill_categories[9]:
        pass
    elif skill_category_choice == skill_categories[10]:
        pass
else:
    valid_skill_category = False
    print("You did not enter the correct skill category.")
