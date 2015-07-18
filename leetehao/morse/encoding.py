# encoding: utf-8

"""
Encoding and decoding function

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


class MorseDecodeError(Exception):

    """Error while decode morse"""

    def __str__(self):
        return ('Error decode content: "{s}". Please extend or replace '
                'mapping dictionary to resolve.'.format(s=' '.join(self.args)))


class MorseEncodeError(Exception):

    """Error while encode morse"""

    def __str__(self):
        return ('Error encode content: "{s}". Please extend or replace '
                'mapping dictionary to resolve.'.format(s=' '.join(self.args)))


def encode(message='', encoding='utf-8', mapping=constants.MAP_FORWARD,
           spl=constants.SPLIT):
    """Encode mesaage

    :param message: message to encode
    :param encoding: message encoding
    :param mapping: mapping dictionary
    :param spl: split word between code
    :returns: encoded message

    """

    try:
        _message = spl.join(list(map(lambda v: mapping[v], list(message.upper()))))
    except KeyError as e:
        raise MorseEncodeError(e.args[0])

    return _message


def decode(message, encoding='utf-8', mapping=constants.MAP_INVERSE,
           spl=constants.SPLIT):
    """Decode mesaage

    :param message: message to decode
    :param encoding: message encoding
    :param mapping: mapping dictionary
    :param spl: split word between code
    :returns: decoded message

    """
    _tokens = message.split(spl)
    try:
        _detokens = list(map(lambda n: mapping[n], _tokens))
    except KeyError as e:
        raise MorseDecodeError(e.args[0])

    return ''.join(_detokens)
