#!/bin/bash

exercise=${1:-"exponents"}
course="data-structures"

mkdir -p "./$course/$exercise"

touch "./$course/$exercise/main_test.py"
touch "./$course/$exercise/main.py"

code "./$course/$exercise/main_test.py"
code "./$course/$exercise/main.py"

echo "Created exercise: $exercise in $course"