#!/usr/bin/env bash

n="$1"
if [[ -z $n ]]; then
    exit 1
fi

lo=1
hi=$n

while (( lo <= hi )); do
    mid=$(((lo+hi)/2))
    sq=$((mid*mid))
    if (( sq == n )); then
        echo "$mid"
        exit 0
    elif (( sq < n )); then
        lo=$((mid+1))
    else
        hi=$((mid-1))
    fi
 done
