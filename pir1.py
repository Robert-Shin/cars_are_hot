from gpiozero import MotionSensor
from time import sleep
pir = MotionSensor(4)
sleep(50)
print("detecting...")
pir.wait_for_motion()
while True:
	pir.wait_for_motion()
	print("aids... :(")
	sleep(5)
