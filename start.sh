#!/bin/bash

function function_exit() {
  kill -9 `ps aux | awk '/stream.sh/ {print $2}'`
}
trap function_exit EXIT

./stream.sh &>/dev/null &

python ./main.py
