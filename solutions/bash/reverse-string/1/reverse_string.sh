#!/usr/bin/env bash

reverse_string() {
  # Uses 'rev' to reverse the input string
  echo "$1" | rev
}

main() {
  reverse_string "$1"
}

main "$@"
