# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

class Meter:
    def __init__(self):
        pass

    def get_result(self, binary):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError
