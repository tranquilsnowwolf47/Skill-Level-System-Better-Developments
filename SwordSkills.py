# Filename: SwordSkills.py
# Date: 2/20/26
# Author: Aoi | shadowsnowwolf 
# Sword (Essentials) skill list

class SwordSkills:
    S_plus_skills = (
"Entrepreneur",
"Officer-like Planner",
"Time Wizard",
"Financial IQ + 50",
"Investing + 5",
"Budgeting + 5",
"Saving + 5",
"Financial Discipline + 5",
"Financial Literacy + 5",
"Transaction Tracking + 5")
    
    S_skills = (
"Baron",
"Excellent Credit Score",
"Problem-Solution Scientist",
"Schedule Planning + 5",
"Investing + 4",
"Financial Discipline + 4",
"Grocery Shopping + 5",
)
    
    A_plus_skills = (
"Master Planner", 
"Financial IQ + 40",
"Saving + 4",
"Budgeting + 4")
    
    A_skills = (
"Financially Literate", 
"Problem Solver", 
"Great Credit Score",
"Schedule Planning + 4",
"Financial IQ + 30",
"Investing + 3",
"Financial Discipline + 3",
"Financial Literacy + 4",
"Transaction Tracking + 4", 
"Sword Prowess Lvl. 5" 
)

    B_plus_skills = (
"Time Manager", 
"Financial IQ + 20",
"Investing + 2",
"Saving + 3",
"Financial Literacy + 3",
"Sword Prowess Lvl. 4",  
"Budgeting + 3"
)
    B_skills = (
"Good Credit Score",
"Good Spender",  
"Decision Maker",
"Schedule Planning + 3",
"Financial IQ + 10",
"Grocery Shopping + 4",
"Financial Literacy + 2",
"Financial Discipline + 2",
"Transaction Tracking + 3"
)
    C_plus_skills = (
"Budgeter",
"Schedule Planning + 2",
"Investing + 1",
"Transaction Tracking + 2",
"Grocery Shopping + 3",
"Sword Prowess Lvl. 3",
"Budgeting + 2"
)
    C_skills = (
"Novice Planner", 
"Novice Time Management",
"Schedule Planning + 1",
"Transaction Tracking + 1",
"Financial Literacy + 1",
"Saving + 2",
"Financial Discipline + 1",
"Sword Prowess Lvl. 2" 
)
    D_plus_skills = (
"Grocery Shopping + 2",
"Average Spender" 
)
    D_skills = (
"Budgeting + 1",
"Saving + 1",
"Sword Prowess Lvl. 1" 
)
    E_plus_skills = ("Grocery Shopping + 1")

# Displays the full list of X skills
def display_e_plus_skills():
    print("E+:")
    print(SwordSkills.E_plus_skills)

# Displays the full list of D skills
def display_d_skills():
    print("D")
    for skill in SwordSkills.D_skills:
        print(skill)

# Displays the full list of D+ skills
def display_d_plus_skills():
    print("D+")
    for skill in SwordSkills.D_plus_skills:
        print(skill)

# Displays the full list of C skills
def display_c_skills():
    print("C")
    for skill in SwordSkills.C_skills:
        print(skill)

# Displays the full list of C+ skills
def display_c_plus_skills():
    print("C+")
    for skill in SwordSkills.C_plus_skills:
        print(skill)

# Displays the full list of B skills
def display_b_skills():
    print("B")
    for skill in SwordSkills.B_skills:
        print(skill)

# Displays the full list of B+ skills
def display_b_plus_skills():
    print("B+")
    for skill in SwordSkills.B_skills:
        print(skill)

# Displays the full list of A skills
def display_a_skills():
    print("A")
    for skill in SwordSkills.A_skills:
        print(skill)

# Displays the full list of A+ skills
def display_a_plus_skills():
    print("A+")
    for skill in SwordSkills.A_plus_skills:
        print(skill)

# Displays the full list of S skills
def display_s_skills():
    print("S")
    for skill in SwordSkills.S_skills:
        print(skill)

# Displays the full list of S+ skills
def display_s_plus_skills():
    print("S+")
    for skill in SwordSkills.S_plus_skills:
        print(skill)

