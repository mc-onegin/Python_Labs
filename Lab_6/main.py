import json
import csv
#1)
with open('Sample-JSON-file-with-multiple-records.json') as json_data:
    data = json.load(json_data)

with open('users.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    fieldnames = ['userId', 'firstName', 'lastName', 'phoneNumber', 'emailAddress']
    writer.writerow(fieldnames)

    for user in data['users']:
        row = [user.get(key) for key in fieldnames]
        writer.writerow(row)

#2)
with open('Sample-employee-JSON-data.json') as json_data2:
    data_2 = json.load(json_data2)

with open('Employees.csv', 'w', newline='') as csv_file2:
    writer_2 = csv.writer(csv_file2)
    fieldnames_2 = ['userId', 'jobTitle', 'firstName', 'lastName', 'employeeCode', 'region', 'phoneNumber', 'emailAddress']
    writer_2.writerow(fieldnames_2)

    for employees in data_2['Employees']:
        row = [employees.get(key) for key in fieldnames_2]
        writer_2.writerow(row)
