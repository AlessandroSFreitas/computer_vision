from djitellopy import Tello
import cv2, math, time

# Inicia o SDK do Tello
tello = Tello()

if not tello.connect():
  print("Cannot reach tello, aborting!")
  exit(1)

tello.streamoff()
time.sleep(1)
tello.streamon()

# Nível da bateria do Tello
battery = tello.query_battery()

cv2.namedWindow("Tello")
frame_read = tello.get_frame_read()

while True:
  img = frame_read.frame
  cv2.imshow("drone", img)

  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    frame_read.stop()
    tello.streamoff()
    exit(0)
