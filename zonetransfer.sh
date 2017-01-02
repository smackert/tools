#!/bin/bash

# Zone Transfer bash script


if [ -z "$1" ]; then
exit 0
fi

for dns in $(host -t ns $1 | cut -d " " -f 4); do
host -l $1 $dns | grep "has address" | cut -d " " -f 1,4
done
