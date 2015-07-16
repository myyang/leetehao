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

import random
import re

from .import constants


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
    _message, last = '', len(message) - 1

    try:
        for i, v in enumerate(message.upper()):
            _message += (mapping[v] if v in mapping else v)
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
    for k, v in mapping.items():
        message = re.sub(re.escape(k), v, message)
    return message
