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
for each galaxy, with each galaxy separated by a new line

Note that you may choose to keep some or all of the RGB values and and radius of the particles constant, and hence would not need to include this in the file

Output the data to Assets/Resources/[Name of Survey]Processed.txt

For example, the programme to convert the 2dF data includes the line:

ascii.write(dataTable, "../Assets/Resources/2dFProcessed.txt", delimiter=",", format="no_header")
