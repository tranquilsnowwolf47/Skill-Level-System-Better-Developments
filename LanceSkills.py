# Filename: LanceSkills.py
# Date: 2/21/26
# Author: Aoi | shadowsnowwolf 
# Lance (The Arts) skill list

class LanceSkills:
    S_plus_skills = (
"Pro Artist",
"Character Design + 5",
"Fight Scenes + 5")

    S_skills = (
"Piano Master",
"Anatomy Master",
"Mangaka",
"Action Poses + 5")

    A_plus_skills = (
"Proportions Master",
"Full Body + 3",
"Fable Teller",
"Poses + 3",
"Clothing Design Lvl 3")

    A_skills = (
"Pro Lyricist",
"Musician",
"Character Design + 4",
"Anatomy + 3",
"Full Body + 2",
"Story Telling + 2",
"Action Poses + 4",
"Fight Scenes + 4",
"Lance Prowess Lvl. 5")

    B_plus_skills = (
"Art + 3",
"Body Proportions + 3",
"Character Design + 3",
"Fight Scenes + 3",
"Anatomy + 2",
"Story Telling + 1")

    B_skills = (
"Lyricist",
"Character Design + 2",
"Art + 2",
"Poses + 2",
"Body Proportions + 2",
"Full body + 1",
"Action Poses + 3",
"Fight Scenes + 2",
"Clothing Design Lvl 2",
"Lance Prowess Lvl. 4")

    C_plus_skills = (
"Character Design + 1",
"Action Poses + 2",
"Anatomy + 1",
"Fight scenes + 1",
"Lance Prowess Lvl. 3")

    C_skills = (
"Novice Musician",
"Clothing Design Lvl 1",
"Action Poses + 1",
"Body Proportions + 1")

    D_plus_skills = (
"Apprentice Lyricist",
"Poses + 1")

    D_skills = (
"Lance Prowess Lvl. 2",
"Art + 1")

    E_plus_skills = ("Lance Prowess Lvl. 1")

# Displays the full list of E+ skills
def display_e_plus_skills():
    print("E+:")
    print(LanceSkills.E_plus_skills)

# Displays the full list of D skills
def display_d_skills():
    print("D")
    for skill in LanceSkills.D_skills:
        print(skill)

# Displays the full list of D+ skills
def display_d_plus_skills():
    print("D+")
    for skill in LanceSkills.D_plus_skills:
        print(skill)

# Displays the full list of C skills
def display_c_skills():
    print("C")
    for skill in LanceSkills.C_skills:
        print(skill)

# Displays the full list of C+ skills
def display_c_plus_skills():
    print("C+")
    for skill in LanceSkills.C_plus_skills:
        print(skill)

# Displays the full list of B skills
def display_b_skills():
    print("B")
    for skill in LanceSkills.B_skills:
        print(skill)

# Displays the full list of B+ skills
def display_b_plus_skills():
    print("B+")
    for skill in LanceSkills.B_plus_skills:
        print(skill)

# Displays the full list of A skills
def display_a_skills():
    print("A")
    for skill in LanceSkills.A_skills:
        print(skill)

# Displays the full list of A+ skills
def display_a_plus_skills():
    print("A+")
    for skill in LanceSkills.A_plus_skills:
        print(skill)

# Displays the full list of S skills
def display_s_skills():
    print("S")
    for skill in LanceSkills.S_skills:
        print(skill)

# Displays the full list of S+ skills
def display_s_plus_skills():
    print("S+")
    for skill in LanceSkills.S_plus_skills:
        print(skill)
