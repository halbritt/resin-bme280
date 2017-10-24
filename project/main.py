from datetime import datetime
import pandas as pd

import bme280
import smbus2

port = 1
address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)
dictlist = []
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
        dictlist.append(mydict)
    except:
        df = pd.DataFrame(dictlist)
        print(df)
        print("KABLOOEY!")
        break
