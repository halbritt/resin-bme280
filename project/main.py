import bme280
import smbus2
from flask import Flask

port = 1
address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)
app = Flask(__name__)


@app.route('/')
def get_sample():
    data = bme280.sample(bus, address)
    mydict = {
        "uuid": str(data.id),
        "timestamp": datetime.strftime(data.timestamp, "%s%f"),
        "temperature": data.temperature,
        "pressure": data.pressure,
        "humidity": data.humidity
    }
    return mydict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
