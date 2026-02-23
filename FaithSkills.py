# Filename: FaithSkills.py
# Date: 2/21/26
# Author: Aoi | shadowsnowwolf 
# Faith (Piety and Spirituality) skill list


class FaithSkills:
    S_plus_skills = (
"Child of God",
"Luck + 5",
"Risk Taking + 5",
"Bible Knowledge + 5"
)
    
    S_skills = (
"Divine Knowledge",
"Sacred Power",
"Divine Fortune",
"Miracle Granter",
"Luck + 4",
"Risk Taking + 4",
"Karma + 5",
"Bible Reading Lvl 3",
"Bible Knowledge + 4"
)
    
    A_plus_skills = (
"Pro-Life Gambler",
"Scripture Reader",
"Karma + 4",
"Faith Prowess Lvl. 5"
)
    
    A_skills = (
"Divine Bond + 3",
"Humility + 3",
"Luck + 3",
"Risk Taking + 3",
"Bible Knowledge + 3"
)
    
    B_plus_skills = (
"Sacred Prayer",
"Virtue + 3",
"Faith Prowess Lvl. 4"
)
    
    B_skills = (
"Divine Bond + 2",
"Humility + 2",
"Virtue + 2",
"Risk taking + 2",
"Karma + 3",
"Bible Reading Lvl 2",
"Bible Knowledge + 2"
)
    
    C_plus_skills = (
"Faith Prowess Lvl. 3", 
"Divine Bond + 1",
"Luck + 2"
)
    
    C_skills = (
"Virtue + 1",
"Humility + 1",
"Risk Taking + 1",
"Bible Knowledge + 1"
)
    
    D_plus_skills = (
"Luck + 1",
"Karma + 2",
"Bible Reading Lvl 1",
"Faith Prowess Lvl. 2"
)
    
    D_skills = ("Karma + 1")

    E_plus_skills = (
"Prayer",
"Faith Prowess Lvl. 1")
    
# Displays the full list of E+ skills
def display_e_plus_skills():
    print("E+:")
    for skill in FaithSkills.E_plus_skills:
        print(skill)

# Displays the full list of D skills
def display_d_skills():
    print("D")
    print(FaithSkills.D_skills)

# Displays the full list of D+ skills
def display_d_plus_skills():
    print("D+")
    for skill in FaithSkills.D_plus_skills:
        print(skill)

# Displays the full list of C skills
def display_c_skills():
    print("C")
    for skill in FaithSkills.C_plus_skills:
        print(skill)

# Displays the full list of C+ skills
def display_c_plus_skills():
    print("C+")
    for skill in FaithSkills.C_plus_skills:
        print(skill)

# Displays the full list of B skills
def display_b_skills():
    print("B")
    for skill in FaithSkills.B_skills:
        print(skill)

# Displays the full list of B+ skills
def display_b_plus_skills():
    print("B+")
    for skill in FaithSkills.B_plus_skills:
        print(skill)

# Displays the full list of A skills
def display_a_skills():
    print("A")
    for skill in FaithSkills.A_skills:
        print(skill)

# Displays the full list of A+ skills
def display_a_plus_skills():
    print("A+")
    for skill in FaithSkills.A_plus_skills:
        print(skill)

# Displays the full list of S skills
def display_s_skills():
    print("S")
    for skill in FaithSkills.S_skills:
        print(skill)

# Displays the full list of S+ skills
def display_s_plus_skills():
    print("S+")
    for skill in FaithSkills.S_plus_skills:
        print(skill)
