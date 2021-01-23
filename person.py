from enum import Enum

class Person

    class Type(Enum):
        Student = 0
        Teacher = 1
        TA = 2

    def __init__(self, type: Type, id: int, firstname: str, lastname: str,
            grade: int, schedule: list[str], health_conditions=None, ecs=None):
        self.type = type
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade
        self.schedule = schedule
        self.health_conditions = health_conditions
        self.ecs = ecs

