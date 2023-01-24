#!/usr/bin/env python3
import subprocess

def get_cpu_temp():
    result = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True, text=True)
    temp = result.stdout.strip().split("=")[1].replace("'C", "")
    return float(temp)

def get_disk_usage():
    result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
    usage = result.stdout.strip().split("\n")[1].split()[4]
    return usage

def main():
    cpu_temp = get_cpu_temp()
    disk_usage = get_disk_usage()
    return (cpu_temp, disk_usage)