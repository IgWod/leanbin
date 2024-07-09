#/bin/bash

# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

$LIFT_ROOT/../mambo/dbm ${@:1}

$LIFT_ROOT/lifter ${1} && $LIFT_ROOT/bash/generate-source.sh ${1} && $LIFT_ROOT/bash/patch-and-compile.sh ${1}
