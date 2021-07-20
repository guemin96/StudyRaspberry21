import RPi.GPIO as GPIO
import dht11
import time

pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin)

while True:
    try:
        result = instance.read()

        if result.is_valid():
            print('Temp : {0} C / Humidity : {1}'.format(result.temperature, result.humidity))
        else:
            print('Read error : {0}'.format(result.error_code))
        
        time.sleep(2)
    except Exception as e:
        print('error {0}'.format(e))