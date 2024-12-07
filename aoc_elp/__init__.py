from .utils import elpsort, ON_CHAR, OFF_CHAR, LEFT, UP, RIGHT, DOWN, CHAR_TO_DS, DS, TURN_LEFT45, TURN_LEFT90, TURN_RIGHT45, TURN_RIGHT90, UPLEFT, UPRIGHT, DOWNLEFT, DOWNRIGHT, arounds, get_raw_inputs

__version__ = "0.0.1"
__author__ = "Edward Palmer"

def library_info():
    return f"ELP's AOC helper utils v{__version__}"
