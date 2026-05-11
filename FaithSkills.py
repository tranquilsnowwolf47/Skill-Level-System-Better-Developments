# Filename: FaithSkills.py
# Date: 2/21/26
# Author: Aoi | shadowsnowwolf 
# Faith (Piety and Spirituality) skill list


class FaithSkills:
    S_plus_skills = (
"Child of God",
"Luck + 5",
"Risk Taking + 5",
"Bible Knowledge + 5",
"Old Testament Lvl 3", 
"New Testament Lvl 3", 
"Matthew | Requirement: Complete the book of Matthew",
"Mark | Requirement: Complete the book of Mark",
"Luke | Requirement: Complete the book of Luke",
"John | Requirement: Complete the book of John",
"Acts | Requirement: Complete the book of Acts",
"Romans | Requirement: Complete the book of Romans",
"1 Corinthians | Requirement: Complete the book of 1 Corinthians",
"2 Corinthians | Requirement: Complete the book of 2 Corinthians",
"Galatians | Requirement: Complete the book of Galatians",
"Ephesians | Requirement: Complete the book of Ephesians",
"Phillippians | Requirement: Complete the book of Phillippians",
"Colossians | Requirement: Complete the book of Colossians",
"1 Thessalonians  | Requirement: Complete the book of 1 Thessalonians",
"2 Thessalonians  | Requirement: Complete the book of 2 Thessalonians",
"1 Timothy | Requirement: Complete the book of 1 Timothy",
"2 Timothy | Requirement: Complete the book of 2 Timothy",
"Titus | Requirement: Complete the book of Titus",
"Philemon | Requirement: Complete the book of Philemon",
"Hebrews | Requirement: Complete the book of Hebrews",
"James | Requirement: Complete the book of James",
"1 Peter | Requirement: Complete the book of 1 Peter",
"2 Peter | Requirement: Complete the book of 2 Peter",
"1 John | Requirement: Complete the book of 1 John",
"2 John | Requirement: Complete the book of 2 John",
"3 John | Requirement: Complete the book of 3 John",
"Jude | Requirement: Complete the book of Jude",
"Revelation | Requirement: Complete the book of Revelation"
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
"Bible Knowledge + 4",
"New Testament Lvl 2", 
"Old Testament Lvl 2", 
"Psalms | Requirement: Complete the book of Psalms",
"Proverbs | Requirement: Complete the book of Proverbs",
"Ecclesiastes | Requirement: Complete the book of Ecclesiastes",
"Song of Songs | Requirement: Complete the book of Song of Songs",
"Isaiah | Requirement: Complete the book of Isaiah",
"Jeremiah | Requirement: Complete the book of Jeremiah",
"Lamentations | Requirement: Complete the book of Lamentations",
"Ezekiel | Requirement: Complete the book of Ezekiel",
"Daniel | Requirement: Complete the book of Daniel",
"Hosea | Requirement: Complete the book of Hosea",
"Joel | Requirement: Complete the book of Joel",
"Amos | Requirement: Complete the book of Amos",
"Obadiah | Requirement: Complete the book of Obadiah",
"Jonah | Requirement: Complete the book of Jonah",
"Micah | Requirement: Complete the book of Micah",
"Nahum | Requirement: Complete the book of Nahum",
"Habakkuk | Requirement: Complete the book of Habakkuk",
"Zephaniah | Requirement: Complete the book of Zephaniah",
"Haggai | Requirement: Complete the book of Haggai",
"Zechariah | Requirement: Complete the book of Zechariah",
"Malachi | Requirement: Complete the book of Malachi"
)
    
    A_plus_skills = (
"Pro-Life Gambler",
"Scripture Reader",
"Karma + 4",
"Divine Offering",
"New Testament Lvl 1",
"Faith Prowess Lvl. 5"
)
    
    A_skills = (
"Divine Bond + 3",
"Humility + 3",
"Luck + 3",
"Risk Taking + 3",
"Bible Knowledge + 3",
"Old Testament Lvl 1"
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
"Divine Bond + 1",
"Luck + 2",
"Offering",
"Esther | Requirement: Complete the book of Esther",
"Job | Requirement: Complete the book of Job",
"Faith Prowess Lvl. 3" 
)
    
    C_skills = (
"Virtue + 1",
"Humility + 1",
"Risk Taking + 1",
"Bible Knowledge + 1",
"1 Kings | Requirement: Complete the book of 1 Kings",
"Kings | Requirement: Complete the book of 2 Kings",
"1 Chronicles  | Requirement: Complete the book of 1 Chronicles",
"2 Chronicles  | Requirement: Complete the book of 2 Chronicles",
"Ezra | Requirement: Complete the book of Ezra",
"Nehemiah | Requirement: Complete the book of Nehemiah"
)
    
    D_plus_skills = (
"Luck + 1",
"Karma + 2",
"Bible Reading Lvl 1",
"Faith Prowess Lvl. 2",
"Judges | Requirement: Complete the book of Judges",
"Ruth | Requirement: Complete the book of Ruth",
"1 Samuel | Requirement: Complete the book of 1 Samuel", 
"2 Samuel | Requirement: Complete the book of 2 Samuel"
)
    
    D_skills = (
"Numbers | Requirement: Complete the book of Numbers",
"Deuteronomy | Requirement: Complete the book of Deuteronomy",
"Joshua | Requirement: Complete the book of Joshua",
"Karma + 1"
)

    E_plus_skills = (
"Genesis | Requirement: Complete the book of Genesis",
"Exodus | Requirement: Complete the book of Exodus",
"Leviticus | Requirement: Complete the book of Leviticus",
"Prayer",
"Faith Prowess Lvl. 1")
    
skill_category = "Faith (Piety and Spirituality)"

# Displays the full list of E+ skills
def display_e_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("E+:")
    for skill in FaithSkills.E_plus_skills:
        print(skill)

# Displays the full list of D skills
def display_d_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("D:")
    print(FaithSkills.D_skills)

# Displays the full list of D+ skills
def display_d_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("D+:")
    for skill in FaithSkills.D_plus_skills:
        print(skill)

# Displays the full list of C skills
def display_c_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("C:")
    for skill in FaithSkills.C_skills:
        print(skill)

# Displays the full list of C+ skills
def display_c_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("C+:")
    for skill in FaithSkills.C_plus_skills:
        print(skill)

# Displays the full list of B skills
def display_b_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("B:")
    for skill in FaithSkills.B_skills:
        print(skill)

# Displays the full list of B+ skills
def display_b_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("B+:")
    for skill in FaithSkills.B_plus_skills:
        print(skill)

# Displays the full list of A skills
def display_a_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("A:")
    for skill in FaithSkills.A_skills:
        print(skill)

# Displays the full list of A+ skills
def display_a_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("A+:")
    for skill in FaithSkills.A_plus_skills:
        print(skill)

# Displays the full list of S skills
def display_s_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("S:")
    for skill in FaithSkills.S_skills:
        print(skill)

# Displays the full list of S+ skills
def display_s_plus_skills(show_header=False):
    if show_header:
        print(f"{skill_category} skills:")
    print("S+:")
    for skill in FaithSkills.S_plus_skills:
        print(skill)

# Displays the full list of all skills corresponding to each skill letter
def display_all_faith_skills(show_header=False):
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
