# Leanbin

This the meta repository used to build Leanbin from all its separate components.

> [!WARNING]
> Few problems have been identified and are currently being addressed:
>
> 1) Having multiple traces can cause issues with lifting and recompilation as duplicate trampoline entries are being generated.

## Requirements

The setup has been tested on Ubuntu 20.04 running on native AArch64 (Armv8.2) hardware with 512GB of RAM.

The tool includes majority of dependencies as sub-modules:

* [MAMBO](https://github.com/beehive-lab/mambo)
* [MAMBO Trace](https://github.com/IgWod/mambo-trace)
* [MAMBO Lift](https://github.com/IgWod/mambo-lift)
* [UNICORN](https://github.com/IgWod/unicorn)

The following tools also need to be installed:

* [Ropper](https://github.com/sashs/Ropper)
* [Binutils >=2.38](https://sourceware.org/pub/binutils/releases/)

Finally, the following tools are *optional* to install and are only used in the evaluation:

* [Instrew](https://github.com/aengelke/instrew)
* [RetDec](https://github.com/avast/retdec)

All required tools are automatically installed when `setup.sh` is used. Instrew and RetDec needs to be downloaded and build manually.

## Setup

First, `git` needs to be installed if not yet available, e.g.,

```
sudo apt install git
```

Then, the repository and all it sub-modules can be cloned with:

```
git clone --recurse-submodule https://github.com/IgWod/leanbin
```

Finally, provided scripts can be used to build Leanbin - those need to be run inside the `leanbin` directory:

```
cd leanbin/

source env.sh

./setup.sh
```

## Run

A simple wrapper script is provided to run all required commands, i.e., tracing, lifting, post-processing and recompilation:

```
source env.sh # Only needs to be done once

leanbin.sh <binary> <args>
```

Note: This script allows neither adding arguments to the lifter itself nor generating multiple traces.

For example:

```
printf "#include <stdio.h>\n\nint main() {\n\tprintf(\"Hello World\");\n\treturn 0;\n}\n" > example.c
gcc -o out example.c
./leanbin.sh out
./out_lifted
```

## Evaluation

To run the extensive evaluation of the tool provided Python script can be used:

```
python3 evaluation/Evaluate.py --lifter <path-to-leanbin-lifter> --tracer <path-to-leanbin-tracer> --instrew <path-to-instrew> --retdec <path-to-retdec> <spec> <benchmarks-dir>
```

Both `--retdec` and `--instrew` are optional and the tools are not used in the evaluation when skipped. A high-level scripts has been also provided to run the whole evaluation (excluding Instrew and RetDec) with provided JSON files for the SPEC CPU2006 INT benchmarks:

```
./evaluate.sh
```

It assumes that `CPU2006_ROOT` is set to the root directory of the SPEC CPU2006 benchmark suite and the `evaluation.cfg` (provided) has been copied to the `config/` directory of the suite. It is also assumed that `env.sh` has been sourced.

To summarize the following commands need to be run in order to clone, setup and evaluate Leanbin on Ubuntu 20.04 running natively on AArch64:

```
sudo apt install git
git clone --recurse-submodule https://github.com/IgWod/leanbin
cd leanbin/
source env.sh
./setup.sh

# Optional
# export CC=<compiler-used-to-recompile-lifted-binaries>
# e.g., export CC=clang-18 (see https://apt.llvm.org on how to install LLVM 18 on Ubuntu 20.04)

./evaluate.sh
```

### Docker

A Docker container is also provided to simplify the setup. To build it the following command should be run inside the Leanbin directory:

```
docker build --tag "leanbin:latest" .
```

To run it with the SPEC CPU2006 directory attached for the evaluation the following command can be used:

```
docker run -v <spec2006-root>:/home/mambo/cpu2006 -t -i leanbin
```

For all the other used `-v [...]` can be skipped.

The default credentials for the container are `mambo` (both user and the password).

Once inside the container the previously described commands can be run:

```
cd leanbin
source env.sh
./setup.sh

export CC=clang-18
export CPU2006_ROOT=/home/mambo/cpu2006/

./evaluate.sh
```

## Publications

If you use Leanbin in your research please cite:

```
@misc{leanbin,
      title={LeanBin: Harnessing Lifting and Recompilation to Debloat Binaries}, 
      author={Igor Wodiany and Antoniu Pop and Mikel Luján},
      year={2024},
      eprint={2406.16162},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2406.16162}, 
}
```
