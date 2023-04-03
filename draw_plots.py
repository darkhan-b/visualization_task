import os
import pandas as pd
import matplotlib.pyplot as plt


class Plots:
    def draw_plots(self, file):
        df = pd.read_json(file) # read json file
        os.makedirs('plots', exist_ok=True) # create directory for plots
        paths_return = [] # list of plots


        fig, ax = plt.subplots() # draw plots
        ax.plot(df['min'], df['max']) # columns max and min
        plt.savefig('plots/plot1.png')
        paths_return.append('plots/plot1.png')

        fig, ax = plt.subplots()
        ax.plot(df['gt_corners'], df['rb_corners']) # columnts gt_corners and rb coreners
        plt.savefig('plots/plot2.png') #savefig from class
        paths_return.append('plots/plot2.png')

        return paths_return # return to Jupyter output