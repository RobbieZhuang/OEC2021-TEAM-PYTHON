from itertools import product
from enum import Enum

class Occupation(Enum):
    Student = 0
    Teacher = 1
    TA = 2

# randomly chosen
CLASS_EXPOSURE_FACTOR = 1.0
EC_EXPOSURE_FACTOR = 1.1
TRANSITION_EXPOSURE_FACTOR = 0.9

# students more likely to interact with one another
OCCUPATIONAL_EXPOSURE_FACTORS = {
    Occupation.Student: 1.0,
    Occupation.Teacher: 0.8,
    Occupation.TA: 0.9,
}

R_0 = 3
AVERAGE_EXPOSURES = 100

CLASSES = [
    f"{cl} {sec}"
    for cl, sec in product(
        [
            "Physics",
            "Biology",
            "Functions",
            "Calculus",
            "Philosophy",
            "Art",
            "Drama",
            "Computer Science",
            "Computer Engineering",
            "Humanities",
        ],
        ["A", "B"],
    )
]

CLASSES.extend([f'Gr {gr} Lunch' for gr in range(9, 13)])

ECS = [
    "Board Game Club",
    "Football",
    "Soccer",
    "Video Game Club",
    "Band",
    "Computer Science Club",
    "Choir",
    "Basketball",
    "Badminton",
    "Baseball",
]
