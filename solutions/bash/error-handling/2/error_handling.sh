#!/usr/bin/env bash

# Define a cleanup function to release resources if needed.
cleanup() {
    # If you had any resources to free (temporary files, file descriptors, etc.),
    # you would do so here. This script does not allocate additional resources.
    :
}

# Ensure that the cleanup function is called on script exit.
trap cleanup EXIT

main() {
    # Ensure exactly one argument is provided.
    if [ "$#" -ne 1 ]; then
        echo "Usage: error_handling.sh <person>"
        exit 1
    fi

    # Print the greeting, even if the argument is an empty string.
    echo "Hello, $1"
}

# Execute the main function with all positional arguments.
main "$@"
