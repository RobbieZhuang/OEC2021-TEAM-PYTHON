from collections import defaultdict
from constants import *


class Person:
    def __init__(
        self,
        occupation: Occupation,
        id,
        firstname: str,
        lastname: str,
        grade,
        schedule,
        health_conditions=None,
        ecs=None,
        initial_exposure=0.0,
        location_in_ui=[500, -10],
    ):
        self.occupation = occupation
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.schedule = schedule
        self.health_conditions = health_conditions
        self.ecs = ecs
        self.grade = grade

        # Previous, current exposure
        self.exposure = (initial_exposure, initial_exposure)

        health_exposure_factor = 1.7 if self.health_conditions else 1.0
        age_exposure_factor = 1.0 if grade is None else 1.0 + ((grade - 9) / 4.0)
        self.exposure_factor = (
            BASELINE_EXPOSURE_FACTOR * health_exposure_factor * age_exposure_factor
        )
        self.trace = defaultdict(int)

        self.location_in_ui = location_in_ui

    def __str__(self):
        return "Id-{}, Ou-{}, Na-{} {}, Gr-{}. Sch-{}, He-{}, Ecs-{}, Inf-{}".format(
            self.id,
            self.occupation,
            self.firstname,
            self.lastname,
            self.grade,
            self.schedule,
            self.health_conditions,
            self.ecs,
            self.exposure,
        )

    def expose(self, exposure, person=""):
        old = self.exposure[1]
        self.exposure = (
            self.exposure[0],
            min(
                1.0,
                self.exposure[1]
                + (1 - self.exposure[1]) * exposure * self.exposure_factor,
            ),
        )
        if (self.exposure[1] - old) > 0.00001:
            self.trace[person] += (self.exposure[1] - old)
        return self.exposure[1] - old

    def next_class(self):
        self.trace = defaultdict(int)
        self.exposure = (self.exposure[1], self.exposure[1])

    def get_exposure(self):
        return self.exposure[0]

    def __hash__(self):
        return hash((self.id, self.firstname, self.lastname))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                self.id == other.id
                and self.firstname == other.firstname
                and self.lastname == other.lastname
            )
        return False
