from constants import *

class ExposureChance:

    def __init__(self, name, exposure_factor, is_class=True):
        self.name = name
        self.exposure_factor = exposure_factor
        self.is_class=is_class

    def calculate_exposure(self, people):
        # Update incubation period for each person
        for p in people:
            if is_class:
                p.next_class()
        
        # Perform pairwise exposure calculations between people
        for i in range(len(people)):
            for j in range(len(people)):
                if i != j:
                    people[j].expose(
                        people[i].get_exposure() * \
                        self.exposure_factor * \
                        (R_0 / len(people)) * \
                        OCCUPATIONAL_EXPOSURE_MATRIX[people[i].occupation][people[j].occupation]
                        )
