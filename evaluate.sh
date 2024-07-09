#!/bin/bash

# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

CURRENT_DIR=$(pwd)

cd $CPU2006_ROOT
source shrc

runspec --action=setup --config evaluation.cfg --size ref int > /dev/null 2> /dev/null || exit 1
python3 $LIFT_ROOT/../evaluation/Evaluate.py --lifter $LIFT_ROOT/lifter --tracer $LIFT_ROOT/../mambo/dbm $LIFT_ROOT/../evaluation/config/cpu2006-ref-d.json $CPU2006_ROOT/.. || exit 1

runspec --action=setup --config evaluation.cfg --size ref int > /dev/null 2> /dev/null || exit 1
python3 $LIFT_ROOT/../evaluation/Evaluate.py --lifter $LIFT_ROOT/lifter --tracer $LIFT_ROOT/../mambo/dbm $LIFT_ROOT/../evaluation/config/cpu2006-ref-ds1.json $CPU2006_ROOT/.. || exit 1

runspec --action=setup --config evaluation.cfg --size ref int > /dev/null 2> /dev/null || exit 1
python3 $LIFT_ROOT/../evaluation/Evaluate.py --lifter $LIFT_ROOT/lifter --tracer $LIFT_ROOT/../mambo/dbm $LIFT_ROOT/../evaluation/config/cpu2006-ref-ds2.json $CPU2006_ROOT/.. || exit 1

cd $CURRENT_DIR

