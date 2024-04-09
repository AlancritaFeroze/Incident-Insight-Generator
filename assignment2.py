import csv
from openpyxl import Workbook
import argparse

import assignment0.main
import util
from assignment0 import main


incident_rank = {}
reference_latitude = 35.220833
reference_longitude = -97.443611


class AugmentedIncident:
    def __init__(self, day_of_week, time_of_day, weather, location_rank, side_of_town, incident_rank, nature, ems_stat):
        self.weather = weather
        self.side_of_town = side_of_town
        self.ems_stat = ems_stat
        self.incident_rank = incident_rank
        self.location_rank = location_rank
        self.day_of_week = day_of_week
        self.nature = nature
        self.time_of_day = time_of_day
        

    def to_list(self):
        return [self.day_of_week, self.time_of_day, self.weather, self.location_rank,
                self.side_of_town, self.incident_rank, self.nature, self.ems_stat]


def make_output_excel(filename, data):
    wb = Workbook()
    ws = wb.active

    for row in data:
        print(row)
        ws.append(row)

    wb.save(filename)
    print(f"Excel sheet '{filename}' created successfully!")


def parse_csv(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

def evaluate_ranks(incidents):
    locfreq = {}
    natfreq = {}
    for incident in incidents:
        if incident.nature in natfreq:
            natfreq[incident.nature] += 1
        else:
            natfreq[incident.nature] = 1
        if incident.incident_location in locfreq:
            natfreq[incident.incident_location] += 1
        else:
            natfreq[incident.incident_location] = 1

    sorted_frequency = sorted(natfreq.items(), key=lambda x: x[1], reverse=True)
    rank = 1
    ranks = {}
    previous_count = None
    for element, count in sorted_frequency:
        if count != previous_count:
            rank = len(ranks) + 1
        ranks[element] = rank
        previous_count = count

    sorted_frequency = sorted(natfreq.items(), key=lambda x: x[1], reverse=True)
    rank = 1
    locationRanks = {}
    previous_count = None
    for element, count in sorted_frequency:
        if count != previous_count:
            rank = len(ranks) + 1
        locationRanks[element] = rank
        previous_count = count


    return ranks,locationRanks




def main(filename):
    parsed_data = parse_csv(filename)
    augmented_data = list()
    augmented_data.append(["Day Of the Week", "Time of Day", "Weather", "Location Rank","Side of Town", "Incident Rank","Nature","EMSSTAT"])
    total_data = []
    for pd in parsed_data:
        for data in pd:
            if data:
                results = assignment0.main.parseAndFetchResults(data)
                total_data.extend(results)
    incidentRanks,location_ranks = evaluate_ranks(total_data)

    count = 0
    tc = len(total_data)
    for result in total_data:
        #if count > 100 : break
        day = util.retrieve_day_week(result.incident_time)
        timeOfDay = util.extract_hr_from_ts(result.incident_time)
        latitude, longitude = util.get_coordinates_gmaps(result.incident_location, reference_latitude,
                                                   reference_longitude)
        weather_of_inc = util.retrieve_weather(latitude, longitude, result.incident_time)
        location_rank = location_ranks[result.incident_location]
        sideOfTown = util.get_side_of_town(latitude, longitude, reference_latitude, reference_longitude)
        incident_rank = incidentRanks[result.nature]
        nature = result.nature
        emstatt = False
        if result.incident_ori == "EMSSTAT":
            emstatt = True
        ia = AugmentedIncident(day, timeOfDay, weather_of_inc, location_rank, sideOfTown, incident_rank, nature,
                               emstatt)
        augmented_data.append(AugmentedIncident.to_list(ia))
        count = count + 1
        print(str(tc - count)+" Records pending")


    filename = "DATASHEET.xlsx"
    make_output_excel(filename, augmented_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", type=str, required=True,
                        help="Incident summary URLs file")

    args = parser.parse_args()
    if args.urls:
        main(args.urls)

