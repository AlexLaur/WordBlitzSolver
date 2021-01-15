[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Python 3.8.x](https://img.shields.io/badge/python-3.8.x-blue.svg)](https://www.python.org/downloads/release/python-380/)
# Word Blitz Solver
***

Can automatically solve a word blitz game. To run the program execute the following command.

## Installation
1. You will need a install of python3.x.
2. Download this source code by cloning the master branch, or downloading.
3. Install all the python dependencies by running ```pip install -r requirements.txt```

### Installation using virtualenv
If you want to keep your python install independent of any dependencies in this project, you can install a virtual environment.
1. Go to the directory of this project.
2. Create virtual environment by running```virtualenv venv```.
3. Activate the virtual environment by running ```venv/Scripts/activate``` on Windows or ```source venv/bin/activate``` on Unix.
4. Once inside the virtual environment, run step 3 in installation.

## Informations
This script is designed for a game on a 1920*1080 screen.
If you need to change, go to [networkx_functions#L53](https://github.com/AlexLaur/word_blitz_solver/blob/137de13c3621e99b6f43f0958212d1c2ced509e0/libs/networkx_functions.py#L53) and change the value of the offset.
## Running
```python word_blitz_view```

## How it works
To find words, We construct a graph (each node represent a chars with its position on the screen).
Then, we walk recurssivelly inside the graph in order to find words.

## TODO
1. Add a timer or detect the end of the game in order to stop the solver.
2. Auto chars detection, using opencv and tesseract or something like that.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
