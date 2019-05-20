#!/bin/bash

kill -9 `ps aux | awk '/main.py/ {print $2}'`
