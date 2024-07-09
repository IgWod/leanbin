#!/bin/python3

# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

import argparse
import json
import os

from InstrewRunner import InstrewRunner
from RetdecRunner import RetdecRunner
from LeanbinTracerRunner import LeanbinTracerRunner
from LeanbinLifterRunner import LeanbinLifterRunner

from GadgetsMeter import GadgetsMeter
from SizeMeter import SizeMeter
from CoverageMeter import CoverageMeter

from NativeExecutor import NativeExecutor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog="ProgramName",
                    description="What the program does",
                    epilog="Text at the bottom of help")

    parser.add_argument("spec")
    parser.add_argument("prefix")
    parser.add_argument("--instrew")
    parser.add_argument("--retdec")
    parser.add_argument("--tracer")
    parser.add_argument("--lifter")

    args = parser.parse_args()

    lifters = []

    if args.instrew is not None:
        instrew = InstrewRunner(args.instrew)
        lifters.append(instrew)

    if args.retdec is not None:
        retdec = RetdecRunner(args.retdec)
        lifters.append(retdec)

    if args.tracer is not None:
        tracer = LeanbinTracerRunner(args.tracer)
        lifters.append(tracer)

    if args.tracer is not None and args.lifter is not None:
        lifter = LeanbinLifterRunner(args.lifter)
        lifters.append(lifter)

    print("Benchmark, Arguments", end=", ")
    for lifter in lifters:
        print(lifter.get_name(), end=", ")

    meters = [SizeMeter(), GadgetsMeter()] 
    pac = GadgetsMeter()
    coverage = CoverageMeter()

    executor = NativeExecutor()
    lifted_executor = NativeExecutor()

    print("Execution Time Native", end=", ")
    for meter in meters:
        print(meter.get_name() + " Native", end=", ")

    print("Execution Time Lifted", end=", ")
    for meter in meters:
        print(meter.get_name() + " Lifted", end=", ")
    print(pac.get_name() + " PAC Lifted", end=", ")

    print(coverage.get_name(), end=", ")

    print("Correct")

    with open(args.spec) as file:
        data = json.load(file)
        for program in data["programs"]:
            binary = os.path.basename(program["binary"])
            for arg in program["args"]:
                print(binary, end=", ")
                print(arg, end=", ")
                in_data=None
                if len(arg) > 0 and arg[0] == "<":
                    in_data_f = open(arg[1], "rb")
                    in_data = in_data_f.read()
                    in_data_f.close()
                    arg = []

                path = os.path.join(args.prefix, program["binary"])

                for lifter in lifters:
                    if isinstance(lifter, LeanbinLifterRunner):
                        lifter.extras = program["extra-args"]
                    result = lifter.lift(path, arg) 
                    print(result, end=", ")

                executor.run(path, arg)
                print(executor.execution_time, end=", ")

                for meter in meters:
                    result = meter.get_result(path)
                    print(result, end=", ")

                lifter.recompile(path)

                lifted_executor.run(path + "_lifted", arg)
                print(lifted_executor.execution_time, end=", ")

                for meter in meters:
                    if isinstance(lifter, SizeMeter):
                        result = meter.get_result(path + "_lifted_size")
                    else:
                        result = meter.get_result(path + "_lifted")
                    print(result, end=", ")

                result = pac.get_result(path + "_lifted_pac")
                print(result, end=", ")

                result = coverage.get_result(path)
                print(result, end=", ")

                if executor.stdout == lifted_executor.stdout and executor.stderr == lifted_executor.stderr:
                    print("Y")
                else:
                    print("N")

                for lifter in lifters:
                    lifter.cleanup(path)


