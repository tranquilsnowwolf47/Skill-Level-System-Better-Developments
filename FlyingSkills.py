# Filename: FlyingSkills.py
# Date: 2/21/26
# Author: Aoi | shadowsnowwolf 
# Flying (Organizational) skill list

class FlyingSkills:
    S_plus_skills = (
    "Cleaning Freak",
    "Physical Organization + 5",
    "Digital Organization + 5",
    "Dish Washing + 5",
    "Cleanliness + 5",
    "Photo Organization + 5"
)
    
    S_skills = (
    "Always Organized",
    "Clean Mind",
    "Dish Conqueror",
    "Physical Organization + 4",
    "Digital Organization + 4",
    "Sweeping + 5",
    "Dish Washing + 4",
    "Cleanliness + 4"
    "Photo Organization + 4",
    "Doc Organization + 5",
    "Video Organization + 5"
    )
    
    A_plus_skills = (
    "Maid",
    "Computer File Administrator",
    "Dish Washing + 3",
    "Sweeping + 4",
    "Sticky Note Organization + 5"
    )
    
    A_skills = (
    "Cleanliness + 3",
    "Physical Organization + 3",
    "Digital Organization + 3",
    "Photo Organization + 3", 
    "Vacuuming + 5",
    "Doc Organization + 4",
    "Sticky Note Organization + 4",
    "Video Organization + 4"
    )
    
    B_plus_skills = ("Sweeping + 3",)

    B_skills = (
    "Vacuuming + 4",
    "Physical Organization + 2",
    "Digital Organization + 2",
    "Doc Organization + 3",
    "Sticky Note Organization + 3",
    "Video Organization + 3"
    )
    
    C_plus_skills = ("Cleanliness + 2",
                    "File Backup",  
                    "Photo Organization + 2"
)

    C_skills = (
    "Vacuuming + 3",
    "Sweeping + 2", 
    "Dish Washing + 2", 
    "Doc Organization + 2", 
    "Sticky Note Organization + 2",
    "Video Organization + 2"
    )

    D_plus_skills = (
    "Physical Organization + 1",
    "Digital Organization + 1"
    )

    D_skills = (
    "Vacuuming + 2"
    "Dish Washing + 1",
    "Cleanliness + 1",
    "Photo Organization + 1",
    "Doc Organization + 1",
    "Sticky Note Organization + 1",
    "Video Organization + 1"
    )

    E_plus_skills = ("Vacuuming + 1",
                     "Sweeping + 1")

skill_category = "Flying (Organizational)"

# Displays the full list of E+ skills
def display_e_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    for skill in FlyingSkills.E_plus_skills:
        print(skill)

# Displays the full list of D skills
def display_d_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("D:")
    for skill in FlyingSkills.D_skills:
        print(skill)

# Displays the full list of D+ skills
def display_d_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("D+:")
    for skill in FlyingSkills.D_plus_skills:
        print(skill)

# Displays the full list of C skills
def display_c_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("C:")
    for skill in FlyingSkills.C_skills:
        print(skill)

# Displays the full list of C+ skills
def display_c_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("C+:")
    for skill in FlyingSkills.C_plus_skills:
        print(skill)

# Displays the full list of B skills
def display_b_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("B:")
    for skill in FlyingSkills.B_skills:
        print(skill)

# Displays the full list of B+ skills
def display_b_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("B+:")
    for skill in FlyingSkills.B_plus_skills:
        print(skill)

# Displays the full list of A skills
def display_a_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("A:")
    for skill in FlyingSkills.A_skills:
        print(skill)

# Displays the full list of A+ skills
def display_a_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("A+:")
    for skill in FlyingSkills.A_plus_skills:
        print(skill)

# Displays the full list of S skills
def display_s_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("S:")
    for skill in FlyingSkills.S_skills:
        print(skill)

# Displays the full list of S+ skills
def display_s_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("S+:")
    for skill in FlyingSkills.S_plus_skills:
        print(skill)

# Displays the full list of all skills corresponding to each skill letter
def display_all_flying_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    display_e_plus_skills()
    print()
    display_d_skills()
    print()
    display_d_plus_skills()
    print()
    display_c_skills()
    print()
    display_c_plus_skills()
    print()
    display_b_skills()
    print()
    display_b_plus_skills()
    print()
    display_a_skills()
    print()
    display_a_plus_skills()
    print()
    display_s_skills()
    print()
    display_s_plus_skills()
