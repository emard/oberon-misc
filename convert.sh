#!/bin/sh

# convert unix txt (\n line ending)
# to oberon Text (\r line ending)

cat $1 | tr -d \\r | tr \\n \\r > $2
