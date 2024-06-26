#!/bin/bash

source ./setup/setup_Linux.shù

clear

echo "Do you want to run the program in GUI mode? (y/n)-->"
read UserInput

cd /bin/

if [ $UserInput = "n" ]; then
    python3 router.py --cli --help
    exit
fi

python3 router.py --gui
exit