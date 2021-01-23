from constants import *
from exposure import ExposureChance
from collections import defaultdict
import parsers
import pygame
import random
import math

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

# def get_class_set(class_, period, students):
#     class_set = []
#     for s in students:
#         if class_ in s.schedule[period]:
#             class_set.append(s)
#
# def get_class_sets_for_period(period, students):
#     period_set = {}
#     for c in CLASSES:
#         period_set[c] = get_class_set(c, period, students)
#     for ec in ECS:
#         period_set[ec] = get_class_set(ec, period, students)

def get_exposure_sets(exposures, people, period):
    sets = defaultdict(set)
    for p in people:
        if period >= len(p.schedule):
            continue
        for e in p.schedule[period]:
            sets[e].add(p)
    return sets

def clear_screen(screen):
    screen.fill((255, 255, 255))

def init_ui(screen):
    clear_screen(screen)

def get_class_locations():
    class_locations = {}
    total_classes = len(CLASSES)
    classrooms_per_row = math.sqrt(total_classes)
    for i in range(0, total_classes):
        class_locations[CLASSES[i]] = [int(WINDOW_SIZE/classrooms_per_row) * (i % classrooms_per_row) + 100, int(i / classrooms_per_row) * 100 + 50]

    # TODO: Add club location
    class_locations["Clubs"] = [500, 700]

    return class_locations

def draw_rooms(class_locations, screen):
    for key in class_locations:
        font = pygame.font.Font(None, 22)
        text = font.render(key, True, (0, 0, 0))
        text_rect = text.get_rect(center=class_locations[key])
        screen.blit(text, text_rect)

def distance(d_x, d_y):
    return math.sqrt(d_x ** 2 + d_y ** 2)

# Returns where the person should move to next
def get_next_location(cur_location, final_location):
    d_x = final_location[0] - cur_location[0]
    d_y = final_location[1] - cur_location[1]
    hyp = distance(d_x, d_y)

    if hyp > SPEED:
        ratio = SPEED/hyp
        return [cur_location[0] + d_x * ratio, cur_location[1] + d_y * ratio]
    else:
        return final_location

def draw(location, class_locations, screen):
    # Clear the screen
    clear_screen(screen)

    # Draw and add room label text
    draw_rooms(class_locations, screen)

    # Draw a dot for a person
    pygame.draw.circle(screen, (0, 0, 255), location, 5)

    # Render
    pygame.display.flip()

def animate(population, cur_period, class_locations, screen):
    should_continue_drawing = True
    while should_continue_drawing:
        should_continue_drawing = False
        for p in population:
            if cur_period < len(p.schedule):
                if p.schedule[cur_period] and p.schedule[cur_period][0] in class_locations:
                    next_loc = class_locations[p.schedule[cur_period][0]]
                    p.location_in_ui = get_next_location(p.location_in_ui, next_loc)
                    if p.location_in_ui != next_loc:
                        should_continue_drawing = True
            draw(p.location_in_ui, class_locations, screen)
    print(population[0].location_in_ui)

    # Transition students to the new room in the given period

def run_simulation(exposures, people):
    if VISUALIZATIONS_ENABLED:
        pygame.init()

        screen = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])

        init_ui(screen)
        class_locations = get_class_locations()

        sim_running = True
        while sim_running:

            for p in range(NUM_PERIODS):
                sets = get_exposure_sets(exposures, people, p)
                for exposure_name, people_exposed in sets.items():
                    exposures[exposure_name].calculate_exposure(list(people_exposed))

                ### Graphics rendering
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sim_running = False

                animate(population, p, class_locations, screen)

        pygame.quit()
    else:
        for p in range(NUM_PERIODS):
            sets = get_exposure_sets(exposures, people, p)
            for exposure_name, people_exposed in sets.items():
                exposures[exposure_name].calculate_exposure(list(people_exposed))

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
        print('%030s: %5.2f' % (p.firstname + ' ' + p.lastname, 100 * p.exposure[1]))

if __name__ == "__main__":
    population = load_population()
    exposures = initialize_exposures()
    run_simulation(exposures, population)

    print_results(population)
