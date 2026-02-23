# Filename: HeavyArmorSkills.py
# Date: 2/21/26
# Author: Aoi | shadowsnowwolf 
# Heavy Armor (Grit and Guts) skill list

class HvyArmorSkills:
    S_plus_skills = (
"Ballet Muscles", 
"Golem",
"Self-control + 5",
"Grit + 5",
"Courage + 5",
"Discipline + 5"
)
    
    S_skills = (
"Defensive Tactics", 
"Pain Tolerance + 3", 
"Flexibility + 3", 
"Self-control + 4",
"Grit + 4",
"Super Armor Lvl 3",
"Courage + 4",
"Discipline + 4"
)
    
    A_plus_skills = (
"Focused Mind",
"Grit + 3", 
"Flexibility + 2" 
)
    
    A_skills = (
"Anti-shuffle",
"Masochist", 
"Resistance + 3", 
"Self-control + 3",
"Grit + 3",
"Super Armor Lvl 2",
"Courage + 3"
)
    
    B_plus_skills = (
"Pain Tolerance + 2", 
"Discipline + 3"
)
    
    B_skills = (
"Stubborn Fighter", 
"Grit + 2", 
"Self-control + 2",
"Super Armor Lvl 1",
"Courage + 2"
)
    
    C_plus_skills = (
"Alert Stance", 
"Flexibility + 1",
"Grit + 2",
"Courage + 1"
)
    
    C_skills = (
"Resistance + 2", 
"Self-control + 1",
"Discipline + 2"
)
    
    D_plus_skills = ("Grit + 1")

    D_skills = (
"Pain Tolerance + 1", 
"Discipline + 1"
)
    E_plus_skills = ("Resistance + 1")

# Displays the full list of E+ skills
def display_e_plus_skills():
    print("E+:")
    print(HvyArmorSkills.E_plus_skills)

# Displays the full list of D skills
def display_d_skills():
    print("D")
    for skill in HvyArmorSkills.D_skills:
        print(skill)
    
# Displays the full list of D+ skills
def display_d_plus_skills():
    print("D+")
    print(HvyArmorSkills.D_plus_skills)

# Displays the full list of C skills
def display_c_skills():
    print("C")
    for skill in HvyArmorSkills.C_skills:
        print(skill)

# Displays the full list of C+ skills
def display_c_plus_skills():
    print("C+")
    for skill in HvyArmorSkills.C_plus_skills:
        print(skill)

# Displays the full list of B skills
def display_b_skills():
    print("B")
    for skill in HvyArmorSkills.B_skills:
        print(skill)

# Displays the full list of B+ skills
def display_b_plus_skills():
    print("B+")
    for skill in HvyArmorSkills.B_plus_skills:
        print(skill)

# Displays the full list of A skills
def display_a_skills():
    print("A")
    for skill in HvyArmorSkills.A_skills:
        print(skill)

# Displays the full list of A+ skills
def display_a_plus_skills():
    print("A+")
    for skill in HvyArmorSkills.A_plus_skills:
        print(skill)

# Displays the full list of S skills
def display_s_skills():
    print("S")
    for skill in HvyArmorSkills.S_skills:
        print(skill)

# Displays the full list of S+ skills
def display_s_plus_skills():
    print("S+")
    for skill in HvyArmorSkills.S_plus_skills:
        print(skill)
