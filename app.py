from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/cpu/temp')
def get_cpu_temp():
    return '<h1>CPU Temp:</h2>'

@app.route('/disk/usage')
def get_disk_usage():
    return '<h1>Disk USAGE:</h2>'


if __name__ == "__main__":
    app.run(debug=True)