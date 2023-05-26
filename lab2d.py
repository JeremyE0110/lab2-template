#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    usage_message = sys.argv[0] + ' name age'
    print('Usage:', usage_message)
    sys.exit()


#Objects
name = sys.argv[1]
age = int(sys.argv[2])

print('Hi ' + name + ', you are ' + str(age) + ' years old.')
