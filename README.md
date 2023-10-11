# Python-Avalanche-Simulation
Avalanche simulation made in Python

Snow Avalanche Simulation
This Python script simulates a snow avalanche using the NumPy and Matplotlib libraries. The avalanche starts with a layer of snow in the center of the grid and moves randomly, accumulating more snow as it progresses.

Table of Contents
Introduction
Installation
Usage
Parameters
License
Introduction
This simulation demonstrates the behavior of a snow avalanche as it moves through a grid, accumulating more snow based on its density and speed. The avalanche starts at a random location and changes direction when it reaches the edge of the grid.

## Installation
To run the simulation, you need to have Python, NumPy, and Matplotlib installed on your system. You can install the required libraries using pip:

bash
pip install numpy matplotlib

## Usage
After installing the required libraries, you can run the simulation by executing the Python script. The avalanche will move, leaving a trail of accumulated snow in its path.

bash
python avalanche_simulation.py

## Parameters
You can modify the behavior of the simulation by adjusting the following parameters in the code:

brzina_kretanja_lavine: Controls the speed of the avalanche.
gustoca_snijega: Defines the density of the snow.
lavina_x and lavina_y: Specify the initial position of the avalanche.
lavina_smjer_x and lavina_smjer_y: Determine the initial direction of the avalanche.

Feel free to experiment with these parameters to observe different avalanche behaviors.
