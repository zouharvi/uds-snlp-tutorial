#!/bin/bash

wget https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt -O /tmp/alice
cat /tmp/alice | tr  ' ' '\n' | grep . | sort | uniq -ic |  sort -nr | awk '{print "|"NR"|"$2"|"$1"|"}' | head -n 20