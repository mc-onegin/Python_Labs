import os
import csv
import random
from random import sample
def Show(file_path="users.csv", output_type="top", num_rows=5, separator=","):
    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter=separator)
        data = list(reader)

    headers = data[0]
    rows = data[1:]
    if len(rows) < num_rows:
        print(f"В файле {len(rows)} строк, вывод всех строк.")
        selected_rows = rows
    else:
        if output_type == "top":
            selected_rows = rows[:num_rows]
        elif output_type == "bottom":
            selected_rows = rows[-num_rows:]
        elif output_type == "random":
            selected_rows = sample(rows, k=num_rows)
    all_data = [headers] + selected_rows
    max_lengths = [max(len(str(x)) for x in col) for col in zip(*all_data)]
    format_string = "| ".join(["{:<" + str(max_len) + "}" for max_len in max_lengths])

    def format_row(row):
        return format_string.format(*row)

    print(format_row(headers))
    print("-" * sum(max_lengths) + "-" * len(max_lengths) * 2)
    for row in selected_rows:
        print(format_row(row))


def Info(file_path="users.csv"):
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)

    total_rows = len(rows)
    column_count = len(header)
    print(f"{total_rows}x{column_count}")

    field_stats = {}
    for i, field in enumerate(header):
        non_empty_values = []
        for row in rows:
            value = row[i].strip()
            if value != '':
                try:
                    converted_value = int(value)
                    type_str = 'int'
                except ValueError:
                    try:
                        converted_value = float(value)
                        type_str = 'float'
                    except ValueError:
                        converted_value = value
                        type_str = 'string'
                non_empty_values.append(converted_value)

        count_non_empty = len(non_empty_values)
        types_in_field = set(type(v).__name__ for v in non_empty_values)
        most_common_type = sorted(types_in_field)[0]

        field_stats[field] = {
            'count': count_non_empty,
            'type': most_common_type
        }
    for field, stats in field_stats.items():
        print(f"{field:<10}{stats['count']:^10}{stats['type']:<10}")


def DelNaN(input_file="users.csv", output_file="cleaned_users.csv"):
    with open(input_file, newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        filtered_data = []
        for row in reader:
            if not any(field.strip() == "" for field in row):
                filtered_data.append(row)
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(filtered_data)


def MakeDS(input_file="users.csv"):
    base_dir = "workdata"
    learning_dir = os.path.join(base_dir, "Learning")
    testing_dir = os.path.join(base_dir, "Testing")
    os.makedirs(learning_dir)
    os.makedirs(testing_dir)

    with open(input_file, newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        data = list(reader)

    random.shuffle(data)
    split_point = int(len(data) * 0.7)
    training_set = data[:split_point]
    testing_set = data[split_point:]

    with open(os.path.join(learning_dir, "train.csv"), mode='w', newline='') as train_file:
        writer = csv.writer(train_file)
        writer.writerow(header)
        writer.writerows(training_set)

    with open(os.path.join(testing_dir, "test.csv"), mode='w', newline='') as test_file:
        writer = csv.writer(test_file)
        writer.writerow(header)
        writer.writerows(testing_set)


Show()
#Show(output_type="random", num_rows=15)
Info()
DelNaN()
MakeDS()

