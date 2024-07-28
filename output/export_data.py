import json
import csv

def export_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Username'])
        for item in data:
            writer.writerow([item])
