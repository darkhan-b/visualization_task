import os
import pandas as pd
import matplotlib.pyplot as plt


class Plots:
    def draw_plots(self, file):
        df = pd.read_json(file) # read json file
        os.makedirs('plots', exist_ok=True) # create directory for plots
        paths_return = [] # list of plots

        # fig, ax = plt.subplots() # draw plots
        # ax.bar(df['min'], df['max']) # columns max and min
        # plt.xlabel('Sample')
        # plt.ylabel('Number of corners')
        # plt.title('Number of Corners Comparison')
        # plt.savefig('plots/plot1.png')
        # paths_return.append('plots/plot1.png')

        # first_five_names = df['name'].head(5).values.tolist()
        # filtered_df = df[df['name'].isin(first_five_names)]
        #
        # plt.figure(figsize=(10, 5))
        # plt.bar(filtered_df['name'], filtered_df['gt_corners'], label="Truth number", color='blue')
        # plt.bar(filtered_df['name'], filtered_df['rb_corners'], label="Corners by model", color='orange')
        # plt.xlabel('Name')
        # plt.ylabel('Difference of GT corners and number of RB corners')
        # plt.title('Comparison corners first 5 people')
        # plt.savefig('plots/plot1.png')
        # paths_return.append('plots/plot1.png')


        # first plot
        names = df['name'][:5] # first 5 rows bty names
        col1 = df['mean'][:5] # first 5
        col2 = df['ceiling_mean'][:5] # first 5
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(13, 5)) # two bar plots in one

        # First bar chart
        axs[0].bar(names, col1, color ='orange')
        axs[0].set_xlabel('Name') # x label
        axs[0].set_ylabel('Mean') # y label
        axs[0].set_title('General mean')
        axs[0].set_yticks(range(0, 50, 5)) # tick by 5
        # Second bar chart
        axs[1].bar(names, col2)
        axs[1].set_xlabel('Name')
        axs[1].set_ylabel('Ceiling mean') # diff between ceiling mean and general
        axs[1].set_title('Ceiling mean')
        axs[0].set_yticks(range(0, 50, 10))
        plt.suptitle('Comparison between mean and ceiling mean for first 5 people') # main title
        plt.savefig('plots/plot1.png')
        paths_return.append('plots/plot1.png')


        # second plot
        df = df.head()
        plt.figure(figsize=(10, 5)) # size plot
        plt.plot(df['name'], df['floor_min'], label='Floor Min') # col1 min
        plt.plot(df['name'], df['floor_max'], label='Floor Max') # col2 max
        plt.xlabel('Name')
        plt.ylabel('Min and Max') # diff between max and min (floor)
        plt.yticks(range(0, 20, 2)) # tick by 2
        plt.title('Comparison of floors (Min and Max) for first 5 people') # title
        plt.legend()
        plt.savefig('plots/plot2.png')
        paths_return.append('plots/plot2.png')



        return paths_return # return to Jupyter output