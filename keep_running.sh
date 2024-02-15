#!/usr/bin/bash
python3 index.py 1
read -r output < output.txt

while [ "$output" != "success" ]
do
    sleep 20    
    python3 index.py "$output"
    read -r output < output.txt
done
