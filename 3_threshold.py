import cv2

org_img = cv2.imread('./images/dark_bookpage.jpg')
_, thresh = cv2.threshold(org_img, 12, 255, cv2.THRESH_BINARY)
# THRESH_BINARY_INV
# THRESH_TRUNC
# THRESH_TOZERO
# THRESH_TOZERO_INV

grayscaled = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
_, thresh2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', org_img)
cv2.imshow('thresh', thresh)
cv2.imshow('thresh2', thresh2)
cv2.imshow('gaus', gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
