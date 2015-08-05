# encoding: utf-8

"""
Some constants of morse

release |release|, version |version|

.. versionadded:: 1.0

    Initial

Contents
--------

Classes:

Functions:

Variables:

* :data:`MORSE_NUMERIC`
* :data:`MORSE_NUMERIC_SHORT`
* :data:`MORSE_PUNCTUATION`
* :data:`MORSE_SYMBOL`
* :data:`MORSE_ALPHA`
* :data:`MORSE_ENCODE`
* :data:`MORSE_ENCODE_SHORT`
* :data:`MORSE_DECODE`
* :data:`MORSE_DECODE_SHORT`

Members
-------

"""

from itertools import chain

MORSE_NUMERIC = {
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

MORSE_NUMERIC_SHORT = {
    '1': '.-',
    '2': '..-',
    '3': '...-',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '-...',
    '8': '-..',
    '9': '-.',
    '0': '-',
}

MORSE_PUNCTUATION = {
    '.': '.-.-.-',
    ':': '---...',
    ',': '--..--',
    ';': '-.-.-.',
    '?': '..--..',
    '=': '-...-',
    "'": '.----.',
    '"': '.-..-.',
    '/': '-..-.',
    '!': '-.-.--',
    '-': '-....-',
    '_': '..--.-',
    '(': '-.--.',
    ')': '-.--.-',
    '@': '.--.-.',
    '$': '...-..-',
    '&': '.-...',
    '+': '.-.-.',
}

MORSE_SYMBOL = {
    'AAAAA': '.-.-.-.-.-',
    'AAA': '.-.-.-',
    'EEEEE': '．．．．．',
    'AR': '.-.-.',
    'AS': '.-...',
    'TTTTT': '-----',
    'IMI': '..--..',
    'SK': '...-.-',
    'BT': '-...-',
    'SOS': '...---...',
}

MORSE_ALPHA = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}

MORSE_ENCODE = dict(chain(MORSE_NUMERIC.items(), MORSE_PUNCTUATION.items(), MORSE_ALPHA.items()))
MORSE_ENCODE_SHORT = dict(
    chain(MORSE_NUMERIC_SHORT.items(), MORSE_PUNCTUATION.items(), MORSE_ALPHA.items())
)

MORSE_DECODE = dict((v, k) for (k, v) in MORSE_ENCODE.items())
MORSE_DECODE_SHORT = dict((v, k) for (k, v) in MORSE_ENCODE_SHORT.items())

MORSE_SPLIT = " "
