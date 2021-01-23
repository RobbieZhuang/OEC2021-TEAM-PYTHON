from person import Person.Type as Type
from itertools import product

# randomly chosen
CLASS_EXPOSURE_FACTOR = 1.0
EC_EXPOSURE_FACTOR = 1.1
TRANSITION_EXPOSURE_FACTOR = 0.9

PERSONAL_EXPOSURE_FACTORS = {
    Type.Student: 1.0,
    Type.Teacher: 0.8,
    Type.TA: 0.9,
}

R_0 = 3
AVERAGE_EXPOSURES = 100

CLASSES = [f'{cl} {sec}' for cl, sec in product([
    'Physics',
    'Biology',
    'Functions',
    'Calculus',
    'Philosophy',
    'Art',
    'Drama',
    'Computer Science',
    'Computer Engineering',
    'Humanities'],
    ['A', 'B'])]

CLASSES.extend([f'Gr {gr} Lunch' for gr in range(9, 13)])

ECS = [
    'Board Game Club',
    'Football',
    'Soccer',
    'Video Game Club',
    'Band',
    'Computer Science Club',
    'Choir',
    'Basketball',
    'Badminton',
    'Baseball']
