#!/bin/bash

args=("$@")

#args is of length 3 or larger
#args[1] is either "answer" or "elaborate"
#args[2] is the question (a string) that you typed in
#args[3] is either a timeout value, or a list of integers indicating the blah number

python debate_server.py &

if [ $1 = "answer" ]; then

    for f in $2; do
        que="$que$f "
    done

    python debate_client.py $1 "$que" $3


else

    for f in $2; do
        que="$que$f "
    done
    python debate_client.py $1 "$que" ${@:3}

fi