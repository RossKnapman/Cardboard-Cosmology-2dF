from matplotlib import pyplot as plt

import numpy as np
from astropy.coordinates import Angle
from astropy import units as u
from astropy import coordinates as coord
from astropy.table import Table
from astropy.io import ascii

# Import required data, reshuffle, and get random sample
print("\nImporting data...")
data = np.genfromtxt("2dFData.txt", dtype="str", delimiter=',')

# Slice data array to get values of interest
print("\nSlicing arrays...")
RAStrings = data[:,1]
DecStrings = data[:,2]
RedshiftStrings = data[:,3]
RedMagStrings = data[:,4]
BlueMagStrings = data[:,5]

# Convert these string values to values that astropy can manage
print("\nConverting data:")
print("\tGetting RA values...")
RAValues = Angle(RAStrings, u.hourangle)
print("\tConverting RA values to radians...")
RAValues = RAValues.to(u.rad)
print("\tGetting Dec values...")
DecValues = Angle(DecStrings, u.deg)
print("\tConverting Dec values to radians...")
DecValues = np.radians(DecValues)
print("\tGetting redshift values...")
RedshiftValues = RedshiftStrings.astype(np.float)
print("\tGetting r_F magnitudes...")
rFMags = RedMagStrings.astype(np.float)
print("\tGetting b_J magnitudes...")
bJMags = BlueMagStrings.astype(np.float)

# Get the red and blue values for the galaxies
# The formulae for converting magnitudes are from http://magnum.anu.edu.au/~TDFgg/Public/Release/PhotCat/photcalib.html
# I have assigned the 'g' values as blue here
# Don't read into it too much; I spent like an entire day optimising it and it is the result of MANY minor tweaks
gamma = 5 # For gamma correction
cutoff = 2000 # The distance from the end of the data to cut it off, exlcuding anomalously high values
print("\nGetting colour data...")
print("\tGetting red magnitudes...")
RedMags = rFMags + 0.13
print("\tGetting blue magnitudes...")
BlueMags = (1/1.13) * (bJMags - 0.15 + (0.13 * (rFMags + 0.13)))
print("\tGetting red intensities...")
RedIntensities = 10 ** RedMags
print("\tGetting blue intensities...")
BlueIntensities = 10 ** BlueMags
print("\tGetting red values...")
Red = RedIntensities ** (1/(gamma))
RedValues = np.interp(Red, np.array([np.sort(Red)[cutoff], np.sort(Red)[len(Red)-cutoff]]), np.array([0.0, 0.75]))
print("\tGetting blue values...")
Blue = BlueIntensities ** (1/(gamma * 1000))
BlueValues = np.interp(Blue, np.array([np.sort(Blue)[cutoff], np.sort(Blue)[len(Blue)-cutoff]]), np.array([0.0, 1.0]))

## Plot graph to aid in optimising above code
#plt.figure()
#plt.ylim(0, 1.1)
#plt.plot(RedValues, np.linspace(1, len(RedValues), len(RedValues)), np.sort(RedValues), 'r-')
#plt.plot(BlueValues, np.linspace(1, len(BlueValues), len(RedValues)), np.sort(BlueValues), 'b-')
#plt.show()

# Get the Cartesian coordinates of the galaxies
print("\nGetting cartesian values...")
multiplier = 1000 # The factor to spread it out in Unity visualisation space, equivalent to redshiftScale in CreateGrid.cs
XArray = RedshiftValues * np.cos(DecValues) * np.cos(RAValues) * multiplier
YArray = RedshiftValues * np.cos(DecValues) * np.sin(RAValues) * multiplier
ZArray = RedshiftValues * np.sin(DecValues) * multiplier

# Assign values to table
print("\nWriting data to table...")
dataTable = Table({'x' : XArray, 'y' : YArray, 'z' : ZArray, 'R' : RedValues, 'B' : BlueValues}, names=("x", "y", "z", "R", "B"))

# Write to file
print("\nWriting to file...")
ascii.write(dataTable, "../Assets/Resources/2dFProcessed.txt", delimiter=",", format="no_header")

print("\nDone!\n")