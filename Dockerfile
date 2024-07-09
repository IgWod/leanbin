FROM ubuntu:20.04

RUN apt update
RUN apt install -y gnupg2 wget

RUN echo "deb http://apt.llvm.org/focal/ llvm-toolchain-focal-18 main" | tee -a /etc/apt/sources.list
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt upgrade -y
RUN apt install -y xz-utils git sudo vim
RUN apt install -y clang-18 lldb-18 lld-18

# Create new user

RUN useradd -ms /bin/bash mambo
RUN echo 'mambo:mambo' | chpasswd
RUN usermod -a -G sudo mambo

USER mambo
WORKDIR /home/mambo/

RUN git clone --recurse-submodule https://github.com/IgWod/leanbin
