import cv2
import numpy as np

def showFrame(name, img):
	img = cv2.resize(img, (570, 320))
	cv2.imshow(name, img)

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	laplacian = cv2.Laplacian(frame, cv2.CV_64F)

	sobelX = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
	sobelY = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)

	edges = cv2.Canny(frame, 150, 250)

	showFrame('frame', frame)
	showFrame('laplacian', laplacian)
	showFrame('sobelX', sobelX)
	showFrame('sobelY', sobelY)
	showFrame('edges', edges)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
