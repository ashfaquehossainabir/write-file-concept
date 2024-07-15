# Python writing files (.txt, .json, .csv)

import json
import csv

txt_data = "I like pizza"

file_path = "output.txt"


# Write File "w"

# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"text file '{file_path}' was created")


# Prevent Overwrite File "x"

# try:
#     with open(file_path, "x") as file:
#         file.write(txt_data)
#         print(f"text file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


# Append File "a"

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
#
# try:
#     with open(file_path, "a") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"text file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


# Create JSON File

# json_file_path = "output.json"
#
# employee = {
#     "name": "SpongeBob",
#     "age": 30,
#     "job": "Cook"
# }
#
# try:
#     with open(json_file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file '{json_file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


# Create CSV File

csv_file_path = "output.csv"

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

try:
    with open(csv_file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{csv_file_path}' was created")
except FileExistsError:
    print("That file already exists!")
