from prometheus_client import start_http_server, Summary
from prometheus_client import Counter
from prometheus_client import Gauge
import random
import time
import board
import busio
import adafruit_ina260
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan1 = AnalogIn(ads, ADS.P0)
chan2 = AnalogIn(ads, ADS.P1)
chan3 = AnalogIn(ads, ADS.P2)
chan4 = AnalogIn(ads, ADS.P3)
# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

#print("{:>5}\t{:>5}".format('raw', 'v'))

#while True:
#    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
#    time.sleep(0.5)



i2c = busio.I2C(board.SCL, board.SDA)
ina1 = adafruit_ina260.INA260(i2c, 0x40)
ina2 = adafruit_ina260.INA260(i2c, 0x41)
ina3 = adafruit_ina260.INA260(i2c, 0x42)
ina4 = adafruit_ina260.INA260(i2c, 0x43)
ina5 = adafruit_ina260.INA260(i2c, 0x44)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

c = Counter('my_failures', 'Description of counter')
c.inc()     # Increment by 1
#c.inc(1.6)  # Increment by given value
c.inc(33)
c.inc(33)

g1 = Gauge('ina1_current', 'Description of gauge')
g2 = Gauge('ina2_current', 'Description of gauge')
g3 = Gauge('ina3_current', 'Description of gauge')
g4 = Gauge('ina4_current', 'Description of gauge')
g5 = Gauge('ina5_current', 'Description of gauge')
g6 = Gauge('ina1_voltage', 'Description of gauge')
g7 = Gauge('ina2_voltage', 'Description of gauge')
g8 = Gauge('ina3_voltage', 'Description of gauge')
g9 = Gauge('ina4_voltage', 'Description of gauge')
g10 = Gauge('ina5_voltage', 'Description of gauge')
g11 = Gauge('ads1_voltage', 'Description of gauge')
g12 = Gauge('ads2_voltage', 'Description of gauge')
g13 = Gauge('ads3_voltage', 'Description of gauge')
g14 = Gauge('ads4_voltage', 'Description of gauge')
g1.inc()      # Increment by 1
g1.dec(10)    # Decrement by given value
g1.set(ina1.current)   # Set to a given value
g2.set(ina2.current)   # Set to a given value
g3.set(ina3.current)   # Set to a given value
g4.set(ina4.current)
g5.set(ina5.current)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
        g1.set(ina1.current)   # Set to a given value
        g2.set(ina2.current)   # Set to a given value
        g3.set(ina3.current)   # Set to a given value
        g4.set(ina4.current)
        g5.set(ina5.current)
        g6.set(ina1.voltage)   # Set to a given value
        g7.set(ina2.voltage)   # Set to a given value
        g8.set(ina3.voltage)   # Set to a given value
        g9.set(ina4.voltage)
        g10.set(ina5.voltage)
        g11.set(chan1.voltage)
        g12.set(chan2.voltage)
        g13.set(chan3.voltage)
        g14.set(chan4.voltage)
