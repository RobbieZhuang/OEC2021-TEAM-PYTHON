from enum import Enum


class Person:
    class Occupation(Enum):
        Student = 0
        Teacher = 1
        TA = 2

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
    ):
        self.occupation = occupation
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade
        self.schedule = schedule
        self.health_conditions = health_conditions
        self.ecs = ecs

    def __str__(self):
        return "Id-{}, Ou-{}, Na-{} {}, Gr-{}. Sch-{}, He-{}, Ecs-{}".format(
            self.id,
            self.occupation,
            self.firstname,
            self.lastname,
            self.grade,
            self.schedule,
            self.health_conditions,
            self.ecs,
        )
