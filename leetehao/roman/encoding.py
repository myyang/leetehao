# encoding: utf-8

"""
Encode / Decode

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


from . import constants


class RomanDecodeError(Exception):
    pass


class RomanEncodeError(Exception):
    pass


def encode(value):
    if not 0 < value < 4000:
        raise RomanEncodeError('Value should be 1~3999')
    s = ''

    def conv(x, div, U, H, N):
        v, x = x // div, x % div
        if 9 > v >= 5:
            return H + U * (v - 5), x
        elif v == 4:
            return U + H, x
        elif v == 9:
            return U + N, x
        else:
            return U * v, x

    v, rem = value // 1000, value % 1000
    s += constants.THOU * v
    for u, h, d, n in [constants.HUND, constants.TENS, constants.UNIT]:
        ap, rem = conv(rem, d, u, h, n)
        s += ap

    return s


def decode(message):
    msg_set, val_set = set(message), set(constants.VALUE_MAPPING)
    if not val_set.issuperset(msg_set):
        raise RomanDecodeError(
            'Roman numerals ONLY contains: ["I", "V", "X", "L", "C", "D", "M"]')
    t = 0
    s = str(message).upper()
    for i in list(s):
        t += constants.VALUE_MAPPING[i]

    for k in constants.CORRECTION_MAPPING:
        if k in s:
            t += constants.CORRECTION_MAPPING[k]
    return t
