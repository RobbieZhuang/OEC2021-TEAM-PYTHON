from constants import *

class Person:

    def __init__(
        self,
        occupation: Occupation,
        id: int,
        firstname: str,
        lastname: str,
        grade: int,
        schedule,
        health_conditions=None,
        ecs=None,
        initial_exposure=0.0
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

        self.exposure_factor = PERSONAL_EXPOSURE_FACTORS[occupation] * (1.5 ** (self.age / 2))

    def __str__(self):
        return "Id-{}, Ou-{}, Na-{} {}, Age-{}. Sch-{}, He-{}, Ecs-{}".format(
            self.id,
            self.occupation,
            self.firstname,
            self.lastname,
            self.age,
            self.schedule,
            self.health_conditions,
            self.ecs,
        )

    def expose(self, exposure):
        self.exposure[1] += (1 - self.exposure[1]) * exposure

    def next_class(self):
        self.exposure[0] = self.exposure[1]

    def get_exposure(self):
        return self.exposure[0]
