import csv

csv_file = 'earthquake_data_notype_23col.csv'
output_file = 'earthquake_data_standardized.csv'

# find max of columns latitude, longitude, depth, nst, gap, dmin, rms, depthError, magError, magNst
with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    maxes = {"latitude": 0, "longitude": 0, "depth": 0, "nst": 0, "gap": 0, "dmin": 0, "rms": 0, "horizontalError": 0, "depthError": 0, "magError": 0, "magNst": 0}
    for row in reader:
        for key in row:
            if key in maxes:
                if float(row[key]) > maxes[key]:
                    maxes[key] = float(row[key])
    print(maxes)

# create month and day columns based on the datetime columns and standardize them
# divide the value in each column by the max and place in new csv file
with open(csv_file, "r", newline="", encoding="utf-8") as oldfile:
    with open(output_file, "w", newline="", encoding="utf-8") as newfile:
        reader = csv.DictReader(oldfile)
        writer = csv.DictWriter(newfile, fieldnames=["month", "day", "latitude", "longitude", "depth", "mag", "nst", "gap", "dmin", "rms", "horizontalError", "depthError", "magError", "magNst"])
        writer.writeheader()
        for row in reader:
            newrow = {}
            for key in row:
                if key in maxes:
                    newrow[key] = float(row[key]) / maxes[key]
            newrow["month"] = float(row["time"][5:7])/12
            newrow["day"] = float(row["time"][8:10])/31
            newrow["mag"] = float(row["mag"])
            writer.writerow(newrow)