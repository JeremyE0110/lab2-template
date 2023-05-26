#!/usr/bin/env python3

#Author:Jeremy Evangelista
#Author ID:129577193
#Date Created:2023/05/26

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
    
print('blast off!')