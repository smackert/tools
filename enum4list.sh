#!/usr/bin/env bash

# usage: ./enum4list.sh [list of hosts] 

mkdir -p "enum4linux-results";
while read p; do
	enum4linux -a $p > enum4linux-results/$p.txt
done <$1
