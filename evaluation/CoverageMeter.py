# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

import os
import re
import subprocess

from elftools.elf.elffile import ELFFile

from Meter import Meter

class CoverageMeter(Meter):
    def __init__(self):
        super().__init__()

    def get_result(self, binary):
        blocks = os.path.join(os.path.dirname(binary), "blocks.txt")

        subprocess.run(["sort", "-k", "2", "-o", blocks, blocks])

        with open(binary, "rb") as binary:
          elf = ELFFile(binary)

          text_section = elf.get_section_by_name(".text")

          lower = text_section["sh_addr"]
          upper = text_section["sh_size"] + lower
          size = text_section["sh_size"]

          blocks_list = []

          with open(blocks, "r") as blocks:
            for line in blocks:
              block = line.split()
              block[0] = int(block[0], 16)
              block[1] = int(block[1], 16)
              if block[0] >= lower and block[1] < upper:
                if len(blocks_list) == 0:
                  blocks_list.append(block)
                else:
                  if block[1] != blocks_list[-1][1]:
                    if(blocks_list[-1][1] + 4 != block[0]):
                      pass
                    blocks_list.append(block)

          covered = 0
          for b in blocks_list:
            covered += b[1] - b[0] + 4

          return (covered / size) * 100

    def get_name(self):
        return "Coverage"
