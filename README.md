# Cardboard-Universe-2dF
## Adding a New Survey
1. Download [Unity](https://unity3d.com/) (Personal Edition is fine).
2. Download [GitHub Desktop](https://desktop.github.com/).
3. On the [2dF repository page](https://github.com/RossKnapman/Cardboard-Universe-2dF), select "Clone or download", "Open in Desktop", "Launch Application".
4. Clone to your desired location.
5. Replace the "2dF" in the project name with the name of the new survey.
6. In the project, delete the contents of the "Data" folder.
7. Add the raw data for the new survey, e.g. in the form of a .txt file.
8. Write a Python programme to convert the raw data to the table below, in a .txt file, with the values separated by commas in the format:

  x position, y position, z position, Red, Green, Blue, Radius of particles
  
  for each galaxy, with each galaxy separated by a new line.

  Note that you may choose to keep some or all of the RGB values and and radius of the particles constant, and hence would not need to include this in the file

  Output the data to Assets/Resources/[Name of New Survey]Processed.txt

  For example, the programme to convert the 2dF data includes the line:

  ascii.write(dataTable, "../Assets/Resources/2dFProcessed.txt", delimiter=",", format="no_header")

  Run this programme to place the data in the required location.

  While writing the programme, make a note of how many units in the Cartesian output correspond to 1 redshift unit. For example, for the 2dF survey, 1000 Cartesian output units correspond to 1 redshift unit.

9. In Assets/Runtime Scripts/Scale Grid/CreateGrid.cs, set redshiftScale on line 7 to the value noted down previously.
10. In the same script, set intervalLength on line 9 to the desired number of units in the Unity visualisation space between successive scale rings.
11. In Assets/Resources/Constants.txt, replace the 300 with the outer limit in Unity visualisation space units that the camera can reach in any dimension from the origin, which also corresponds to the radius of the outer ring of the scale grid (you can decided on this by playing around in Unity). Note that you may wish to override this in the script to draw the scale grid to prevent confusion with a distance in ly greater than the age of the universe, see the CreateGrid.cs script in the WiggleZ repository for an example of when this has been the case.
12. Also in CreateGrid.cs, you frustratingly must manually input the distance in Gly corresponding to each redshift, so write the code to do this in the format of lines 39-48. You can find the values for each redshift value using the calculator [here](http://www.astro.ucla.edu/~wright/CosmoCalc.html).
13. In Assets/Runtime Scripts/AddGalaxies.cs, for any colour values that are to remain constant for all galaxies set the values, e.g. 0.5f.
14. For any colour values which are to vary between galaxies, set them from the required index in the text file containing the processed data.

  For example, say the data contains the Cartesian coordinates, red values, and blue values. Each line would be in the format:
  
  x, y, z, R, B
  
  So the R value would be at index 3, hence set redValue = galaxyData [i][3], and blueValue = galaxyData [i][4]
15. If the particle size varies between galaxies, this can be set in a similar way to the colour.
  1. On line 22, remove the "=2f" part.
  2. Within the loop starting at line 52, add the line particleSize = galaxyData[i][x], where x is the index in a line in the processed data file that stores the radius of the particles. Ensure this is before line 57.
16. Change "2dFProcessed" in line 30 to [Name of New Survey]Processed.
17. In Assets/Runtime Scripts/, on line 13, change the speed that the camera flies around the survey if desired.
18. Change the logo:
  1. In Unity, select "File", "Build Settings...", "Player Settings" and "Select" under "Default Icon" in the Inspector panel. Select the new logo.
  2. In "Icon", next to the 192x192 option, select the same logo.
19. Generally tweak the project.
20. Build the apk:
  1. Select "File", "Build Settings..."
  2. Under "Other Settings" in the Inspector panel, replace "TwodFSurvey" in the bundle identifier with the name of the new survey.
  3. If you plan on submitting an update to Google Play, increment the Version and the Bundle Version Code by 1.
  4. FOR THE FIRST TIME ONLY under "Publishing Settings", create a new keystore. Remember the password (for all of the projects so far it is "survey"). IF YOU CREATE A NEW KEYSTORE ONCE IT'S BEEN SUBMITTED TO GOOGLE PLAY, YOU WILL NOT BE ABLE TO SUBMIT A NEW UPDATE so always "Use Existing Keystore" after publishing.

I'm pretty sure this is complete, though I have most likely missed out some minor steps along the way so feel free to email me with any questions at rjknapman@gmail.com if you run into any problems.
