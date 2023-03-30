import pandas as pd  # import pandas and matplotlib
import os
import matplotlib.pyplot as plt


class Plots:  # create class for plots
    def __init__(self):
        self.figure, self.axis1 = plt.subplots()  # constructor

    def plot(self, x, y, label):
        self.axis1.plot(x, y, label=label)

    def set_title(self, title):  # setters
        self.axis1.set_title(title)

    def set_x_label(self, x_label):
        self.axis1.set_xlabel(x_label)

    def set_y_label(self, y_label):
        self.axis1.set_ylabel(y_label)

    def legend(self):
        self.axis1.legend()  # legend info plot

    def save_fig(self, filepath):  # save figure
        self.figure.savefig(filepath)


def draw_plots(json_file):
    df = pd.read_json(json_file)  # parameter json from jupyter path and using pandas for read file

    if not os.path.exists('plots'):
        os.makedirs('plots')  # create folder "plots"

    plot_compare = Plots()  # Initialize the plotCompare from class

    for col in df.columns:
        plot_compare.plot(df.index, df[col], label=col)  # comparing each plot using loop columns

    plot_compare.set_title('Comparison Columns')
    plot_compare.set_x_label('Indexes from deviations')  # titles
    plot_compare.set_y_label('General value comparing')
    plot_compare.legend()

    filepath = os.path.join('plots', 'testPlot.png')  # using join for all plots to filepath
    plot_compare.save_fig(filepath)  # saving plot

    return filepath  # return the path to the plot
