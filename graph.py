from collections import defaultdict
import matplotlib.pyplot as plt

class Series():
    def __init__(self):
        self.x = []
        self.y = []

class Graph():
    def __init__(self, name):
        self.name = name

        self.data = defaultdict(Series)

    def add_point(self, x, ys):
        for name, y in ys.items():
            self.data[name].x.append(x)
            self.data[name].y.append(y)

    # display graph on screen
    def show(self):
        plt.figure()
        plt.title(self.name)
        for name, series in self.data.items():
            plt.plot(series.x, series.y, label=name)
        plt.legend()
