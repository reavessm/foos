#!/bin/bash

kill -9 `ps aux | awk '/python main.py/ {print $2}'`
