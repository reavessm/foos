#!/bin/bash

function function_exit() {
  kill -9 `ps aux | awk '/video.sh/ {print $2}'`
}
trap function_exit EXIT

./video.sh &>/dev/null &

python ./main.py
