# -*- coding: utf-8 -*-
#
# - game -
#
# Game objects is an instance of a party. Each party need to be initialized
# with the Game object.
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

from . import networkx_functions as nxf


class Game(object):
    def __init__(self, grid):
        # Constants
        self.characters = []

        self.grid = grid
        self.graph = nxf.build_graph(grid=grid)
        self._characters()

    def _characters(self):
        """Returns all characters of the current game

        :return: list of chars
        :rtype: list
        """
        self.characters = list(
            set([item for sublist in self.grid for item in sublist])
        )
        return self.characters
