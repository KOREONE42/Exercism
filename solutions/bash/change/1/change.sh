#!/usr/bin/env bash

target="$1"
shift
coins=("$@")

# Validate target
if [[ -z "$target" || ! "$target" =~ ^-?[0-9]+$ ]]; then
  echo "target can't be negative"
  exit 1
fi

if (( target < 0 )); then
  echo "target can't be negative"
  exit 1
fi

# No change needed for 0
if (( target == 0 )); then
  exit 0
fi

# Initialize DP arrays
# best[i] = min coins to make amount i
# prev[i] = coin used to make amount i
declare -a best
declare -a prev
max=$((target + 1))
best[0]=0
for ((i=1; i<=target; i++)); do
  best[i]=$max
  prev[i]=-1
done

# Compute DP
for ((i=1; i<=target; i++)); do
  for c in "${coins[@]}"; do
    if (( c <= i )) && (( best[i-c] + 1 < best[i] )) && (( best[i-c] < max )); then
      best[i]=$(( best[i-c] + 1 ))
      prev[i]=$c
    fi
  done
done

# Check if solution exists
if (( best[target] >= max )); then
  echo "can't make target with given coins"
  exit 1
fi

# Reconstruct solution
result=()
amt=$target
while (( amt > 0 )); do
  c=${prev[amt]}
  result+=("$c")
  (( amt -= c ))
done

# Output sorted result
printf "%s\n" "${result[@]}" | sort -n | tr '\n' ' ' | sed 's/ $/\n/'
