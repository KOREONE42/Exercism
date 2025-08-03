#!/usr/bin/env bash

target=$1
shift
coins=("$@")

# validate target is a non-negative integer
if [[ ! $target =~ ^-?[0-9]+$ ]]; then
  echo "target can't be negative"
  exit 1
fi
if (( target < 0 )); then
  echo "target can't be negative"
  exit 1
fi

# no change for zero
(( target == 0 )) && exit 0

# initialize DP arrays
declare -a best prev
inf=$((target + 1))
best[0]=0
for ((i=1; i<=target; i++)); do
  best[i]=$inf
  prev[i]=-1
done

# compute minimal coins
for ((i=1; i<=target; i++)); do
  for c in "${coins[@]}"; do
    if (( c <= i && best[i-c] + 1 < best[i] )); then
      best[i]=$((best[i-c] + 1))
      prev[i]=$c
    fi
  done
done

# check feasibility
if (( best[target] >= inf )); then
  echo "can't make target with given coins"
  exit 1
fi

# reconstruct solution
result=()
amt=$target
while (( amt > 0 )); do
  result+=("${prev[amt]}")
  (( amt -= prev[amt] ))
done

# output in ascending order
printf "%s\n" "${result[@]}" | sort -n | tr '\n' ' ' | sed 's/ $/\n/'
