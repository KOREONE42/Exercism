#!/usr/bin/env bash

gcd() {
    a=$1
    b=$2
    while (( b )); do
        t=$b
        b=$((a % b))
        a=$t
    done
    echo $a
}

solve() {
    local from_cap=$1
    local to_cap=$2
    local goal=$3
    local from_name=$4
    local to_name=$5

    local from=0
    local to=0
    local moves=0

    while [[ $from -ne $goal && $to -ne $goal ]]; do
        if [[ $from -eq 0 ]]; then
            from=$from_cap
            moves=$((moves+1))
        elif [[ $to -eq $to_cap ]]; then
            to=0
            moves=$((moves+1))
        else
            local pour=$(( to_cap - to ))
            if [[ $from -lt $pour ]]; then
                pour=$from
            fi
            from=$((from - pour))
            to=$((to + pour))
            moves=$((moves+1))
        fi
        # forbidden state: starting bucket empty and other full
        if [[ $from -eq 0 && $to -eq $to_cap ]]; then
            break
        fi
    done

    if [[ $from -eq $goal ]]; then
        echo "$moves $from_name $to"
        return 0
    elif [[ $to -eq $goal ]]; then
        echo "$moves $to_name $from"
        return 0
    else
        return 1
    fi
}

main() {
    b1=$1
    b2=$2
    goal=$3
    start=$4

    if [[ "$start" == "one" ]]; then
        from_cap=$b1
        to_cap=$b2
        from_name="one"
        to_name="two"
    else
        from_cap=$b2
        to_cap=$b1
        from_name="two"
        to_name="one"
    fi

    # Validate numbers
    if [[ $goal -gt $b1 && $goal -gt $b2 ]]; then
        echo "invalid goal"
        exit 1
    fi

    divisor=$(gcd $b1 $b2)
    if (( goal % divisor != 0 )); then
        echo "invalid goal"
        exit 1
    fi

    # Special case: the goal is the full 'to' bucket.
    if [[ $goal -eq $to_cap ]]; then
        echo "moves: 2, goalBucket: $to_name, otherBucket: $from_cap"
        exit 0
    fi

    if result=$(solve $from_cap $to_cap $goal "$from_name" "$to_name"); then
        set -- $result
        moves=$1
        goal_bucket=$2
        other_bucket=$3
        echo "moves: $moves, goalBucket: $goal_bucket, otherBucket: $other_bucket"
        exit 0
    else
        echo "invalid goal"
        exit 1
    fi
}

main "$@"
