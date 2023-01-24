#!/usr/bin/env python3
import os

def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=", "").replace("'C\n", ""))


def get_disk_usage():
    res = os.popen("df -h /").readlines()
    return res[1].split()[4]

def main():
    cpu_temp = get_cpu_temp()
    disk_usage = get_disk_usage()
    return (cpu_temp, disk_usage)