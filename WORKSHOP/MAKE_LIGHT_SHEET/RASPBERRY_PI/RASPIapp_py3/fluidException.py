import os
import datetime


class fluidException(Exception):
    def __init__(self, *args):
        self.args = [a for a in args]
