# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

import os
import subprocess
import time

class LifterRunner:
    def __init__(self, lifter):
        self.lifter = lifter
        self.extras = []
        pass

    def lift(self, binary, args, stdio=None):
        command = [self.lifter] + self.extras + [binary] + args
        begin = time.time() 
        subprocess.run(command, capture_output=True, input=stdio, cwd=os.path.dirname(binary), check=True)
        return time.time() - begin

    def recompile(self, binary):
        raise NotImplementedError

    def cleanup(self, binary):
        pass

    def get_name(self):
        raise NotImplementedError
