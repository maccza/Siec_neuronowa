# from matplotlib.figure import Figure
# from numpy import arange, pi, random, linspace
# import matplotlib.cm as cm
# import multiprocessing
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib
import time


class Chart:
    """
    Klasa do rysowania wynikow przewidywania sieci neuronowej na zbiorze testowym.
    """

    def __init__(self):
        self.fig,self.ax = plt.subplots()
        self.lines = []
        self.init_canvas()
        
    @property
    def return_fig(self):
        return self.fig
    
    def init_canvas(self):
        self.canvas = FigureCanvas(self.fig)
        self.canvas.set_size_request(400, 400)

    @property
    def return_canvas(self):
        return self.canvas

    def plot_dataset(self, x, y, name):
        self.lines.append(self.ax.plot(x, y, label=name))
        # time.sleep(10)
        # self.lines[0].remove()
        # self.ax.draw()
        self.ax.legend()
    
    def clear_chart(self):
        for line in self.lines:
            self.ax.lines.remove(*line)
        self.lines = None
        self.lines = []
        self.ax.legend().remove()
