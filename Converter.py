# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 17:17:05 2015

@author: Jeff Beckman
"""
import str

infile = "Scan 86.0-87.0MHz.rfs"
f = open(infile, "r")
outfile = "MapPoints.txt"
fOut = open(outfile, "w")
for line in iter(f):
    if str.endswith(": ["):
        for i in range(0,3):
            fOut.write(line)
    #print line

f.close()
fOut.close()