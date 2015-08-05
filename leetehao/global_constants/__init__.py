# encoding: utf-8

from .leet import *
from .morse import *
from .roman import *

import os, sys, logging

f = 'leetehao_local.py'
local = os.path.join(os.path.abspath(os.path.curdir), f)
if os.path.exists(local):
    sys.path.append(local)
    from leetehao_local import *
    logging.debug("Loaded constants in %s" % f)
else:
    logging.debug("No local defined file at '%s', using default" % f)
