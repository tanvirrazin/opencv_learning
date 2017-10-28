import cv2
import numpy as np

def showFrame(name, img):
	img = cv2.resize(img, (570, 320))
	cv2.imshow(name, img)

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([150, 90, 0])
	upper_red = np.array([250, 250, 255])

	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	kernel = np.ones((5, 5), np.uint8)

	erosion = cv2.erode(mask, kernel, iterations=1)
	dilation = cv2.dilate(mask, kernel, iterations=1)

	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

	showFrame('frame', frame)
	showFrame('res', res)
	showFrame('erosion', erosion)
	showFrame('dilation', dilation)
	showFrame('opening', opening)
	showFrame('closing', closing)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
