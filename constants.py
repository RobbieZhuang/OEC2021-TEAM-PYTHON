from itertools import product
from enum import Enum
from datetime import datetime, timedelta

class Occupation(Enum):
    Student = 0
    Teacher = 1
    TA = 2


CLASS_EXPOSURE_FACTOR = 1.0
LUNCH_EXPOSURE_FACTOR = 0.5 # People usually separate into small groups, so they are unlikely to all interact
TA_LUNCH_EXPOSURE_FACTOR = 0.0 # TAs eat alone apparently
EC_EXPOSURE_FACTOR = 1.1
TRANSITION_EXPOSURE_FACTOR = 5.0 / 45.0 * CLASS_EXPOSURE_FACTOR
LAST_NAME_EXPOSURE_FACTOR = 1.3

#AVERAGE_TEACHER_AGE = 40
#AVERAGE_TA_AGE = 21

BASELINE_EXPOSURE_FACTOR = 0.3

# Chance each occupation exposes another
# First index from, second index to
OCCUPATIONAL_EXPOSURE_MATRIX = {
    Occupation.Student: {
        Occupation.Student: 1.5,
        Occupation.Teacher: 0.7,
        Occupation.TA: 0.8,
    },
    Occupation.Teacher: {
        Occupation.Student: 0.7,
        Occupation.Teacher: 1.0,
        Occupation.TA: 1.5,
    },
    Occupation.TA: {
        Occupation.Student: 0.8,
        Occupation.Teacher: 1.5,
        Occupation.TA: 1.2,
    },
}

R_0 = 3

NUM_PERIODS = (
    6 * 2
) + 1  # 4 classes, lunch, ecs, transitions between, before, and after
LUNCH_PERIOD = 5

START_TIMES = []
_time = datetime.now().replace(hour=8, minute=55, second=0, microsecond=0, tzinfo=None)

_transition = True
for i in range(NUM_PERIODS):
    START_TIMES.append(_time)
    if _transition:
        _time += timedelta(minutes=5)
    else:
        _time += timedelta(minutes=45)

    _transition = not _transition

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

CLASSES.extend([f"Gr {gr} Lunch" for gr in range(9, 13)])
CLASSES.append("TA Lunch")

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
    "Drama Club",
]
