# -*- coding: utf-8 -*-
#
# - tracer -
#
# Tracer module to work with the mouse. Just call the trace method with the path
# of nodes to construct the word.
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

import time
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0


class Tracer(object):
    def __init__(self):
        self.delay_ms = 40
        self.graph = None

    def set_graph(self, graph):
        """Set the current graph in the Tracer

        :param graph: The graph from the game
        :type graph: nx.Graph
        """
        self.graph = graph

    def trace(self, sequence):
        """Trace the word on the screen

        :param sequence: The sequence of the word which correspond of the path
        with nodes to construct the word.
        :type sequence: list
        """
        for index, step in enumerate(sequence):
            x = self.graph.nodes[step]["x"]
            y = self.graph.nodes[step]["y"]
            pyautogui.moveTo(x, y)
            if index == 0:
                pyautogui.mouseDown()
            time.sleep(self.delay_ms / 1000)
        pyautogui.mouseUp()
