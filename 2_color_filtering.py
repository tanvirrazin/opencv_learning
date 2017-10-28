import cv2
import numpy as np

def showFrame(name, img):
	img = cv2.resize(img, (570, 320))
	cv2.imshow(name, img)

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([150, 90, 230])
	upper_red = np.array([250, 150, 255])

	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	showFrame('frame', frame)
	showFrame('mask', mask)
	showFrame('res', res)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
