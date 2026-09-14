import cv2

image = cv2.imread("photo.PNG")

cv2.imshow("practice image", image)

cv2.waitKey(15000)

cv2.destroyAllWindows()
