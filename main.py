# from constants import *
from exposure import ExposureChance
import parsers

<<<<<<< Updated upstream
def initialize_exposures():
    exposures = {}

    for c in CLASSES:
        exposures[c] = ExposureChance(c, CLASS_EXPOSURE_FACTOR)
        transition = c + ' Transition'
        exposures[transition] = ExposureChance(transition, TRANSITION_EXPOSURE_FACTOR, False)

    for ec in ECS:
        exposures[ec] = ExposureChance(ec, EC_EXPOSURE_FACTOR)
        transition = ec + ' Transition'
        exposures[transition] = ExposureChance(transition, TRANSITION_EXPOSURE_FACTOR, False)

    return exposures

def get_class_set(class, period, students):
    class_set = []
    for s in students:
        if class in s.schedule[period]:
            class_set.append(s)

def get_class_sets_for_period(period, students):
    period_set = {}
    for c in CLASSES:
        period_set[c] = get_class_set(c, period, students)
    for ec in ECS:
        period_set[ec] = get_class_set(ec, period, students)

def get_class_sets(students):
    sets = {}
    for p in range(13):
        sets[p] = get_class_sets_for_period(p, students)
    return sets
    
def run_simluation(exposures, students):
    def have_class():
        for e in exposures:
            pass
        period_transition()

    def ecs():
        period_transition()

    def lunch():
        period_transition()
=======

# def initialize_exposures():
#     exposures = {}
#     for c in CLASSES:
#         exposures[c] = ExposureChance(c, CLASS_EXPOSURE_FACTOR)
#         transition = c + ' Transition'
#         exposures[transition] = ExposureChance(transition, TRANSITION_EXPOSURE_FACTOR)

#     for ec in ECS:
#         exposures[ec] = ExposureChance(ec, EC_EXPOSURE_FACTOR)
#         transition = ec + ' Transition'
#         exposures[transition] = ExposureChance(transition, TRANSITION_EXPOSURE_FACTOR)

#     return exposures

>>>>>>> Stashed changes

# def run_simluation(exposures, students):
#     def have_class():
#         for e in exposures:
#             pass 

<<<<<<< Updated upstream
    class_sets = get_class_sets()

    period_transition()
    have_class()
    have_class()
    lunch()
    have_class()
    have_class()
    ecs()
=======
#     def ecs():
#         pass

#     def period_transition():
#         pass
>>>>>>> Stashed changes

#     def lunch():
#         pass

#     have_class()
#     period_transition()
#     have_class()
#     period_transition()
#     lunch()
#     have_class()
#     period_transition()
#     have_class()
#     period_transition()
#     ecs()

#     show_exposures()

<<<<<<< Updated upstream

    
=======
# def show_exposures():
#     pass


def load_population():
    students = parsers.get_students()
    teachers = parsers.get_teachers()
    tas = parsers.get_tas()

    infects = parsers.get_infects()

    for infect in infects:
        if p.id is None:
            for ta in tas:
                if infect == ta:
                    ta.initial_exposure = (1, 1)
                    print(ta)
        else:
            for l in [students, teachers]:
                for p in l:
                    if infect == p:
                        p.initial_exposure = (1, 1)
                        print(ta)
    return students + teachers + tas


if __name__ == "__main__":
    population = load_population()
>>>>>>> Stashed changes
