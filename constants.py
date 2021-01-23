from itertools import product

# randomly chosen
CLASS_EXPOSURE_FACTOR = 0.5
EC_EXPOSURE_FACTOR = 0.7
TRANSITION_EXPOSURE_FACTOR = 0.3

TA_EXPOSURE_FACTOR = 0.9
TEACHER_EXPOSURE_FACTOR = 0.8

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
