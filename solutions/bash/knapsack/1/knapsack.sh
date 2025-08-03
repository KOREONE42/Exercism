#!/usr/bin/env bash

# Validate arguments
if [[ $# -lt 1 ]]; then
  exit 1
fi

# Maximum weight capacity
capacity=$1
shift

# If no items, result is 0
if [[ $# -eq 0 ]]; then
  echo 0
  exit 0
fi

# Initialize DP array
declare -a dp
for ((i=0; i<=capacity; i++)); do
  dp[i]=0
done

# Process each item: weight:value
for item in "$@"; do
  IFS=':' read -r w v <<< "$item"
  # Update DP table backwards to avoid reuse
  for ((j=capacity; j>=w; j--)); do
    val=$(( dp[j-w] + v ))
    if (( val > dp[j] )); then
      dp[j]=$val
    fi
  done
done

# Output the maximum value for full capacity
echo "${dp[capacity]}"
