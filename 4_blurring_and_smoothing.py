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

	kernel = np.ones((15, 15), np.float32) / 255
	smoothed = cv2.filter2D(res, -1, kernel)
	blur = cv2.GaussianBlur(res, (15, 15), 0)
	median = cv2.medianBlur(res, 15)

	showFrame('frame', frame)
	showFrame('mask', mask)
	showFrame('res', res)
	showFrame('smoothed', smoothed)
	showFrame('blur', blur)
	showFrame('median', median)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
