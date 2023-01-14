from datetime import datetime
import os
import time

def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=", "").replace("'C\n", ""))


def get_disk_usage():
    res = os.popen("df -h /").readlines()
    return res[1].split()[4]


while True:
    cpu_temp = get_cpu_temp()
    disk_usage = get_disk_usage()
    timestamp = datetime.now()

    if cpu_temp < 40:
        print(timestamp +" - CPU Temperature: " + str(cpu_temp) + "°C")
        print("I'm cold")
        print("Disk Usage: " + disk_usage)
        time.sleep(10)
    elif cpu_temp < 60:
        print(timestamp +" - CPU Temperature: " + str(cpu_temp) + "°C")
        print("All good, working temp")
        print("Disk Usage: " + disk_usage)
        time.sleep(10)
    elif cpu_temp < 80:
        print(timestamp +" - CPU Temperature: " + str(cpu_temp) + "°C")
        print("Getting a little warm")
        print("Disk Usage: " + disk_usage)
        time.sleep(10)
    else:
        print(timestamp +" - CPU Temperature: " + str(cpu_temp) + "°C")
        print("OVERHEATING!")
        print("Disk Usage: " + disk_usage)
        time.sleep(10)

