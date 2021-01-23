from constants import *
from exposure import ExposureChance
import parsers


def initialize_exposures():
    exposures = {}

    for c in CLASSES:
        exposures[c] = ExposureChance(c, CLASS_EXPOSURE_FACTOR)
        transition = c + " Transition"
        exposures[transition] = ExposureChance(
            transition, TRANSITION_EXPOSURE_FACTOR, False
        )

    for ec in ECS:
        exposures[ec] = ExposureChance(ec, EC_EXPOSURE_FACTOR)
        transition = ec + " Transition"
        exposures[transition] = ExposureChance(
            transition, TRANSITION_EXPOSURE_FACTOR, False
        )

    return exposures


def get_class_set(class_, period, students):
    class_set = []
    for s in students:
        if class_ in s.schedule[period]:
            class_set.append(s)


def get_class_sets_for_period(period, students):
    period_set = {}
    for c in CLASSES:
        period_set[c] = get_class_set(c, period, students)
    for ec in ECS:
        period_set[ec] = get_class_set(ec, period, students)


def get_class_sets(students):
    sets = {}
    for p in range(NUM_PERIODS):
        sets[p] = get_class_sets_for_period(p, students)
    return sets


def run_simluation(exposures, students):
    class_sets = get_class_sets()
    transition = True
    for p in range(NUM_PERIODS):
        for class_ in class_sets[p]:
            if transition:
                exposures[class_ + ' Transition'].calculate_exposure(class_sets[p][class_])
            else:
                exposures[class_].calculate_exposure(class_sets[p][class_])
        transition ^= True

def load_population():
    students = parsers.get_students()
    teachers = parsers.get_teachers()
    tas = parsers.get_tas()

    infects = parsers.get_infects()

    for infect in infects:
        if infect.id is None:
            for ta in tas:
                if infect == ta:
                    ta.exposure = (1, 1)
                    # print(ta)
        else:
            for l in [students, teachers]:
                for p in l:
                    if infect == p:
                        p.exposure = (1, 1)
                        # print(p)
    return students + teachers + tas


if __name__ == "__main__":
    population = load_population()
