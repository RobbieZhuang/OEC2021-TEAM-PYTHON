from constants import *
from exposure import ExposureChance
from collections import defaultdict
import parsers
from graph import Graph

student_inf_over_time = Graph('Average Student Infection Over Time')
infection_over_time = Graph('Average Infection Over Time')
classroom_infection_over_time = Graph('Average Classroom Infection Over Time')

def initialize_exposures():
    exposures = {}

    for c in CLASSES:
        if 'Lunch' in c:
            exposures[c] = ExposureChance(c, LUNCH_EXPOSURE_FACTOR)
        else:
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

    exposures["Last Name"] = ExposureChance(
        "Last Name", LAST_NAME_EXPOSURE_FACTOR, False
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


def group_by_last_name(people):
    sets = defaultdict(set)
    for p in people:
        sets[p.lastname].add(p)
    return sets


def update_graphs(time, exposures, people):
    all_inf = [person.exposure[1] for person in people]
    teach_inf = [person.exposure[1] for person in people if person.occupation == Occupation.Teacher]
    ta_inf = [person.exposure[1] for person in people if person.occupation == Occupation.TA]
    stud_inf = [person.exposure[1] for person in people if person.occupation == Occupation.Student]

    infection_over_time.add_point(time, {
        'all': sum(all_inf) / len(all_inf),
        'teachers': sum(teach_inf) / len(teach_inf),
        'TAs': sum(ta_inf) / len(ta_inf),
        'students': sum(stud_inf) / len(stud_inf),
        })

    gr_9 = [person.exposure[1] for person in people if person.grade == 9]
    gr_10 = [person.exposure[1] for person in people if person.grade == 10]
    gr_11 = [person.exposure[1] for person in people if person.grade == 11]
    gr_12 = [person.exposure[1] for person in people if person.grade == 12]

    student_inf_over_time.add_point(time, {
        'Gr 9': sum(gr_9) / len(gr_9),
        'Gr 10': sum(gr_10) / len(gr_10),
        'Gr 11': sum(gr_11) / len(gr_11),
        'Gr 12': sum(gr_12) / len(gr_12),
        })

    cl = [e.exposure_factor for e in exposures.values() if e.is_class]
    classroom_infection_over_time.add_point(time, {
        'all': sum(cl) / len(cl)
        })

def run_simulation(exposures, people, follow_people):
    people_trace = defaultdict(list)
    for p in range(NUM_PERIODS):
        if p == LUNCH_PERIOD:
            for e in exposures.values():
                e.clean()

        update_graphs(START_TIMES[p], exposures, people)

        sets = get_exposure_sets(people, p)
        for exposure_name, people_exposed in sets.items():
            exposures[exposure_name].calculate_exposure(list(people_exposed))
        for p in follow_people:
            people_trace[p].append((p.exposure[1], p.trace))
    
    last_name_grps = group_by_last_name(people)
    for grp in group_by_last_name(people).values():
        exposures["Last Name"].calculate_exposure(list(grp))
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


def show_graphs(people):
    import matplotlib.pyplot as plt
    import numpy as np

    infection_over_time.show()
    student_inf_over_time.show()
    classroom_infection_over_time.show()

    plt.show()

if __name__ == "__main__":
    population = load_population()
    exposures = initialize_exposures()
    people_trace = run_simulation(exposures, population, [])

    print_results(population)
    show_graphs(population)
    for p in people_trace:
        print(f"    {p.firstname} {p.lastname}'s trace")
        for i in range(NUM_PERIODS):
            print(f"        Time Period {i + 1} | Exposure: {people_trace[p][i][0]}")
            for other in people_trace[p][i][1]:
                print(f"            {other}: {people_trace[p][i][1][other]}")
