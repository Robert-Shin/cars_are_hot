from gpiozero import MotionSensor
from w1thermsensor import W1ThermSensor
from time import sleep
pir = MotionSensor(27)
sensor = W1ThermSensor()
sleep(50)
print("detecting...")
pir.wait_for_motion()

while True:
	pir.wait_for_motion()
	temp = sensor.get_temperature()
	print(temp)
	time.sleep(2)


