# Loading , Displaying, Resizing and Writing Images with python.

import cv2


# 0 means show in white and gray
img = cv2.imread("galaxy.jpg", 0)

print(type(img))

# print pixel array
print(img)

# show pixel size
print(img.shape)

# show image dimentions
print(img.ndim)


# resize image
# resized_image = cv2.resize(img, (400, 400))


# resizing while keeping ration same
resized_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))


# save resized image
cv2.imwrite("Galaxy_resized.jpg", resized_image)

cv2.imshow("Galaxy", resized_image)

# show image for 2000 micro seconds
cv2.waitKey(2000)

# after 2 sec close all window
cv2.destroyAllWindows()
