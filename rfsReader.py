# -*- coding: utf-8 -*-
import linecache

# Frist read in the input and output files
#inFile = "Scan 86.0-87.0MHz.rfs"
#inFile = "Scan 117.0-118.0MHz.rfs"
inFile = "Scan 121.0-122.0MHz.rfs"
fIn = open(inFile, "r")

outFile = "MapPoints.csv"
fOut = open(outFile, "w")

# This is the line ending that we are going to search for
lineEnd = " [\n"

# This list stores the line number before the start of a data point
startLines = []

# Populate the list of startLines and close the input file
for num, line in enumerate(fIn, 1):
    if line.endswith(lineEnd):
        startLines.append(num)
fIn.close()

# Write a header row to the output file
fOut.write("Lat,Long,SignalStrength\n")

# For each item in the list of startLines, read the 3 following lines stripping
# the white space out.
for spot in startLines:
    spot1 = spot + 1; spot2 = spot+2; spot3 = spot+3;
    fOut.write(linecache.getline(inFile,spot1).strip())
    fOut.write(linecache.getline(inFile,spot2).strip())
    fOut.write(linecache.getline(inFile,spot3).strip())
    fOut.write("\n")

# Close the output file
fOut.close()