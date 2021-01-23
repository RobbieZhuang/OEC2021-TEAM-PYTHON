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
    ):
        self.occupation = occupation
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.schedule = schedule
        self.health_conditions = health_conditions
        self.ecs = ecs

        # Previous, current exposure
        self.exposure = (initial_exposure, initial_exposure)

        if occupation == Occupation.Student:
            self.age = grade + 5
        elif occupation == Occupation.Teacher:
            self.age = AVERAGE_TEACHER_AGE
        elif occupation == Occupation.TA:
            self.age = AVERAGE_TA_AGE

        health_exposure_factor = 1.7 if self.health_conditions else 1.0
        self.exposure_factor = (
            BASELINE_EXPOSURE_FACTOR * health_exposure_factor * (1 + (self.age / 4))
        )

    def __str__(self):
        return "Id-{}, Ou-{}, Na-{} {}, Age-{}. Sch-{}, He-{}, Ecs-{}, Inf-{}".format(
            self.id,
            self.occupation,
            self.firstname,
            self.lastname,
            self.age,
            self.schedule,
            self.health_conditions,
            self.ecs,
            self.exposure,
        )

    def expose(self, exposure):
        self.exposure[1] += (1 - self.exposure[1]) * exposure * self.exposure_factor
        self.exposure[1] = min(self.exposure[1], 1.0)

    def next_class(self):
        self.exposure[0] = self.exposure[1]

    def get_exposure(self):
        return self.exposure[0]

    def __hash__(self):
        return hash(tuple(self.id, self.firstname, self.lastname))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                self.id == other.id
                and self.firstname == other.firstname
                and self.lastname == other.lastname
            )
        return False
