import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from sensor.models import SensorData  

csv_file_path = "dataset/ai4i2020.csv"  

with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        SensorData.objects.create(
            air_temperature=float(row['Air temperature [K]']),
            process_temperature=float(row['Process temperature [K]']),
            rotational_speed=float(row['Rotational speed [rpm]']),
            torque=float(row['Torque [Nm]']),
            tool_wear=float(row['Tool wear [min]']),
            machine_failure=int(row['Machine failure'])
        )

print("Import เสร็จเรียบร้อย!")