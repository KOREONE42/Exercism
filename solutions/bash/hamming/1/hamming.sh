#!/usr/bin/env bash

# Check that exactly two arguments are provided
if [[ $# -ne 2 ]]; then
  echo "Usage: hamming.sh <string1> <string2>"
  exit 1
fi

# Read input strands
s1=$1
s2=$2

# Compare lengths
len1=${#s1}
len2=${#s2}
if [[ $len1 -ne $len2 ]]; then
  echo "strands must be of equal length"
  exit 1
fi

# Compute Hamming distance
distance=0
for (( i=0; i<len1; i++ )); do
  c1=${s1:i:1}
  c2=${s2:i:1}
  if [[ "$c1" != "$c2" ]]; then
    ((distance++))
  fi
 done

# Output result
echo "$distance"
