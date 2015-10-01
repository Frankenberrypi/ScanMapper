# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Import data from file to numpy array, delete header.
# Data is of the form lad,lon,signal strength
scanData = np.genfromtxt('MapPoints.csv', delimiter=',')
# Delete the header row
scanData = np.delete(scanData,0,0)

# Load the color map
cMap = plt.get_cmap("jet")

# This function takes an array of RGB color and returns a string of hex color
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
# End of function -------------------------------------

# This function takes a normalized signal strength and returns a string of 
# hex color, using the function above. 
def colorBar(signalStrength):
    red = np.round(cMap(signalStrength)[0]*255,decimals=0)
    green = np.round(cMap(signalStrength)[1]*255,decimals=0)
    blue = np.round(cMap(signalStrength)[2]*255,decimals=0)
    rgb = (red,green,blue)

    return rgb_to_hex(rgb)
# End of function -------------------------------------    
    

#Find the bounds for normalization
latMax, lonMax, sigMax = scanData.max(axis=0)
latMin, lonMin, sigMin = scanData.min(axis=0)

#Do the normalization math, replacing the right column in the array
for i in range(0,len(scanData)):
    scanData[i,2] = (scanData[i,2] - sigMin) / (sigMax - sigMin)

# Open the gpx file for writing
outFile = "Scan 121.0-122.0MHz.gpx"
fOut = open(outFile,"w")

# Write the first line of the gpx
fOut.write('<?xml version="1.0" encoding="UTF-8"?><gpx xmlns="'\
'http://www.topografix.com/GPX/1/1" version="1.1" creator="CALTOPO">\n')

# Write the waypoints to the gpx file
for i in range(0,len(scanData)):
    fOut.write('  <wpt lat="')
    fOut.write(np.array_str(scanData[i,0]))
    fOut.write('" lon="')
    fOut.write(np.array_str(scanData[i,1]))
    fOut.write('">\n')
    fOut.write('    <name>ELT ')
    fOut.write(str(i))
    fOut.write('</name>\n')
    fOut.write('    <cmt/>\n')
    fOut.write('<desc><![CDATA[comments=&url=%23')
    fOut.write(colorBar(scanData[i,2]))
    fOut.write(']]></desc>\n')
    fOut.write('  </wpt>\n')
    
# Close the gpx file, both with a tag, then close the file. 
fOut.write('</gpx>\n')
fOut.close()



    
    
