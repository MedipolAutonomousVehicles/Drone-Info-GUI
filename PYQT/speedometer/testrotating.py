import cv2
def rotate(img, angle, scale: float = 1, center: tuple = None):
    (h, w) = img.shape[:2]
    if center is None:
        center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
#                       (rotate around, angle, scale)
    rotated = cv2.warpAffine(img, M, (w, h))
    return rotated
path = r"pointer.png"

img = cv2.imread(path)
newImg = rotate(img,15)
cv2.imshow("image",newImg)
cv2.imwrite("newNeedle.png",newImg)
cv2.waitKey(0)
