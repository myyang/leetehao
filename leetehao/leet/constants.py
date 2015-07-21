# encoding: utf-8

"""
constants of leet

release |release|, version |version|

.. versionadded:: 1.0

    Initial

Contents
--------

Classes:

Functions:

Variables:

Members
-------

"""

from itertools import chain

MAP_NUMERIC = {
    "1": "On",
    "2": "Too",
    "3": "Thee",
    "4": "For",
    "5": "Fy",
    "6": "Sx",
    "7": "Say",
    "8": "At",
    "9": "Knight",
    "0": "Zero",
}

MAP_ALPHABET_ONE = {
    "A": "@",
    "B": "8",
    "C": "[",
    "D": ")",
    "E": "&",
    "F": "f",  # no ascii options for one charater
    "G": "6",
    "H": "#",
    "I": "!",
    "J": "j",  # no ascii options for one charater
    "K": "X",
    "L": "l",
    "M": "m",  # no ascii options for one charater
    "N": "^",
    "O": "0",
    "P": "?",
    "Q": "q",  # no ascii options for one charater
    "R": "2",
    "S": "$",
    "T": "+",
    "U": "v",
    "V": "u",
    "W": "w",  # no ascii options for one charater
    "X": "*",
    "Y": "7",
    "Z": "%",
    " ": "_",
}

MAP_FORWARD_ONE = dict(chain(MAP_ALPHABET_ONE.items(), MAP_NUMERIC.items()))
MAP_INVERSE_ONE = dict((v, k) for (k, v) in MAP_FORWARD_ONE.items())

MAP_ALPHABET_TWO = {
    "A": "(L",
    "B": "/3",
    "C": "[ ",  # no ascii options for two charater
    "D": "|)",
    "E": "[-",
    "F": "/=",
    "G": "<-",
    "H": "}{",
    "I": "][",
    "J": "(/",
    "K": "]{",
    "L": "[_",
    "M": "^^",
    "N": "/V",
    "O": "()",
    "P": "/*",
    "Q": "<|",
    "R": "[z",
    "S": "es",
    "T": "+ ",  # no ascii options for two charater
    "U": "L|",
    "V": "\|",
    "W": "vv",
    "X": "><",
    "Y": "`/",
    "Z": "7_",
    " ": "  ",
}

MAP_FORWARD_TWO = dict(chain(MAP_ALPHABET_TWO.items(), MAP_NUMERIC.items()))
MAP_INVERSE_TWO = dict((v, k) for (k, v) in MAP_FORWARD_TWO.items())

MAP_MIXED = {
    "A": set(["4", "/\\", "@", "/-\\", "^", "aye", "(L", "Д"]),
    "B": set(["8", "13", "|3", "ß", "P>", "|:", "!3", "(3", "/3", ")3", "|-]"]),
    "C": set(["[", "¢", "<", "(", "©"]),
    "D": set([")", "|)", "(|", "|o", "[)", "I>", "|>", "?", "T)", "I7", "cl"]),
    "E": set(["3", "&", "£", "€", "ë", "[-", "|=-"]),
    "F": set(["|=", "ƒ", "|#", "ph", "/=", "v"]),
    "G": set(["6", "&", "(_+", "9", "C-", "gee", "(?,", "[,", "{,", "<-", "(."]),
    "H": set(["#", "/-/", "[-]", "]-[", ")-(", "(-)", ":-:", "|~|", "|-|", "]~[", "}{", "!-!", "1-1", "\-/", "I+I", " ?", "}-{"]),
    "I": set(["1", "!", "¡", "j", "|", "eye", "3y3", "][", "]", "/me"]),
    "J": set(["_|", "_/", "¿", "</", "_]", "(/"]),
    "K": set(["X", "|<", "|{", "]{", "|X"]),
    "L": set(["1", "£", "7", "1_", "|", "|_", "el", "[]_", "[_"]),
    "M": set(["|v|", "[V]", "{{V}}", "em", "AA", "|\/|", "/\/\\", "(u)", "(V)", "(\/)", "/|\\", "^^", "/|/|", "//\\", "|\|\\", "]\/["]),
    "N": set(["^/", "|\|", "/\/", "[\]", "<\>", "{\}", "[]\\", "// []", "/V", "И", "^"]),
    "O": set(["0", "()", "oh", "[]", "p", "<>"]),
    "P": set(["|*", "|o", "|º", "?", "|^(o)", "|>", "|", "9", "[]D", "|°", "|7"]),
    "Q": set(["(_,)", "()_", "0_", "<|"]),
    "R": set(["|`", "|~", "|?", "/2", "|^", "lz", "|9", "2", "12", "®", "[z", "Я", ".-", "|2", "|-"]),
    "S": set(["5", "$", "z", "§", "ehs", "es"]),
    "T": set(["7", "+", "-|-", "1", "']['", "†", "\"|\""]),
    "U": set(["(_)", "|_|", "v", "L|", "µ", "V", "\/", "|/", "\|"]),
    "W": set(["\/\/", "vv", "\\N", "'//", "\\\\'", "\^/", "dubya", "(n)", "\V/", "\X/", "\|/", "\_|_/", "\_:_/", "?", "uu", "2u"]),
    "X": set(["><", "Ж", "}{", "ecks", "×", "?", ")(", "][", "}{"]),
    "Y": set(["j", "`/", "Ч", "7", "\|/", "¥"]),
    "Z": set(["2", "7_", "-/_", "%", ">_", "s"]),
    " ": set(["G/"]),
}

SPLIT = '  '

LETTER_FREQUENCY = [
    ' ', 'E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U',
    'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']
"""English"""
