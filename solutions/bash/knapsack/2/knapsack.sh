#!/usr/bin/env bash

set -euo pipefail

# Print usage and exit
usage() {
  echo "Usage: $0 MAX_WEIGHT [WEIGHT:VALUE]..." >&2
  exit 1
}

# Main entry point
main() {
  # Require at least the capacity argument
  [[ $# -ge 1 ]] || usage

  local capacity=$1
  shift

  # No items => zero value
  if [[ $# -eq 0 ]]; then
    echo 0
    return 0
  fi

  # Initialize DP array (0 to capacity)
  local -a dp
  for ((i = 0; i <= capacity; i++)); do
    dp[i]=0
  done

  # Process each item (format: weight:value)
  for item in "$@"; do
    IFS=':' read -r w v <<< "$item"

    # Skip items heavier than capacity
    (( w > capacity )) && continue

    # Compute and update DP table backwards
    for ((j = capacity; j >= w; j--)); do
      local candidate=$(( dp[j - w] + v ))
      if (( candidate > dp[j] )); then
        dp[j]=$candidate
      fi
    done
  done

  # Output max value for full capacity
  echo "${dp[$capacity]}"
}

# Invoke main with all arguments
main "$@"
