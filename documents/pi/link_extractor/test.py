#!/usr/bin/env python

import sys

f = open('HERE.txt','a')
f.write(sys.argv[1]+'\n')
f.close()
