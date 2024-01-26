import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = [row for row in reader if len(row) >= 2]
    return data


def analyse_overheads(data):
    """
    Analyses overhead data to find the highest overhead category.
    """
    highest_category, highest_percentage = max(data, key=lambda x: float(x[1]))
    highest_percentage_rounded = round(float(highest_percentage), 2)
    return f"[HIGHEST OVERHEAD] {highest_category}: {highest_percentage_rounded}%"
