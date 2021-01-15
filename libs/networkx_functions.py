# -*- coding: utf-8 -*-
#
# - networdx_functions -
#
# This module is a collection of functions to work arround the graph.
# It use the module networkX in order to have a very strong base for our solver.
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

import networkx as nx

from utils import constants


def build_graph(grid):
    """Build the graph from the the grid of characters

    :param grid: grid with characters
    :type grid: list
    :return: The graph with characters
    :rtype: nx.Graph
    """
    G = nx.grid_2d_graph(4, 4)

    G.add_edges_from(
        [((x, y), (x + 1, y + 1)) for x in range(3) for y in range(3)]
        + [((x + 1, y), (x, y + 1)) for x in range(3) for y in range(3)]
    )

    for x, row in enumerate(grid):
        for y, character in enumerate(row):
            char_type = 0 if character in constants.CONSONANT else 1
            G.nodes[(x, y)]["character"] = character
            G.nodes[(x, y)]["type"] = char_type

    for node in G.nodes:
        G.nodes[node]["x"] = node[1] * 100 + 800
        G.nodes[node]["y"] = node[0] * 100 + 512

    return G


def get_character_node(graph, character, only_one=False):
    """Return nodes for the given character

    :param graph: The graph
    :type graph: nx.Graph
    :param character: The character
    :type character: str
    :param only_one: boolean in order to return one node or all found nodes,
    defaults to False
    :type only_one: bool, optional
    :return: List of nodes if only_one is set to False, else tuple
    :rtype: list or tuple
    """
    found = []
    for node, data in graph.nodes(data=True):
        if data["character"] != character:
            continue
        found.append(node)
    if only_one:
        return found[0] if found else found
    return found


def get_neighbors(graph, node):
    """Return all neighbors for the given node in the graph

    :param graph: The given graph
    :type graph: nx.Graph
    :param node: The node to analyse
    :type node: tuple
    :return: List of all neighbors
    :rtype: list
    """
    return graph.neighbors(node)
