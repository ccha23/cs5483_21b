#!/bin/bash
for cmd in "nbgrader generate_assignment $1" "jupyter-book build ." "ghp-import -n -p -f _build/html" "nbgrader release_assignment $1"
do
    read -r -p "${cmd}?[Y/n] " input

    case $input in
        [yY][eE][sS]|[yY]|'')
    echo "Executing..."
    eval $cmd
    ;;
        [nN][oO]|[nN])
    echo "Skipped..."
        ;;
        *)
    echo "Invalid input..."
    exit 1
    ;;
    esac
done