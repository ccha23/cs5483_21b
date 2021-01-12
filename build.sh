#!/bin/bash
for cmd in "jupyter-book build ." "ghp-import -n -p -f _build/html"
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