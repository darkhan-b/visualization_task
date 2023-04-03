# Visualization task instructions 
Project for task DA junior

!!! The solution differs from the first solution, due to the fact that I could not adapt my image to the tests, since he could not check the list values and there was nothing to return to him. To do this, I created a class that has an empty array and can generate more (to do this, you need to update the generation of new images with different columns for variety)!!!
* How to launch application in terminal
* How to launch unit tests

1. Clone this repository in your desktop and start
```
git clone https://github.com/darkhan-b/visualization_task.git
```

2. Install the packages by running the command in terminal:
```
pip install -r requirements.txt
```

3. Main files for project:
- draw_plots.py
- Jupyer.ipynb
- test.py (Unittest)

The main class for creating a drawing is stored in draw_plots.py to run it, we just need to run Jupyter file, where it imports the first file.
Launch Application for output plot...
!!!PLEASE!!! Delete plots directory for generating new plots 
```
jupyter nbconvert --execute --to notebook --inplace Jupyter.ipynb
```

To check unit-tests command (in main directory of project):
```
python -m unittest discover 
```
Should be 3 OK test responses

Done!
