# from matplotlib.figure import Figure
# from numpy import arange, pi, random, linspace
# import matplotlib.cm as cm
# import multiprocessing
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib
class Chart:

    def __init__(self):
        self.fig,self.ax  = plt.subplots()

        self.init_canvas()
        
    @property
    def return_fig(self):
        return self.fig
    
    def init_canvas(self):
        print("nie rozumiem")
        self.canvas = FigureCanvas(self.fig)
        self.canvas.set_size_request(400,400)

    @property
    def return_canvas(self):
        return self.canvas

    
    def plot_dataset(self,x,y,name):
        self.ax.plot(x,y,label=name)
        # self.ax.draw()
        
        self.ax.legend()
       
        