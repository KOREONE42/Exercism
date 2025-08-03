#!/usr/bin/env bash
set -euo pipefail

main() {
  local raw

  if [[ $# -gt 0 ]]; then
    raw="$*"
  else
    IFS= read -r raw
  fi

  # Hyphens → spaces, drop anything that isn't a letter or space
  raw="${raw//-/ }"
  raw="${raw//[^[:alpha:] ]/}"

  # Build acronym from first letters
  local acronym=""
  for word in $raw; do
    acronym+="${word:0:1}"
  done

  # Upper‑case and print
  printf '%s\n' "${acronym^^}"
}

main "$@"
