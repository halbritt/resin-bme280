from datetime import datetime

import bme280
import smbus2

port = 1
address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)

while True:
    try:
        data = bme280.sample(bus, address)
        mydict = {
            "uuid": str(data.id),
            "timestamp": datetime.strftime(data.timestamp, "%s%f"),
            "temperature": data.temperature,
            "pressure": data.pressure,
            "humidity": data.humidity
        }

        print(mydict)
    except:
        print("KABLOOEY!")
        break
