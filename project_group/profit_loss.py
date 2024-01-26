import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)  
        next(reader) 
        data = [row for row in reader if len(row) >= 5]
    return data