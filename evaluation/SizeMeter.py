# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

from elftools.elf.elffile import ELFFile

from Meter import Meter

class SizeMeter(Meter):
    def __init__(self):
        super().__init__()

    def get_result(self, binary):
        with open(binary, "rb") as binary:
            elf = ELFFile(binary)

            section = elf.get_section_by_name(".text")

            return section["sh_size"]

    def get_name(self):
        return "Binary Size"
