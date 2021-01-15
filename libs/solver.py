# -*- coding: utf-8 -*-
#
# - solver -
#
# Solver module. This module is in charge of find all possible words.
# To do that, we simply walk through the graph and add each chars to each other.
# If the word is in the dictionnary, we have found a word. So, emit a signal
# with the word dans the path to contruct the word.
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

from PySide2 import QtGui, QtCore, QtWidgets

from libs.event_handler import EventHandler
from libs import networkx_functions as nxf
from utils import utils


class Solver(QtCore.QThread):
    def __init__(self, parent=None):
        super(Solver, self).__init__(parent=parent)

        # Signal
        self.signal = EventHandler()

    def solver(self, graph, node, words_dictionnary):
        """public method for the solver

        :param graph: The graph
        :type graph: nx.Graph
        :param node: The node as a starting point
        :type node: tuple
        :param words_dictionnary: Word Dictionnary object
        :type words_dictionnary: object
        """
        self._solver(
            graph=graph,
            node=node,
            visited=[],
            words_dictionnary=words_dictionnary,
        )

    def _solver(
        self, graph, node, words_dictionnary, visited=None, word="", depth=0
    ):
        """Private method for the solver, this method is recurssive.
        If the depth is 16. We stop the recurssion (this should never happened).
        The visited variable is a list on which we happen the current node in
        order to never go again on this node. Moreover, this variable represent
        the path in order to find the word on the graph.


        :param graph: The graph to walk inside
        :type graph: nx.Graph
        :param node: The node as starting point
        :type node: tuple
        :param words_dictionnary: The word dictionnary object
        :type words_dictionnary: object
        :param visited: All node visited, defaults to None
        :type visited: list, optional
        :param word: The current word found, defaults to ""
        :type word: str, optional
        :param depth: The depth in the recurssion, defaults to 0
        :type depth: int, optional
        """
        visited.append(node)
        word += graph.nodes[node]["character"]
        if len(word) >= 3:
            if utils.contains_n_successive_consonant(
                word=word, nb_consonant=3
            ):
                return
            elif utils.contains_n_successive_vowel(word=word, nb_vowel=4):
                return
        if len(word) >= 5:
            if word[0:5] not in words_dictionnary.grouped_chars[word[0]]:
                return
        if word in words_dictionnary.grouped_words[word[0]]:
            result = {"word": word, "path": visited}
            self.signal.sig_word_found.emit(result)

        for neighbor in nxf.get_neighbors(graph=graph, node=node):
            if neighbor in visited:
                continue
            if depth < 16:
                self._solver(
                    graph=graph,
                    node=neighbor,
                    words_dictionnary=words_dictionnary,
                    visited=visited,
                    word=word,
                    depth=depth + 1,
                )
            visited.remove(neighbor)

    def run(self, graph, words_dictionnary):
        for node in graph.nodes():
            self.solver(
                graph=graph, node=node, words_dictionnary=words_dictionnary
            )
