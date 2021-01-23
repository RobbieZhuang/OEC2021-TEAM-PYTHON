import pandas as pd
import numpy as np
import os 


def read_from_csv(filename):
    ir_path = os.path.dirname(os.path.realpath(__file__))
    return pd.read_csv(ir_path + filename)

if __name__ == "__main__":
    print(read_from_csv("/tests/students.csv"))