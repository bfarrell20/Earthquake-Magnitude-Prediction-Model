from time import sleep
import requests
import csv
import os

times = 0
# queries are limited to 20000 entries so must be queries are monthly
# will wait 15+ seconds when requesting too much 
for i in range(0000, 2023):
    for j in range(1, 12):
        if j < 10:
            url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&eventtype=earthquake&starttime=" + str(i) + "-0" + str(j) + "-01&endtime=" + str(i) + "-0" + str(j) + "-31"
        else:
            url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&eventtype=earthquake&starttime=" + str(i) + "-" + str(j) + "-01&endtime=" + str(i) + "-" + str(j) + "-31"
        with requests.Session() as s:
            response = requests.get(url)
            if response.status_code == 200:
                times = 0
                decoded_content = response.content.decode("utf-8")
                csv_rows = decoded_content.strip().split("\n")

                csv_file = 'earthquake_data.csv'
                file_exists = os.path.isfile(csv_file)

                with open(csv_file, 'a', newline='', encoding='utf-8') as fd:
                    writer = csv.writer(fd)
                    
                    if not file_exists:
                        writer.writerow(["time", "latitude", "longitude", "depth", "mag", "magType", "nst", "gap", "dmin", "rms", "net", "id", "updated", "place", "type", "horizontalError", "depthError", "magError", "magNst", "status", "locationSource", "magSource"])

                    for row in csv_rows[1:]:
                        writer.writerow(row.split(','))
            else:
                print(f"API request for {url} failed with status code: {response.status_code}")
                if response.status_code == 429 or response.status_code == 400:
                    times += 1
                    j -= 1
                    print(f"Waiting {times * 15} seconds before trying again")
                    sleep(times * 15)
                    if times == 5:
                        print("Too many failed requests, skipping to next month")
                        j += 1