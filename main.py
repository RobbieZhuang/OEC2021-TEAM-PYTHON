from constants import *
from exposure import ExposureChance
from collections import defaultdict
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


def get_exposure_sets(people, period):
    sets = defaultdict(set)
    for p in people:
        if period >= len(p.schedule):
            continue
        for e in p.schedule[period]:
            sets[e].add(p)
    return sets


def run_simulation(exposures, people, follow_people = []):
    people_trace = defaultdict(list)
    for p in range(NUM_PERIODS):
        if p == LUNCH_PERIOD:
            for e in exposures.values():
                e.clean()

        sets = get_exposure_sets(people, p)
        for exposure_name, people_exposed in sets.items():
            exposures[exposure_name].calculate_exposure(list(people_exposed))
        for p in follow_people:
            people_trace[p].append((p.exposure[1], p.trace))
    return people_trace


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


def print_results(people):
    for p in people:
        print("%030s: %5.2f" % (p.firstname + " " + p.lastname, 100 * p.exposure[1]))


if __name__ == "__main__":
    population = load_population()
    exposures = initialize_exposures()
    people_trace = run_simulation(exposures, population, [])

    print_results(population)
    for p in people_trace:
        print(f"        {p.firstname} {p.lastname}'s trace")
        print(people_trace[p])
