#!/bin/bash

TESTS=(
"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
"5 * X^0 + 4 * X^1 = 4 * X^0"
"8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0" #greater than 2, I can't solve
"8 * X^0 - 6 * X^1 + 0 * X^2 - 0 * X^3 = 3 * X^0" #greater than 2, but 2 is 0, so can solve
"1 * X^0 + 1 * X^1 = 0"
"42 * X^0 = 42 * X^0" # every real number is a solution
"42 * X^0 + 2 * X^1 = 42 * X^0 + 2 * X^1" # every real number
"42 * X^0 + 2 * X^1 + 5 * X^2 = 42 * X^0 + 2 * X^1 + 5 * X^2" # every real number
"1 * X^0 + 1 * X^1 + 1 * X^2 = 0" # no real solutions
"1 * X^0 + 0 * X^1 + 2 * X^2 = 0" # no real solutions
"42 * X^0 = 24 * X^0" # no solution
"1 * X^0 + 0 * X^1 = 0" # no solution
"0 * X^0 + 1 * X^1 = 0" # zero
"-2 * X^0 - 1 * X^1 = 0" # negative
"-2 * X^0 - 1 * X^1 = -3 * X^2" # negative
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