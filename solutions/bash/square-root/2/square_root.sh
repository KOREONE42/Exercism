#!/usr/bin/env bash

# Compute the integer square root of a perfect-square positive integer input

main() {
    local n="$1"

    # Validate input: must be a non-negative integer
    if [[ ! "$n" =~ ^[0-9]+$ ]]; then
        echo "Usage: $0 <non-negative-integer>" >&2
        exit 1
    fi

    # Handle zero explicitly
    if [[ "$n" -eq 0 ]]; then
        echo 0
        exit 0
    fi

    local lo=1
    local hi=$n

    # Binary search for the exact root
    while (( lo <= hi )); do
        local mid=$(((lo + hi) / 2))
        local sq=$((mid * mid))

        if (( sq == n )); then
            echo "$mid"
            exit 0
        elif (( sq < n )); then
            lo=$((mid + 1))
        else
            hi=$((mid - 1))
        fi
    done
}

main "$@"