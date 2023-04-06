import json
import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt
from draw_plots import Plots # import class Plots

class TestPlots(unittest.TestCase): # create test plot class using unittest
    def setUp(self):
        self.plot_out = Plots()
        self.test_json_file = 'deviation.json' # json file for unittest
        self.paths = self.plot_out.draw_plots(self.test_json_file)

    def pathRemove(self):
        for path in self.paths:
            os.remove(path) # remove path

    def test_draw_plots(self):
        self.assertTrue(os.path.exists('plots/plot1.png'))
        self.assertTrue(os.path.exists('plots/plot2.png'))

    def test_return_type(self): # assertIsInstance returning data
        self.assertIsInstance(self.paths, list)
        for path in self.paths:
            self.assertIsInstance(path, str)

    def test_plot_contents(self): # load data from json into df for data response to plot
        with open(self.test_json_file, 'r') as f:
            data = json.load(f)
        df = pd.DataFrame.from_dict(data) # data Dataframe read

        # Check that the first plot has the correct data
        fig, ax = plt.subplots()
        ax.plot(df['mean'], df['ceiling_mean']) # columns
        expected_path = 'plots/plot1.png' # plot path
        actual_path = self.paths[0] # index
        self.assertTrue(os.path.exists(expected_path))
        self.assertTrue(os.path.exists(actual_path))
        self.assertEqual(open(expected_path, 'rb').read(), open(actual_path, 'rb').read()) # read data

        # Check that the second plot has the correct data
        fig, ax = plt.subplots()
        ax.plot(df['floor_min'], df['floor_max']) # columns
        expected_path = 'plots/plot2.png' # plot path
        actual_path = self.paths[1] # index
        self.assertTrue(os.path.exists(expected_path))
        self.assertTrue(os.path.exists(actual_path))
        self.assertEqual(open(expected_path, 'rb').read(), open(actual_path, 'rb').read()) # read data
