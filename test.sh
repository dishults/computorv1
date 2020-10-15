#!/bin/bash

TESTS=(
"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
"5 * X^0 + 4 * X^1 = 4 * X^0"
"8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
)

if [ $1 = "all" ]; then
    for test in "${TESTS[@]}"; do
        echo "$test"
        ./computor.py "$test"
        echo ""
    done
else
    echo "${TESTS[$1]}"
    ./computor.py "${TESTS[$1]}"
fi