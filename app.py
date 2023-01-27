from flask import Flask
app = Flask(__name__)
import psutil

def get_temp():
    temp = psutil.sensors_temperatures()["cpu_thermal"][0]
    return temp

def get_disk_usage():
    usage = psutil.disk_usage('/').percent
    return usage

def get_both():
    temp = psutil.sensors_temperatures()["cpu_thermal"][0]
    usage = psutil.disk_usage('/').percent
    return float(temp.current), str(usage)

@app.route('/error')
def error():
    cpu_temp = get_temp()
    errortemp = 60
    if float(str(cpu_temp.current)) >= float(errortemp):
        output = "Critical temperature: " + str(cpu_temp.current)
    output = "Temperature in good range: " + str(cpu_temp.current)
    return output

@app.route('/cpu/temp')
def get_cpu_temp():
    cpu_temp = get_temp()
    output = "Temperature: " + str(cpu_temp.current)
    return output

@app.route('/disk/usage')
def get_ram():
    usage = get_disk_usage()
    output = "Usage: " + str(usage)
    return output


if __name__ == "__main__":
    app.run(debug=True)
