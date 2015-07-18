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

from leetehao import base

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
    _message, last = '', len(message) - 1

    try:
        for i, v in enumerate(message.upper()):
            _message += mapping[v] + ('' if i == last else spl)
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


class MorseEncoder(base.BaseEncoder):

    mapping = constants.MAP_FORWARD
    spl = constants.SPLIT

    def _encode(self, msg, *args, **kwargs):
        _msg, last = '', len(msg) - 1

        try:
            for i, v in enumerate(msg.upper()):
                _msg += self.mapping[v] + ('' if i == last else self.spl)
        except KeyError as e:
            raise MorseEncodeError(e.args[0])

        return _msg


class MorseDecoder(base.BaseDecoder):

    mapping = constants.MAP_INVERSE
    spl = constants.SPLIT

    def _decode(self, msg, *args, **kwargs):
        ''' actual decode method '''
        _tokens = msg.split(self.spl)
        try:
            _detokens = list(map(lambda n: self.mapping[n], _tokens))
        except KeyError as e:
            raise MorseDecodeError(e.args[0])

        return ''.join(_detokens)
