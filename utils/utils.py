# -*- coding: utf-8 -*-
#
# - utils -
#
# All utils functions to work arround tests on words.
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

import re
from . import constants


def startswith_n_consonant(word, nb_consonant):
    """Check if the word start swith n consonant

    :param word: The word to check
    :type word: str
    :param nb_consonant: The number of consonant to check
    :type nb_consonant: int
    :raises ValueError: If the number of consonant is > to the length of the word
    :return: False if the word doesn't starts with n consonant, else True
    :rtype: bool
    """
    return _startswith_n(
        word=word, nb=nb_consonant, characters=constants.VOWEL
    )


def startswith_n_vowel(word, nb_vowel):
    """Check if the word start swith n vowel

    :param word: The word to check
    :type word: str
    :param nb_vowel: The number of vowel to check
    :type nb_vowel: int
    :raises ValueError: If the number of vowel is > to the length of the word
    :return: False if the word doesn't starts with n vowel, else True
    :rtype: bool
    """
    return _startswith_n(
        word=word, nb=nb_vowel, characters=constants.CONSONANT
    )


def _startswith_n(word, nb, characters):
    word_length = len(word)
    if nb > word_length:
        raise ValueError("nb > word length")
    for char in word[0:nb]:
        if char in characters:
            return False
    return True


def contains_n_successive_consonant(word, nb_consonant):
    """Check if the word has n successive consonant

    :param word: The word to check
    :type word: str
    :param nb_consonant: The number of consonant to check
    :type nb_consonant: int
    :return: True if the word has n successive consonant, else False
    :rtype: bool
    """
    return _contains_n_successive(
        word=word, nb=nb_consonant, characters=constants.CONSONANT
    )


def contains_n_successive_vowel(word, nb_vowel):
    """Check if the word has n successive vowel

    :param word: The word to check
    :type word: str
    :param nb_vowel: The number of consonant to check
    :type nb_vowel: int
    :return: True if the word has n successive vowel, else False
    :rtype: bool
    """
    return _contains_n_successive(
        word=word, nb=nb_vowel, characters=constants.VOWEL
    )


def _contains_n_successive(word, nb, characters):
    successives = re.split(rf"{characters}+", word)
    for successive in successives:
        if len(successive) >= nb:
            return True
    return False
