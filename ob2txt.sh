#!/bin/sh

# convert oberon Text (\r line ending)
# to unix txt (\n line ending)

cat $1 | tr \\r \\n > $2
