import pandas as pd
import numpy as np
import os
from person import Person
from constants import *


def read_from_csv(filename):
    ir_path = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(ir_path + filename)
    return df.where(pd.notnull(df), None)


def get_classes(dfrow, periods=4):
        classes = []
        for period in range(1, periods+1):
            classes.append(dfrow["Period {} Class".format(period)])
        return classes

def get_students(filename="/tests/students.csv"):
    df = read_from_csv(filename)
    students = []
    for idx, row in df.iterrows():
        classes = get_classes(row)
        schedule = []

        classes.insert(2, f'Gr {row["Grade"]} Lunch')

        for i in range(len(classes)):
            transition = []
            if i > 0:
                transition.append(f'{classes[i - 1]} Transition')
            transition.append(f'{classes[i]} Transition')
            schedule.append(transition)

            schedule.append([classes[i]])

            if i == len(classes) - 1:
                schedule.append([f'{classes[i]} Transition'])

        ecs = None
        if row["Extracurricular Activities"] is not None:
            ecs = row["Extracurricular Activities"].split(",")

        if ecs:
            for ec in ecs:
                schedule[-1].append(f'{ec} Transition')
            schedule.append(ecs)
            schedule.append([ec + ' Transition' for ec in ecs])

        student = Person(
            Occupation.Student,
            row["Student Number"],
            row["First Name"],
            row["Last Name"],
            row["Grade"],
            schedule,
            health_conditions=row["Health Conditions"],
            ecs=ecs,
        )
        students.append(student)
    return students

def get_teachers(filename="/tests/teachers.csv"):
    df = read_from_csv(filename)
    teachers = []
    for idx, row in df.iterrows():
        classes = [row["Class"]]
        teach = Person(
            Occupation.Teacher,
            row["Teacher Number"],
            row["First Name"],
            row["Last Name"],
            None,
            classes
        )
        teachers.append(teach)
    return teachers

def get_infects(filename="/tests/infects.csv"):
    df = read_from_csv(filename)
    infects = []
    for idx, row in df.iterrows():
        infected = Person(
            Occupation.Student,
            row["Student ID"],
            row["First Name"],
            row["Last Name"],
            None,
            []
        )
        infects.append(infected)
    return infects

def get_tas(filename="/tests/tas.csv"):
    df = read_from_csv(filename)
    tas = []
    for idx, row in df.iterrows():
        classes = get_classes(row)
        ta = Person(
<<<<<<< Updated upstream
            Occupation.TA, -1, row["First Name"], row["Last Name"], -1, classes
=======
            Person.Occupation.TA,
            None,
            row["First Name"],
            row["Last Name"],
            None,
            classes
>>>>>>> Stashed changes
        )
        tas.append(ta)
    return tas


if __name__ == "__main__":
    print(get_tas()[0])
    print(get_students()[0])
