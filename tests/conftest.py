import os
import sys

# add non-packaged seplib to the path
seplib_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, seplib_path + "/../../")

from .fixtures import *
