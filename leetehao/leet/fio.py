# encoding: utf-8

"""
File I/O

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
import os
import logging
import collections

PATH = os.path.dirname(os.path.abspath(__file__)) + '/data/mapping.txt'
'''Default mapping dictionary'''
PAT = r'(?P<char>\w{1,1}) (?P<value>.+)'
"""Serach pattern"""

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def get_mapping_dict(path=PATH, _set=False):
    """get mapping dictionary of list/set

    :param path: absolutely path of mapping dictionary file
    :returns: dictionary of list/set

    """
    mappings = collections.defaultdict(set)

    with open(path) as f:
        for line in f.readlines():
            LOGGER.debug("line: {l}".format(l=line))
            char, value = re.search(PAT, line).groups()
            mappings[char].add(value)

    if not _set:
        for k in mappings:
            mappings[k] = list(mappings[k])
        LOGGER.debug('dictionary of list: {m}'.format(m=mappings))
        return mappings

    LOGGER.debug('dictionary of set: {m}'.format(m=mappings))
    return mappings
