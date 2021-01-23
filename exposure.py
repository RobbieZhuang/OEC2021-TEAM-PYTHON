from constants import *

class ExposureChance:
    def __init__(self, name, exposure_factor, is_class=True):
        self.name = name
        self.base_exposure_factor = exposure_factor
        self.exposure_factor = exposure_factor
        self.is_class = is_class

    def calculate_exposure(self, people):
        # Update incubation period for each person
        for p in people:
            if self.is_class:
                p.next_class()
        
        exposure = 0.0

        # Perform pairwise exposure calculations between people
        for i in range(len(people)):
            for j in range(len(people)):
                if i != j:
                    exposure += people[j].expose(
                        people[i].get_exposure()
                        * self.exposure_factor
                        * (R_0 / len(people))
                        * OCCUPATIONAL_EXPOSURE_MATRIX[people[i].occupation][
                            people[j].occupation
                        ],
                        f"{people[i].firstname} {people[i].lastname}"
                    )
        
        if self.is_class:
            # Approximate room exposure by taking average exposure of population and dividing by 2
            room_exposure = sum([p.get_exposure() for p in people]) / len(people)
            self.exposure_factor *= 1.0 + room_exposure / 2.0

        # if exposure > 1.0:
        #     print(f"OUTBREAK in {self.name}")

    def clean(self):
        self.exposure_factor = self.base_exposure_factor
