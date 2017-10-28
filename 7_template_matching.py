import cv2
import numpy as np

bgr_img = cv2.imread('./images/template_matching_image.jpg')
template = cv2.imread('./images/template_matching_template.jpg')

img_gray = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
temp_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
h, w = temp_gray.shape

res = cv2.matchTemplate(img_gray, temp_gray, cv2.TM_CCOEFF_NORMED)

threshold = 0.78

loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(bgr_img, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

cv2.imshow('detected', bgr_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
