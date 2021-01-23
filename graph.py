from collections import defaultdict

class Graph():
    def __init__(self, name):
        self.name = name

        #self.data = defaultdict(
        self.x = []
        self.y = []

    def add_point(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def show(

