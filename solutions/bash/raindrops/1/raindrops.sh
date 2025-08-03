#!/usr/bin/env bash

raindrop() {
  local n=$1 result=""
  (( n % 3 == 0 )) && result+="Pling"
  (( n % 5 == 0 )) && result+="Plang"
  (( n % 7 == 0 )) && result+="Plong"
  # If nothing was added, use the number itself
  if [[ -z $result ]]; then
    result="$n"
  fi
  printf "%s\n" "$result"
}

main() {
  if (( $# == 0 )); then
    echo "Usage: $0 <number> [<number> ...]" >&2
    exit 1
  fi

  for num in "$@"; do
    raindrop "$num"
  done
}

main "$@"
