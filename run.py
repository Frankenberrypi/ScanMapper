import os

# Run the file reader, this generates a .csv file
os.system("rfsReader.py")

# Run the gpx writer, this generates a .gpx file from the .csv above
os.system("gpxWriter.py")

# Delete the .csv file to keep things tidy
os.remove("MapPoints.csv")