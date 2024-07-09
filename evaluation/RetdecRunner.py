# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

import glob
import os

from StaticLifterRunner import StaticLifterRunner

class RetdecRunner(StaticLifterRunner):
    def __init__(self, lifter):
        super().__init__(lifter)
        self.extras = ["--cleanup"]

    def get_name(self):
        return "RetDec"

    def cleanup(self, binary):
        for f in glob.glob(binary + ".*"):
            os.remove(f)
