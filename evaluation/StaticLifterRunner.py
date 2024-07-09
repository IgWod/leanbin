# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

import subprocess
import time

from LifterRunner import LifterRunner

class StaticLifterRunner(LifterRunner):
    def __init__(self, lifter):
        super().__init__(lifter)

    def lift(self, binary, args, stdio=None):
        return super().lift(binary, [], None)

    def get_name(self):
        raise NotImplementedError