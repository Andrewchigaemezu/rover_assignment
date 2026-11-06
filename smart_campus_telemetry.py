"""
Smart Campus Telemetry & Data Log Processor
SS1 Creative Capstone Project

This program processes mock telemetry records from a campus rover.
It converts raw text readings into useful values and prints a
simple executive report.
"""


# 1. Use Of Constants

MAX_VOLTAGE = 24.0
MIN_TEMPERATURE = 0.0
MAX_TEMPERATURE = 50.0


# 2. Mock raw telemetry
# Each record is a CSV-style string:
# ID,temperature,motor_pulses,distance,voltage,status

raw_logs = [
    "ROV001,28.5,1200,15.75,22.4,active",
    "ROV002,31.2,1450,18.20,23.1,active",
    "ROV003,47.8,1800,25.60,24.8,warning",
    "ROV004,19.6,980,12.40,21.7,idle",
    "ROV005,52.3,2100,30.15,25.2,warning"
]


# 3. Collections and report
processed_logs = []
sensor_units = ("C", "pulses", "m", "V")  # Tuple: fixed collection of sensor units

campus_summary = {
    "rover_count": 0,
    "total_motor_pulses": 0,
    "total_distance": 0.0,
    "warning_count": 0
}

# -------------------------
# 4. Process each raw log
# -------------------------
for raw_log in raw_logs:
    # Check the length of the raw log
    log_length = len(raw_log)

    # Split the CSV-style text into separate fields
    fields = raw_log.split(",")

    # Extract the rover ID using string slicing
    rover_id = fields[0]
    rover_prefix = rover_id[0:3]
    rover_number = rover_id[-1]
    

    # Convert text readings into appropriate data types
    temperature = float(fields[1])
    motor_pulses = int(fields[2])
    distance = float(fields[3])
    voltage = float(fields[4])
    rover_status = str(fields[5]).lower()

    # Store a Boolean value to indicate whether the rover is active
    is_active = rover_status == "active"

    # Check whether temperature and voltage are within the sample limits
    temperature_ok = MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE
    voltage_ok = voltage <= MAX_VOLTAGE

    # Create a readable status message
    if not temperature_ok or not voltage_ok or rover_status == "warning":
        report_status = "CHECK REQUIRED"
        campus_summary["warning_count"] += 1
    else:
        report_status = "NORMAL"

    # Store processed information in a dictionary
    rover_record = {
        "rover_id": rover_id,
        "rover_prefix": rover_prefix,
        "rover_number": rover_number,
        "temperature": temperature,
        "motor_pulses": motor_pulses,
        "distance": distance,
        "voltage": voltage,
        "rover_status": rover_status,
        "is_active": is_active,
        "log_length": log_length,
        "report_status": report_status
    }

    processed_logs.append(rover_record)

    # Update the campus summary
    campus_summary["rover_count"] += 1
    campus_summary["total_motor_pulses"] += motor_pulses
    campus_summary["total_distance"] += distance


# 5. Executive report

print("SMART CAMPUS ROVER - EXECUTIVE TELEMETRY REPORT".upper())


for rover in processed_logs:
    rover_id = rover["rover_id"].upper()
    status_text = rover["report_status"].upper()

    print(
        "Rover: {} | ID Prefix: {} | ID Ending: {}".format(
            rover_id,
            rover["rover_prefix"].upper(),
            rover["rover_number"]
        )
    )

    print(
        f"Temperature: {rover['temperature']:.1f} {sensor_units[0]} | "
        f"Motor Pulses: {rover['motor_pulses']} {sensor_units[1]} | "
        f"Distance: {rover['distance']:.2f} {sensor_units[2]}"
    )

    print(
        "Voltage: {:.1f} V | Active: {} | Status: {}".format(
            rover["voltage"],
            rover["is_active"],
            status_text
        )
    )

    print(f"Raw log length: {rover['log_length']} characters")
    


# 6. Final campus summary

print("CAMPUS SUMMARY".upper())
print("Total rovers processed: {}".format(campus_summary["rover_count"]))
print("Total motor pulses: {}".format(campus_summary["total_motor_pulses"]))
print("Total distance: {:.2f} meters".format(campus_summary["total_distance"]))
print("Rovers requiring checks: {}".format(campus_summary["warning_count"]))

# Demonstrate upper(), lower(), and split() using a sample text
sample_text = "SMART CAMPUS,ROVER TELEMETRY,DATA PROCESSING"
print("Sample text in lowercase:", sample_text.lower())
print("Sample text in uppercase:", sample_text.upper())
print("Sample text split into words:", sample_text.split(","))
