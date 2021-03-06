# Utility functions to parse CSV files and return representations of students/teachers/tas used in the program

import pandas as pd
import numpy as np
import os
from person import Person
from constants import *


# Reads a CSV into a pandas DataFrame
def read_from_csv(filename):
    ir_path = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(ir_path + '/' + filename)
    return df.where(pd.notnull(df), None)


# Returns a list class string identifiers
def get_classes(dfrow, periods=4):
    classes = []
    for period in range(1, periods + 1):
        classes.append(dfrow["Period {} Class".format(period)])
    return classes


# Parses a CSV of students and returns the object representation
def get_students(filename="tests/students.csv"):
    df = read_from_csv(filename)
    students = []
    # Iterate over pandas dataframe
    for idx, row in df.iterrows():
        classes = get_classes(row)
        schedule = []

        classes.insert(2, f'Gr {row["Grade"]} Lunch')

        for i in range(len(classes)):
            transition = []
            if i > 0:
                transition.append(f"{classes[i - 1]} Transition")
            transition.append(f"{classes[i]} Transition")
            schedule.append(transition)

            schedule.append([classes[i]])

            if i == len(classes) - 1:
                schedule.append([f"{classes[i]} Transition"])

        # Fetch the ECs, split by comma
        ecs = None
        if row["Extracurricular Activities"] is not None:
            ecs = row["Extracurricular Activities"].split(",")
        if ecs and len(ecs) > 1:
            ecs = [ecs[0]]

        if ecs:
            for ec in ecs:
                schedule[-1].append(f"{ec} Transition")
            schedule.append(ecs)
            schedule.append([ec + " Transition" for ec in ecs])

        # Create object
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


# Parses a CSV of teachers and returns the object representation
def get_teachers(filename="tests/teachers.csv"):
    df = read_from_csv(filename)
    teachers = []
    for idx, row in df.iterrows():
        cl = row["Class"]

        schedule = [[]]
        for i in range(5):
            # Teachers always teach the same class every period
            schedule.append([cl])

            # Teachers don't transition
            schedule.append([])

        # Create the teacher object
        teach = Person(
            Occupation.Teacher,
            row["Teacher Number"],
            row["First Name"],
            row["Last Name"],
            None,
            schedule,
        )
        teachers.append(teach)
    return teachers


# Parses a CSV of infected people and returns the object representation
def get_infects(filename="tests/infects.csv"):
    df = read_from_csv(filename)
    infects = []
    for idx, row in df.iterrows():
        student_id = row["Student ID"]
        infected = Person(
            Occupation.TA, student_id, row["First Name"], row["Last Name"], None, []
        )
        infects.append(infected)
    return infects


# Parses a CSV of TAs and returns the object representation
def get_tas(filename="tests/tas.csv"):
    df = read_from_csv(filename)
    tas = []
    for idx, row in df.iterrows():
        classes = get_classes(row)
        schedule = []

        classes.insert(2, f"TA Lunch")

        for i in range(len(classes)):
            transition = []
            if i > 0:
                transition.append(f"{classes[i - 1]} Transition")
            transition.append(f"{classes[i]} Transition")
            schedule.append(transition)

            schedule.append([classes[i]])

            if i == len(classes) - 1:
                schedule.append([f"{classes[i]} Transition"])

        # Create the TA object
        ta = Person(
            Occupation.TA, None, row["First Name"], row["Last Name"], None, schedule
        )
        tas.append(ta)
    return tas


# Debugging
if __name__ == "__main__":
    print(get_tas()[0])
    print(get_students()[0])
