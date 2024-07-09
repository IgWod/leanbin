#!/bin/bash

# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

export UNICORN_ROOT=$(pwd)/unicorn
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$UNICORN_ROOT/build
export LIFT_ROOT=$(pwd)/mambo-lift
export PYTHONPATH=$PYTHONPATH:$LIFT_ROOT/python/pyelftools/
export PATH=$(pwd)/binutils-2.38/binutils:$PATH
