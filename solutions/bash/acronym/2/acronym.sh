#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<EOF
Usage: ${0##*/} ["phrase to convert"]

Converts a phrase into its uppercase acronym. If no arguments are given, reads from stdin.
Hyphens ("-") act as word separators; all other non-letter characters are ignored.
EOF
}

sanitize() {
  local input="$1"
  input="${input//-/ }"
  input="$(printf '%s' "$input" | tr -cd '[:alpha:] [:space:]')"
  printf '%s' "$input"
}

compute_acronym() {
  local text="$1" acronym=""
  for word in $text; do
    acronym+="${word:0:1}"
  done
  printf '%s' "${acronym^^}"
}

main() {
  if [[ ${1-} == "-h" || ${1-} == "--help" ]]; then
    usage
    exit 0
  fi

  local raw
  if [[ $# -gt 0 ]]; then
    raw="$*"
  else
    IFS= read -r raw || { echo "Error: no input provided." >&2; usage >&2; exit 1; }
  fi

  local cleaned result
  cleaned="$(sanitize "$raw")"
  result="$(compute_acronym "$cleaned")"

  printf '%s\n' "$result"
}

main "$@"