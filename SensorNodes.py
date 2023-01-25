#!/usr/bin/env python3
from datetime import datetime
import subprocess
import time

def get_cpu_temp():
    result = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True, text=True)
    temp = result.stdout.strip().split("=")[1].replace("'C", "")
    return float(temp)

def get_disk_usage():
    result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
    usage = result.stdout.strip().split("\n")[1].split()[4]
    return usage


while True:
    cpu_temp = get_cpu_temp()
    disk_usage = get_disk_usage()
    timestamp = datetime.now()

    if cpu_temp < 40:
        print(str(timestamp) +" - CPU Temperature: " + str(cpu_temp) + "°C")
        print("I'm cold")
        print("Disk Usage: " + disk_usage)
        time.sleep(10)
    elif cpu_temp < 60:
        print(str(timestamp) +" - CPU Temperature: " + str(cpu_temp) + "°C")
        print("All good, working temp")
        print("Disk Usage: " + disk_usage)
        time.sleep(10)
    elif cpu_temp < 80:
        print(str(timestamp) +" - CPU Temperature: " + str(cpu_temp) + "°C")
        print("Getting a little warm")
        print("Disk Usage: " + disk_usage)
        time.sleep(10)
    else:
        print(str(timestamp) +" - CPU Temperature: " + str(cpu_temp) + "°C")
        print("OVERHEATING!")
        print("Disk Usage: " + disk_usage)
        time.sleep(10)

