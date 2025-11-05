Param(
    [Parameter(Position=0)]
    [string]$exercise = "exponents"
)

$course = "data-structures"
mkdir ".\$course\$exercise"
New-Item -ItemType File -Path ".\$course\$exercise\main.py"
New-Item -ItemType File -Path ".\$course\$exercise\main_test.py"
code ".\$course\$exercise\main.py"
code ".\$course\$exercise\main_test.py"