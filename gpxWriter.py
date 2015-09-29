# -*- coding: utf-8 -*-
import numpy as np

# Import data from file to numpy array, delete header.
# Data is of the form lad,lon,signal strength
scanData = np.genfromtxt('MapPoints.csv', delimiter=',')
scanData = np.delete(scanData,0,0)

def colorBar(signalStrength):
    if 200 < signalStrength <= 220:
        return "FF0000"
    elif 180 < signalStrength <= 200:
        return "FF8000"
    elif 160 < signalStrength <= 180:
        return "FFFF00"
    elif 140 < signalStrength <= 160:
        return "00FF00"
    elif 120 < signalStrength <= 140:
        return "00FFFF"
    elif 100 <= signalStrength <= 120:
        return "0000FF"
    else:
        return False

outFile = "Scan 121.0-122.0MHz.gpx"
fOut = open(outFile,"w")
fOut.write('<?xml version="1.0" encoding="UTF-8"?><gpx xmlns="http://www.topografix.com/GPX/1/1" version="1.1" creator="CALTOPO">\n')

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
    
fOut.write('</gpx>\n')
fOut.close()



    
    
