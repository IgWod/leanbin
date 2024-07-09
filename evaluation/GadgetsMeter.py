# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

from ropper import RopperService

from Meter import Meter

class GadgetsMeter(Meter):
    def __init__(self):
        super().__init__()

    def get_result(self, binary):
        options = { "all" : False, "type" : "all" }

        rs = RopperService(options)
        rs.addFile(binary)
        rs.loadGadgetsFor()

        return len(rs.files[0].gadgets)

    def get_name(self):
        return "Gadgets"
