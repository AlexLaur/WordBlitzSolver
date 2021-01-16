# -*- coding: utf-8 -*-
#
# - word_blitz_view -
#
# The core of the app. Load the UI, load the dictionnary of words.
# Inititalize the game and launch the Thread to find words.
# This script use a graph to build the grid of words and to find all possible
# word.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import time
from PySide2 import QtGui, QtCore, QtWidgets

from ui import word_blitz_solver_ui as main_ui

from libs.dictionnary import Dictionnary
from libs.game import Game
from libs.solver import Solver
from libs.tracer import Tracer

from utils import utils

SCRIPT_PATH = os.path.dirname(__file__)


class WordBlitzSolver(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(WordBlitzSolver, self).__init__(parent=parent)

        self.setupUi(self)

        # Constants
        self.current_game = None
        self.words_found = []
        self.solver = Solver(parent=self)
        self.tracer = Tracer()

        source_file = os.path.join(SCRIPT_PATH, "data", "dictionnary_fr.txt")
        # Init the dictionnary only one time
        self.words_dictionnary = Dictionnary(path=source_file)

        # grid of line edits
        self.grid = [
            getattr(self, "lie_%s" % str(index).zfill(2))
            for index in range(16)
        ]

        # Signals
        self.pub_analyse.clicked.connect(self.analyse)
        self.pub_solve.clicked.connect(self.solve)
        self.solver.signal.sig_word_found.connect(self.trace_word)

    def analyse(self):
        """Analyse the game, and construct the grid."""
        # TODO Need to grab the window and auto detect letters. The variable
        # grid is used for tests.
        # grid from the extractor
        grid = GRID

        # Load all line edits
        count = 0
        for row in grid:
            for item in row:
                self.grid[count].setText(item)
                count += 1

    def solve(self):
        """Solve the game"""
        # Get grid from grid of line edit
        grid = self.get_grid()
        # On each party, init the game
        self.current_game = Game(grid=grid)
        # Reload the grouped_words with the current game
        self.words_dictionnary.refine_words(
            characters=self.current_game.characters
        )
        # Give the graph to the tracer
        self.tracer.set_graph(graph=self.current_game.graph)

        self.start_time = time.time()
        self.words_found = []
        self.solver.run(
            graph=self.current_game.graph,
            words_dictionnary=self.words_dictionnary,
        )

    def get_grid(self):
        """Construct the grid of chars from all line edits.
        e.g :

        >>> [
        ...     ["L", "L", "O", "N"],
        ...     ["T", "A", "D", "L"],
        ...     ["I", "N", "E", "T"],
        ...     ["S", "E", "S", "G"],
        ... ]

        :return: list of list
        :rtype: list
        """
        grid = []
        row = []
        for index, line_edit in enumerate(self.grid):
            if index % 4 == 0 and index != 0:
                grid.append(row)
                row = []
            if index == 15:
                grid.append(row)
            row.append(line_edit.text().upper())
        return grid

    @QtCore.Slot(object)
    def trace_word(self, result):
        """New word found, trace it !

        :param result: The result from the thread.
        :type result: dict
        """
        word = result.get("word", None)
        path = result.get("path", None)
        if word not in self.words_found:
            self.words_found.append(word)
            if (time.time() - self.start_time) <= 60:
                self.tracer.trace(sequence=path)
            else:
                print("time elapsed")
            print(word, path)


if __name__ == "__main__":
    # GRID for demo
    GRID = [
        ["L", "L", "O", "N"],
        ["T", "A", "D", "L"],
        ["I", "N", "E", "T"],
        ["S", "E", "S", "G"],
    ]

    app = QtWidgets.QApplication([])
    widget = WordBlitzSolver()
    widget.show()
    app.exec_()
