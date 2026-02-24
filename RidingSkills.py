# Filename: RidingSkills.py
# Date: 2/21/26
# Author: Aoi | shadowsnowwolf 
# Riding (Fitness and Extracurricular) skill list

class RidingSkills:
    S_plus_skills = (
    "Infinite Stamina", 
    "Olympic Runner", 
    "Master Driver", 
    "Breakdancing + 3", 
    "Highway Driving + 5",
    "Lane Switching + 5",
    "Fitness Education + 5"
)
    S_skills = (
    "Fast as Wind", 
    "Speed + 15", 
    "Driving + 5",
    "Highway Driving + 4",
    "Lane Switching + 4",
    "Parking + 5",
    "Cooking + 5",
    "Meal Prep + 5",
    "Eating Habits Lvl 3",
    "Push Ups + 5",
    "Sit Ups + 5"
)
    A_plus_skills = (
    "Monster Stamina",
    "Driving + 3", 
    "Balance + 3",
    "Gym Rat", 
    "Cooking + 4",
    "Fitness Education + 4",
    "Sit Ups + 4"
)
    A_skills = (
    "Rock Solid-Hero",
    "Defensive Driver",
    "Consistent Eater",
    "Footwork + 3",
    "Movement + 3",
    "Driving + 4",
    "Highway Driving + 3",
    "Lane Switching + 3",
    "Parking + 4",
    "Meal Prep + 4",
    "Jumping Jacks + 5",
    "Push Ups + 4",
    "Sit Ups + 3"
)
    B_plus_skills = (
    "Long Strides", 
    "Big Eater",
    "Speed + 10", 
    "Balance + 2", 
    "Consistent Exercise + 2",
    "Driving + 3",
    "Cooking + 3"
    )

    B_skills = (
    "Safe Driver" 
    "Movement + 2" 
    "Footwork + 2" 
    "Breakdancing + 2" 
    "Highway Driving + 2"
    "Lane Switching + 2"
    "Parking + 3"
    "Fitness Education + 3"
    "Meal Prep + 3"
    "Eating Habits Lvl 2"
    "Jumping Jacks + 4"
    "Push Ups + 3"
)
    C_plus_skills = (
    "Stronger Immune System", 
    "Consistent Exercise + 1", 
    "Driving + 2",
    "Lane Switching + 1",
    "Parking + 2",
    "Fitness Education + 2",
    "Jumping Jacks + 3",
    "Push Ups + 2"
)
    C_skills = (
    "Balance + 1",
    "Breakdancing + 1",
    "Highway Driving + 1",
    "Cooking + 2",
    "Meal Prep + 2",
    "Sit ups + 2"
)
    D_plus_skills = (
    "Novice Stamina", 
    "Driving + 1", 
    "Parking + 1",
    "Fitness Education + 1",
    "Meal Prep + 1",
    "Push Ups + 1",
    "Sit Ups + 1",
    "Jumping Jacks + 2"
)
    D_skills = (
    "Speed + 5", 
    "Footwork + 1", 
    "Eating Habits Lvl 1"
)
    E_plus_skills = (
    "Movement + 1",
    "Cooking + 1",
    "Jumping Jacks + 1"
)

# Displays the full list of E+ skills
def display_e_plus_skills():
    print("E+:")
    for skill in RidingSkills.E_plus_skills:
        print(skill)

# Displays the full list of D skills
def display_d_skills():
    print("D:")
    for skill in RidingSkills.D_skills:
        print(skill)
    
# Displays the full list of D+ skills
def display_d_plus_skills():
    print("D+:")
    for skill in RidingSkills.D_plus_skills:
        print(skill)

# Displays the full list of C skills
def display_c_skills():
    print("C:")
    for skill in RidingSkills.C_skills:
        print(skill)

# Displays the full list of C+ skills
def display_c_plus_skills():
    print("C+:")
    for skill in RidingSkills.C_plus_skills:
        print(skill)

# Displays the full list of B skills
def display_b_skills():
    print("B:")
    for skill in RidingSkills.B_skills:
        print(skill)

# Displays the full list of B+ skills
def display_b_plus_skills():
    print("B+:")
    for skill in RidingSkills.B_plus_skills:
        print(skill)

# Displays the full list of A skills
def display_a_skills():
    print("A:")
    for skill in RidingSkills.A_skills:
        print(skill)

# Displays the full list of A+ skills
def display_a_plus_skills():
    print("A+:")
    for skill in RidingSkills.A_plus_skills:
        print(skill)

# Displays the full list of S skills
def display_s_skills():
    print("S:")
    for skill in RidingSkills.S_skills:
        print(skill)

# Displays the full list of S+ skills
def display_s_plus_skills():
    print("S+:")
    for skill in RidingSkills.S_plus_skills:
        print(skill)
