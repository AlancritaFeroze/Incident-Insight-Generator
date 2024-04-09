# cis6930sp24 -- Assignment2

Name: Alancrita Feroze

UFID: 7491-0572

# Assignment Description 
The goal of the project is to fabricate datasheets outlining incident data.

# How to install
pipenv install

## How to run
pipenv run python assignment2.py --urls <file_name>

It can be run as follows:
![](https://github.com/VaishnaviReddy99/cis6930sp24-assignment2/blob/main/output.gif)




## Functions
#### assignment0\main.py \
This file is responsible to fetch data from the Given URLS and parse the pdfs to get Incident data

#### assignment2.py \
This is the main file responsible for the task

make_output_excel(filename, data): Creates an Excel sheet with the given filename and data.

parse_csv(filename): Parses a CSV file and returns the data.

evaluate_ranks(incidents): Evaluates ranks for incidents and returns incident ranks and location ranks.

main(filename): The main function of the file, which orchestrates the processing of data from the CSV file, evaluates ranks, augments incident data, and creates an Excel sheet.


#### util.py \
This script provides helper functions for various tasks related to incident data processing.

retrieve_coord(address, reference_latitude, reference_longitude, max_retries=2): Retrieves coordinates for a given address using Nominatim geocoder.

retrieve_day_week(date_string): Retrieves the day of the week from a given date string.

extract_hr_from_ts(timestamp): Extracts the hour from a given timestamp.

get_side_of_town(latitude, longitude, reference_latitude, reference_longitude): Determines the side of town based on latitude and longitude.

get_date_from_ts(timestamp): Extracts the date from a timestamp.

retrieve_weather(latitude, longitude, timestamp): Retrieves weather information for a given latitude, longitude, and timestamp.

get_coordinates_gmaps(address, reference_latitude, reference_longitude): Retrieves coordinates using Google Maps API.

    
## Datasheet Development
The datasheet is created as DATASHEET.xlsx. This file gets created during application runtime if not present.

## Assumptions
a. URLs are consistently provided within a CSV file, presuming the file contains either URLs or an identifier for acquiring supplementary details about each incident.

b. The util.py script acquires reference coordinates (reference_latitude and reference_longitude) in instances where geocoding is unsuccessful.

c. Date/Time, Incident Number, and Incident ORI must not be left null or empty.

d. The script assumes specific timestamp formats (likely "MM/DD/YYYY HH:MM") utilized within the data.

e. Both scripts may necessitate additional configuration for accessing external APIs (e.g., API keys).

f. To enhance efficiency in calls to the weather API, we are considering utilizing only the integer component (whole number part) of latitude and longitude coordinates when retrieving weather data for incidents.

## Bugs
If the script encounters a scenario where the incident's nature is provided but the location is missing, or vice versa, it will encounter a failure, halting its ability to parse the entire data file.

The code operates under the assumption that weather patterns remain consistent among locations sharing the same integer part of their latitude and longitude. While this optimization can effectively reduce the number of weather API calls, it could potentially result in inaccurate weather data for incidents located in close proximity but with slightly different coordinates.

