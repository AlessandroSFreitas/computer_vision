from djitellopy.tello import Tello

tello = Tello()

if not tello.connect():
  print("Cannot reach tello, aborting!")
  exit(1)

battery = tello.query_battery()

print("Bateria do Tello: ", battery.strip())
