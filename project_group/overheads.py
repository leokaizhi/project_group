import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = []
        for row in reader:
            if len(row) >= 2:
                data.append(row)
    return data


def analyse_overheads(data):
    """
    Analyses overhead data to find the highest overhead category.
    """
    highest_percentage = float(-1000000)
    highest_category = ''

    for row in data:
        category = row[0]
        percentage = float(row[1])
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_category = category

    highest_percentage_rounded = round(highest_percentage, 2)
    return f"[HIGHEST OVERHEAD] {highest_category}: {highest_percentage_rounded}%"