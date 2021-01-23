class ExposureChance:

    def __init__(self, name, exposure_factor, is_class=True):
        self.name = name
        self.exposure_factor = exposure_factor
        self.is_class=is_class

    def calculate_exposure(self, people):
        for p in people:
            if is_class:
                p.next_class()

        for i in range(len(people)):
            for j in range(len(people)):
                if i != j:
                    people[i].expose(people[j].get_exposure())
