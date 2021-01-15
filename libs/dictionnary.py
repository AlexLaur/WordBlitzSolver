# -*- coding: utf-8 -*-
#
# - dictionnary -
#
# The Dictionnary object represent all possible words.
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

from utils import in_out


class Dictionnary(object):
    def __init__(self, path):
        # Group all words by the first letter
        self._grouped_words = {}
        self.grouped_words = {}
        # Group all words by the first 5 characters
        self._grouped_chars = {}
        self.grouped_chars = {}

        # Read the dictionnary and load all words
        self.all_words = in_out.read_dicationnary(path=path)
        self._strip_words()

        # Grouping elements by the first letter
        self.grouping_words()
        self.grouping_chars()

    def _strip_words(self):
        """Remove the "\n" in the end of each words"""
        self.all_words = [word.strip() for word in self.all_words]

    def grouping_words(self):
        """Group all words by the first character

        :return: The dictionnary of grouped words
        :rtype: dict
        """
        self._grouped_words = {}
        for word in self.all_words:
            first_char = word[0]
            if first_char not in self._grouped_words:
                self._grouped_words[first_char] = []
            self._grouped_words[first_char].append(word)
        return self._grouped_words

    def refine_words(self, characters):
        """Refine all words with available characters

        :param characters: List of available characters in the grid of the game
        :type characters: list
        :return: The dictionnary refined
        :rtype: dict
        """
        self.grouped_words = self._grouped_words.copy()
        self.grouped_chars = self._grouped_chars.copy()
        for key in self._grouped_words.keys():
            if key in characters:
                continue
            self.grouped_words.pop(key, None)
            self.grouped_chars.pop(key, None)
        return self.grouped_words, self.grouped_chars

    def grouping_chars(self):
        """Group all words by first 5 chars. Then, put all in a list and group
        by the first chars. This is usefull to improve the time in the solver.

        :return: dictionnary. Key are the first letter, values are a list with
        all possibilities with 5 first chars.
        :rtype: dict
        """
        self._grouped_chars = {}
        for key, value in self._grouped_words.items():
            self._grouped_chars[key] = []
            for word in value:
                chars = word
                if len(word) >= 5:
                    chars = word[0:5]
                self._grouped_chars[key].append(chars)
        return self._grouped_chars
