import csv
from datetime import datetime


# checking how many rows have 21, 22, 23, 24, 25, and 26 columns
def col_count(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        num_columns = len(header)
        count21 = 0
        count22 = 0
        count23 = 0
        count24 = 0
        count25 = 0
        count26 = 0
        for row_num, row in enumerate(reader, start=2):
            if len(row) == 21:
                count21 += 1
            elif len(row) == 22:
                count22 += 1
            elif len(row) == 23:
                count23 += 1
            elif len(row) == 24:
                count24 += 1
            elif len(row) == 25:
                count25 += 1
            elif len(row) == 26:
                count26 += 1
            else:
                print(f"Row {row_num} has {len(row)} columns")
    print(f"21 columns: {count21}")
    print(f"22 columns: {count22}")
    print(f"23 columns: {count23}")
    print(f"24 columns: {count24}")
    print(f"25 columns: {count25}")
    print(f"26 columns: {count26}")
    print(f"Total rows: {row_num}")


# seeing how many rows with 23 columns have a null values
def col23s_with_nulls(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        count_null = 0
        for row_num, row in enumerate(reader, start=2):
            if len(row) == 23:
                for column in row:
                    if column == "":
                        count_null += 1
                        break
    print(f"Total null values: {count_null}")


# moving all rows with 23 columns and no null values to a new file
def move_col23s_no_nulls(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        with open(
            "earthquake_data_23.csv", "a", newline="", encoding="utf-8"
        ) as new_file:
            writer = csv.writer(new_file)
            for row_num, row in enumerate(reader, start=2):
                if len(row) == 23:
                    for column in row:
                        if column == "":
                            break
                    else:
                        writer.writerow(row)


# checking that all rows with 23 columns and no null values were moved to the new file
def check_col23s_no_nulls(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row_num, row in enumerate(reader, start=2):
            if len(row) != 23:
                print(f"Row {row_num} has {len(row)} columns")
    print(f"Total rows: {row_num}")


# time sorted csv file
def sort_csv_by_time(name):
    data = []
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    sorted_data = sorted(
        data, key=lambda x: datetime.fromisoformat(x["time"].replace("Z", ""))
    )

    output_csv_file = "sorted_earthquake_data_23.csv"
    with open(output_csv_file, "w", newline="", encoding="utf-8") as file:
        fieldnames = sorted_data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in sorted_data:
            writer.writerow(row)


# checking if the magnitude column is always a float
def check_mag(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        header = next(reader)
        counter = 0
        for row_num, row in enumerate(reader, start=2):
            try:
                float(row["mag"])
            except ValueError:
                print(f"Row {row_num} has a non-float magnitude value")
                counter += 0
    if counter == 0:
        print("All magnitude values are floats")


# data type check per column of the first row
def check_data_types(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        for i in range(len(header)):
            print(f"{header[i]}: {next(reader)[i]}")


# remove all "," from the sorted_earthquake_data_23.txt file
def remove_faulty_commas(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        with open(
            "earthquake_data_23_no_commas.txt", "w", newline="", encoding="utf-8"
        ) as new_file:
            for line in file:
                new_file.write(line.replace('","', ""))


# checking how many rows in earthquake_data_23.csv are type earthquake
def check_type_earthquake(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        counter = 0
        for row_num, row in enumerate(reader, start=2):
            if row["type"] == "earthquake":
                counter += 1
        print(f"Total rows with type earthquake: {counter}")


# deleting all rows that are not type earthquake
def delete_non_earthquake(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        with open(
            "earthquake_data_23_type.csv", "w", newline="", encoding="utf-8"
        ) as new_file:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            writer.writeheader()
            for row_num, row in enumerate(reader, start=2):
                if row["type"] == "earthquake":
                    writer.writerow(row)


# delete type column
def delete_type_column(name):
    with open(name, "r", newline="", encoding="utf-8") as source:
        rdr = csv.reader(source)
        with open(
            "earthquake_data_23_no_type.csv", "w", newline="", encoding="utf-8"
        ) as result:
            wtr = csv.writer(result)
            for r in rdr:
                wtr.writerow(
                    (
                        f"{r[0]},{r[1]},{r[2]},{r[3]},{r[4]},{r[5]},{r[6]},{r[7]},{r[8]},{r[9]},{r[10]},{r[11]},{r[12]},{r[13]},{r[15]},{r[16]},{r[17]},{r[18]},{r[19]},{r[20]},{r[21]}".split(
                            ","
                        )
                    )
                )


# find earliest date
def find_earliest_date(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        earliest_date = datetime.now()
        for row_num, row in enumerate(reader, start=2):
            if datetime.fromisoformat(row["time"].replace("Z", "")) < earliest_date:
                earliest_date = datetime.fromisoformat(row["time"].replace("Z", ""))
        print(f"Earliest date: {earliest_date}")

# round the magnitude column to 1 decimal place
def round_mag(name):
    with open(name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        with open(
            "earthquake_data_23_rounded_mag.csv", "w", newline="", encoding="utf-8"
        ) as new_file:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            writer.writeheader()
            for row_num, row in enumerate(reader, start=2):
                row["mag"] = round(float(row["mag"]), 1)
                writer.writerow(row)
    
round_mag("earthquake_data_standardized.csv")
