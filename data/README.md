# Data folder

Files in this directory include all python scripts that collect satellite, space debris, and space weather data. 
This forms the backend of the application. The data is passed into a python package called SGP4 which takes the 
live data and propagates them using orbital mechanics principles. 

Since satellite orbits can be changed in small ways each day, a script will access the live data from Celestrak and 
update it each day so that the orbits are always representing the most accurate data.

This directory includes the following resources:
- **Raw Data**: Unprocessed satellite, space weather, and debris datasets.
- **Processed Data**: cleaned and transformed data fit for analysis and visualization.
- **External Sources**: Links or instructions for downloading larger datasets if not stored in this directory.
