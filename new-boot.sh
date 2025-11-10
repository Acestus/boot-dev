#!/bin/bash

exercise=${1:-"exponents"}
course="memory-management"

mkdir -p "./$course/$exercise"

touch "./$course/$exercise/main_test.c"
touch "./$course/$exercise/main.c"

code "./$course/$exercise/main_test.c"
code "./$course/$exercise/main.c"

echo "Created exercise: $exercise in $course"