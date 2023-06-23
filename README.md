# Cubo Finale

## The project
The designed project is a simple simulator of a 2D Rubik's cube using the Pygame library for visual graphics and controls.

## Features
* Two-dimensional visualization of a 3x3 Rubik's cube using a Pygame screen;
* Keyboard controls for face turns and rotations on the cube;
* Generation of animated solutions based on the layer-by-layer method using an algorithm and the Time library;
* Algorithm control and testing using an Excel spreadsheet and a graph that demonstrates the capabilities of the simulator.

## How to install the project
The program can be downloaded from the GitHub repository and imported into any programming software, it is written in Python and every class is perfectly described in the Italian documentation you can find inside of the repository.

### Module needed for the program:
* Pygame Module for the game's interface development
* Numpy Module used to work with multidimensional array
* Openpyxl Module to open and interact with the excel file
* Matplotlib Module to draw and show the statistics graphs

For the code it's possible to create and use a virtual environment just to isolate and manage dependencies for the project, avoiding interference with other environments or dependencies on the same system. 

### How to create a virtual environment:
To create a virtual environment you have to go on the console of you coding IDE and type the following command:
'python3 -m venv virtual_environment'
Replace virtual environment with the name you want to call the environment you generated.
Remember to use the appropriate Python version (python3) based on your system configuration.

Next you have to start running the environment with the command: 
'virtual _environmnet\Scripts\activate'

Once done you have to install in the virtual environment the modules described before to run the program using the command:
'python3 -m pip install module_name'
Replace module_name with the name of the module to install.
Remember to use the appropriate Python version (python3) based on your system configuration.

In the end it will be possible to run the program using the command:
'python3 -m sorgente.main'
Remember to use the appropriate Python version (python3) based on your system configuration.

## Implementation 

### Structure
Every class in the program is well described in the documentation available in the source of the package. Unfortunately, the documentation is written in Italian since the project was designed for an Italian exam. However, the program itself is also well commented, so we hope that the project will be easily understandable.

### Cube
This program uses a relatively simplistic representation of the Rubik's Cube. We simply consider the cube to be an array of 6 2-dimensional arrays (matrix), each representing a face of the cube. Each element of these 2-dimensional arrays then represents a sticker on the cube.

### Solving
The program implements a simplified variant of the LBL beginner's method. This method closely approximates how a normal beginner solver would solve a cube, although without the aid of human intuition. This approach to solving a cube is substantially less move optimal compared to more sophisticated computer-based algorithms, but was chosen due to ease of implementation and relatively low computation cost.
