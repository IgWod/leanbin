# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

import os
import subprocess
import time


class NativeExecutor:
    def __init__(self):
        self.stdout = None
        self.stderr = None
        self.execution_time = None

    def run(self, binary, args, stdio=None):
        command = [binary] + args
        begin = time.time() 
        result = subprocess.run(command, capture_output=True, input=stdio, cwd=os.path.dirname(binary))
        self.stdout = result.stdout.decode("utf-8")
        self.stderr = result.stderr.decode("utf-8")
        self.execution_time = time.time() - begin
