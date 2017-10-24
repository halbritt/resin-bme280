import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address)

# the compensated_reading class has the following attributes
print(data.id)
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)

# there is a handy string representation too
print(data)

mydict = {
    "uuid": str(data.id),
    "timestamp" : datetime.strftime(data.timestamp, "%s%f"),
    "temperature" : data.temperature
    "pressure" : data.pressure,
    "humidity" : data.humidity
    }

print(mydict)
