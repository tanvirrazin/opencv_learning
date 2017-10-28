import cv2

img = cv2.imread('./images/monstar_lab_logo.png', 1)
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	ims = cv2.resize(frame, (540, 320))
	cv2.imshow('Frame', ims)

	ims = cv2.resize(gray, (540, 320))
	cv2.imshow('Gray', ims)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
