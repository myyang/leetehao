# encoding: utf-8

"""
Core functionalities

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

from __future__ import absolute_import

import re

from leetehao import base

from . import constants


class LeetDecodeError(Exception):

    """Error while decode morse"""

    def __str__(self):
        return ('Error decode message: "{s}". Please make sure the message is inversable.'
                'Next, please extend or replace mapping dictionary to resolve.'.format(
                    s=' '.join(self.args))
                )


class LeetEncodeError(Exception):

    """Error while encode morse"""

    def __str__(self):
        return ('Error encode message: "{s}". Please extend or replace '
                'mapping dictionary to resolve.'.format(s=' '.join(self.args)))


def encode(message='', encoding='utf-8', mapping=constants.MAP_FORWARD_TWO):
    """Encode mesaage

    :param message: message to encode
    :param encoding: message encoding
    :param mapping: mapping dictionary
    :param spl: split word between code
    :returns: encoded message

    """

    try:
        _message = ''.join(list(map(lambda v: mapping.get(v, v), list(message.upper()))))
    except KeyError as e:
        raise LeetEncodeError(e.args[0])

    return _message


def decode(message, encoding='utf-8', mapping=constants.MAP_INVERSE_TWO):
    """Decode mesaage

    :param message: message to decode
    :param encoding: message encoding
    :param mapping: mapping dictionary
    :param spl: split word between code
    :returns: decoded message

    """
    inv_map = dict((v, k) for (k, v) in mapping.items())
    keys = constants.LETTER_FREQUENCY + list(
        set(constants.LETTER_FREQUENCY).symmetric_difference(set(inv_map.keys())))

    for k in keys:
        message = re.sub(re.escape(inv_map[k]), k, message)
    return message


class LeetEncoder(base.BaseEncoder):

    mapping = constants.MAP_ALPHABET_TWO


class LeetDecoder(base.BaseDecoder):

    mapping = constants.MAP_INVERSE_TWO
