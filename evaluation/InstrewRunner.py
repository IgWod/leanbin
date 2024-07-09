# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

from DynamicLifterRunner import DynamicLifterRunner

class InstrewRunner(DynamicLifterRunner):
    def __init__(self, lifter):
        super().__init__(lifter)

    def get_name(self):
        return "Instrew"
