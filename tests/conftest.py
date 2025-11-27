import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
