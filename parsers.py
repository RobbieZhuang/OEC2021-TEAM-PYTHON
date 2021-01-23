import pandas as pd
import numpy as np
import os
from person import Person


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
        ecs = None
        if row["Extracurricular Activities"] is not None:
            ecs = row["Extracurricular Activities"].split(",")
        student = Person(
            Person.Occupation.Student,
            row["Student Number"],
            row["First Name"],
            row["Last Name"],
            row["Grade"],
            classes,
            health_conditions=row["Health Conditions"],
            ecs=ecs,
        )
        students.append(student)
    return students

def get_teachers(filename="/tests/teachers.csv"):
    df = read_from_csv(filename)
    teachers = []
    grade = -1
    for idx, row in df.iterrows():
        classes = [row["Class"]]
        teach = Person(
            Person.Occupation.Teacher,
            row["Teacher Number"],
            row["First Name"],
            row["Last Name"],
            grade,
            classes
        )
        teachers.append(teach)
    return teachers

def get_infects(filename="/tests/infects.csv"):
    df = read_from_csv(filename)
    infects = []
    grade = -1
    for idx, row in df.iterrows():
        infected = Person(
            Person.Occupation.Student,
            row["Student ID"],
            row["First Name"],
            row["Last Name"],
            -1,
            []
        )
        infects.append(infected)
    return infects

def get_tas(filename="/tests/tas.csv"):
    df = read_from_csv(filename)
    tas = []
    grade = -1
    for idx, row in df.iterrows():
        classes = get_classes(row)
        ta = Person(
            Person.Occupation.TA,
            -1,
            row["First Name"],
            row["Last Name"],
            -1,
            classes
        )
        tas.append(ta)
    return tas


if __name__ == "__main__":
    print(get_tas()[0])
